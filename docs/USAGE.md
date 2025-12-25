# Translation Pipeline - Usage Guide

Complete guide to using the African Language Translation Pipeline for various translation workflows.

## Table of Contents
1. [Installation & Setup](#installation--setup)
2. [Basic Translation](#basic-translation)
3. [Working with Glossaries](#working-with-glossaries)
4. [Batch Processing](#batch-processing)
5. [Quality Assurance](#quality-assurance)
6. [Advanced Workflows](#advanced-workflows)
7. [Troubleshooting](#troubleshooting)

---

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager
- (Optional) Ollama installed for local LLM support
- (Optional) Google Cloud account for Translate API

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

Required packages:
- `googletrans==4.0.0rc1` or `google-cloud-translate==3.x`
- `python-docx>=0.8.11`
- `PyPDF2>=3.0.0`
- `pyyaml>=6.0`
- `requests>=2.28.0`
- `beautifulsoup4>=4.11.0`
- `nltk>=3.8`

### Step 2: Configure API Keys

Edit `config/translation_settings.yaml`:

```yaml
translation:
  default_source_lang: "en"
  default_target_lang: "sw"
  
  # API configurations
  google_translate:
    enabled: true
    api_key: "YOUR_GOOGLE_API_KEY"
    project_id: "your-project-id"
  
  ollama:
    enabled: true
    base_url: "http://localhost:11434"
    model: "mistral"
    timeout: 120
  
  # Quality settings
  quality:
    min_confidence: 0.7
    enable_qa_checks: true
    glossary_required: true
```

### Step 3: Set Up Glossaries

Place your glossary files in the `glossaries/` directory or create new ones:

```bash
python scripts/create_glossary.py --domain medical --output glossaries/medical_terms.json
```

---

## Basic Translation

### Translating a Single Document

```python
from src.core.translator import Translator

# Initialize translator
translator = Translator(
    source_lang="en",
    target_lang="sw",
    glossary_path="glossaries/medical_terms.json"
)

# Translate document
result = translator.translate_document(
    input_file="report.docx",
    output_file="report_sw.docx"
)

# Check results
print(f"Status: {result.status}")
print(f"Words translated: {result.word_count}")
print(f"Confidence: {result.confidence_score}%")
print(f"Glossary terms used: {len(result.glossary_matches)}")
```

### Translating Plain Text

```python
# Quick text translation
text = "The patient presents with hypertension and diabetes."
translation = translator.translate_text(text)

print(f"Original: {text}")
print(f"Translation: {translation.text}")
print(f"Terms matched: {translation.glossary_terms}")
```

### Supported File Formats

- **DOCX**: Full formatting preservation
- **PDF**: Text extraction and translation (formatting may vary)
- **TXT**: Plain text with encoding support
- **HTML**: Web content with tag preservation
- **SRT**: Subtitle files with timing preservation

---

## Working with Glossaries

### Loading an Existing Glossary

```python
from src.core.glossary_manager import GlossaryManager

glossary = GlossaryManager("glossaries/medical_terms.json")

# View glossary statistics
stats = glossary.get_statistics()
print(f"Total terms: {stats['total_terms']}")
print(f"Domains covered: {stats['domains']}")
```

### Adding Terms to a Glossary

```python
# Add a single term
glossary.add_term(
    source="hemoglobin",
    target="hemoglobini",
    context="medical/laboratory",
    confidence=1.0,
    notes="Standard medical term, no alternatives"
)

# Add multiple terms
terms = [
    {
        "source": "blood pressure",
        "target": "shinikizo la damu",
        "context": "medical/cardiology",
        "confidence": 1.0
    },
    {
        "source": "heart rate",
        "target": "mapigo ya moyo",
        "context": "medical/cardiology",
        "confidence": 0.95,
        "alternatives": ["kasi ya moyo"]
    }
]

glossary.add_terms_batch(terms)
glossary.save()
```

### Searching Glossary Terms

```python
# Search by source term
results = glossary.search_source("blood")
# Returns: ["blood pressure", "blood sugar", "blood type"]

# Search by context
cardio_terms = glossary.filter_by_context("medical/cardiology")

# Get term with all metadata
term_info = glossary.get_term("hypertension")
print(term_info)
# {
#   "source": "hypertension",
#   "target": "shinikizo la damu",
#   "context": "medical/cardiology",
#   "confidence": 1.0,
#   "usage_count": 47,
#   "last_updated": "2024-12-01"
# }
```

### Creating Domain-Specific Glossaries

```python
# Create specialized glossary from existing terms
medical_glossary = glossary.filter_by_context("medical")
medical_glossary.save("glossaries/medical_only.json")

# Merge multiple glossaries
from src.utils.glossary_tools import merge_glossaries

merged = merge_glossaries(
    ["glossaries/medical_terms.json", "glossaries/clinical_research.json"],
    output="glossaries/medical_complete.json",
    conflict_resolution="highest_confidence"  # or "manual"
)
```

---

## Batch Processing

### Translating Multiple Files

```python
from src.processors.batch_processor import BatchProcessor

processor = BatchProcessor(
    source_lang="en",
    target_lang="sw",
    glossary_path="glossaries/medical_terms.json",
    num_workers=4  # Parallel processing
)

# Process all files in a directory
results = processor.process_directory(
    input_dir="./documents/medical_reports",
    output_dir="./translated/medical_reports_sw",
    file_types=[".docx", ".pdf"],
    recursive=True
)

# Review results
for result in results:
    print(f"{result.filename}: {result.status}")
    if result.status == "success":
        print(f"  Confidence: {result.confidence_score}%")
    else:
        print(f"  Error: {result.error_message}")
```

### Processing with Custom Filters

```python
# Only process files modified in last 7 days
from datetime import datetime, timedelta

processor.process_directory(
    input_dir="./documents",
    output_dir="./translated",
    filter_func=lambda f: f.modified_time > datetime.now() - timedelta(days=7)
)

# Only process files containing specific text
processor.process_directory(
    input_dir="./documents",
    output_dir="./translated",
    content_filter=lambda text: "clinical trial" in text.lower()
)
```

### Progress Monitoring

```python
# With progress callback
def progress_callback(current, total, filename):
    percent = (current / total) * 100
    print(f"Progress: {percent:.1f}% - Processing: {filename}")

processor.process_directory(
    input_dir="./documents",
    output_dir="./translated",
    progress_callback=progress_callback
)
```

---

## Quality Assurance

### Running QA Checks

```python
from src.core.quality_checker import QualityChecker

checker = QualityChecker(glossary_path="glossaries/medical_terms.json")

# Check a translated document
qa_result = checker.check_translation(
    source_file="original.docx",
    translated_file="translated.docx"
)

# Review QA report
print(f"Overall Score: {qa_result.overall_score}/100")
print(f"\nIssues Found:")
for issue in qa_result.issues:
    print(f"  - {issue.severity}: {issue.description}")
    print(f"    Location: Line {issue.line_number}")
    print(f"    Suggestion: {issue.suggestion}")
```

### QA Categories

The quality checker evaluates:

1. **Glossary Consistency**: Are terms translated consistently?
2. **Format Preservation**: Is document structure maintained?
3. **Completeness**: Are all sections translated?
4. **Terminology Accuracy**: Are specialized terms correctly used?
5. **Context Appropriateness**: Does translation match domain context?

### Generating QA Reports

```python
# Generate comprehensive QA report
report = checker.generate_report(
    source_file="original.docx",
    translated_file="translated.docx",
    output_format="html"  # or "pdf", "json"
)

report.save("qa_report.html")
```

### Example QA Report Output

```
Quality Assurance Report
========================
Document: medical_report_2024.docx
Translated: 2024-12-13
Overall Score: 87/100

✓ Glossary Consistency: 95/100
  - 47 of 50 medical terms matched glossary
  - 3 terms need review: "biomarker", "cohort", "endpoint"

✓ Format Preservation: 92/100
  - Headers maintained: ✓
  - Tables preserved: ✓
  - Footnotes: 2 missing

⚠ Completeness: 78/100
  - 2 paragraphs flagged for review
  - 1 section appears incomplete

Recommendations:
1. Review "biomarker" translation - consider adding to glossary
2. Check paragraph 7 - low confidence score (0.62)
3. Verify table 3 formatting
```

---

## Advanced Workflows

### Hybrid Translation (Multiple Engines)

```python
# Use multiple translation engines with fallback
translator = Translator(
    source_lang="en",
    target_lang="sw",
    engines={
        "primary": {
            "type": "ollama",
            "model": "mistral",
            "priority": 1
        },
        "fallback": {
            "type": "google",
            "api_key": "YOUR_KEY",
            "priority": 2
        }
    },
    fallback_on_low_confidence=True,
    min_confidence_threshold=0.75
)

result = translator.translate_document("document.docx")
print(f"Primary engine: {result.primary_engine_used}")
print(f"Fallback used: {result.fallback_triggered}")
```

### Translation Memory Integration

```python
# Enable translation memory for consistency
translator.enable_translation_memory(
    db_path="translation_memory.db",
    fuzzy_match_threshold=0.85
)

# Translation memory will automatically:
# - Store all translations
# - Suggest similar translations
# - Maintain consistency across projects
```

### Custom Pre/Post-Processing

```python
# Add custom processing steps
def preprocess(text):
    # Custom preprocessing (e.g., expand abbreviations)
    text = text.replace("pt.", "patient")
    text = text.replace("dx", "diagnosis")
    return text

def postprocess(text):
    # Custom postprocessing (e.g., format numbers)
    import re
    text = re.sub(r'(\d+)mg', r'\1 mg', text)
    return text

translator.add_preprocessor(preprocess)
translator.add_postprocessor(postprocess)

result = translator.translate_document("medical_notes.docx")
```

### Integration with External Systems

```python
# Example: RSS feed translation
from src.integrations.rss_translator import RSSTranslator

rss = RSSTranslator(
    feed_url="https://example.com/medical-news/feed",
    translator=translator
)

# Translate latest articles
translated_articles = rss.translate_latest(limit=10)

for article in translated_articles:
    print(f"Title: {article.translated_title}")
    print(f"Content: {article.translated_content[:200]}...")
```

---

## Troubleshooting

### Common Issues

#### Issue: Low confidence scores

```python
# Solution: Increase glossary coverage
result = translator.translate_document("document.docx")

if result.confidence_score < 0.7:
    # Identify missing terms
    missing_terms = result.get_untranslated_terms()
    print(f"Consider adding these terms to glossary: {missing_terms}")
```

#### Issue: Formatting lost in PDF translation

```python
# Solution: Use OCR preprocessing
from src.processors.pdf_processor import PDFProcessor

pdf_proc = PDFProcessor(use_ocr=True)
text = pdf_proc.extract_text("document.pdf", preserve_layout=True)
translation = translator.translate_text(text)
```

#### Issue: API rate limits

```python
# Solution: Enable rate limiting and caching
translator.configure_api(
    rate_limit=100,  # requests per minute
    enable_cache=True,
    retry_on_limit=True,
    retry_delay=60  # seconds
)
```

### Getting Help

- Check the [FAQ](docs/FAQ.md)
- Review [API documentation](docs/API_INTEGRATION.md)
- Report issues on [GitHub Issues](https://github.com/richlancommunications/translation-pipeline/issues)

---

## Performance Optimization Tips

1. **Use caching** for repeated translations
2. **Enable batch processing** for multiple files
3. **Preload glossaries** at startup
4. **Use local LLMs** for offline/faster translation
5. **Configure parallel workers** based on your CPU cores

```python
# Optimized configuration
translator = Translator(
    cache_enabled=True,
    cache_ttl=86400,  # 24 hours
    num_workers=8,
    preload_glossary=True,
    use_local_llm=True
)
```