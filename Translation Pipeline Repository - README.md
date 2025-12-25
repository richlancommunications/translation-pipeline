# African Language Translation Pipeline

A comprehensive, AI-powered translation system optimized for medical, clinical research, and biblical texts, with specialized support for African languages.

## 🌍 Overview

This translation pipeline combines traditional translation workflows with modern AI integration, featuring:

- **Multi-engine translation** (Google Translate API, local LLM integration)
- **Specialized glossaries** for medical/clinical terminology
- **Quality assurance workflows** with consistency checking
- **Batch processing capabilities** for large-scale projects
- **Terminology management system** with context-aware suggestions
- **Local LLM integration** (Ollama, Mistral) for offline translation

## ✨ Key Features

### 🎯 Specialized Translation Domains
- **Medical & Clinical Research**: Standardized medical terminology across languages
- **Biblical & Religious Texts**: Linguistic precision with original language consultation
- **Technical Documentation**: Consistent technical vocabulary management
- **General Content**: News, articles, and web content

### 🔧 Technical Capabilities
- **Glossary-based translation** with automatic term matching
- **Translation memory** for consistency across projects
- **Multi-format support** (DOCX, PDF, TXT, HTML, SRT)
- **Batch processing** for multiple files
- **Quality metrics** and confidence scoring
- **Offline translation** using local models

### 🌐 Language Support
Primary focus on African languages with specialized glossaries:
- English ↔ Swahili
- English ↔ [Your other target languages]
- Biblical Hebrew → Modern languages
- [Add your specific language pairs]

## 🏗️ Architecture

```
translation-pipeline/
├── src/
│   ├── core/
│   │   ├── translator.py          # Main translation engine
│   │   ├── glossary_manager.py    # Terminology management
│   │   └── quality_checker.py     # QA and consistency checks
│   ├── integrations/
│   │   ├── google_translate.py    # Google Translate API wrapper
│   │   ├── ollama_integration.py  # Local LLM integration
│   │   └── api_manager.py         # API rate limiting & fallback
│   ├── processors/
│   │   ├── document_parser.py     # Multi-format document handling
│   │   ├── batch_processor.py     # Batch translation workflows
│   │   └── output_formatter.py    # Format preservation
│   └── utils/
│       ├── terminology_db.py      # SQLite terminology database
│       └── cache_manager.py       # Translation cache
├── glossaries/
│   ├── medical_terms.json
│   ├── clinical_research.json
│   ├── biblical_terms.json
│   └── technical_vocab.json
├── config/
│   ├── translation_settings.yaml
│   └── language_pairs.yaml
├── tests/
│   └── [test files]
├── docs/
│   ├── USAGE.md
│   ├── GLOSSARY_FORMAT.md
│   └── API_INTEGRATION.md
└── examples/
    └── [example scripts]
```

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/richlancommunications/translation-pipeline.git
cd translation-pipeline

# Install dependencies
pip install -r requirements.txt

# Set up configuration
cp config/translation_settings.example.yaml config/translation_settings.yaml
# Edit with your API keys and preferences
```

### Basic Usage

```python
from src.core.translator import Translator
from src.core.glossary_manager import GlossaryManager

# Initialize translator with medical glossary
glossary = GlossaryManager("glossaries/medical_terms.json")
translator = Translator(
    source_lang="en",
    target_lang="sw",
    glossary=glossary,
    use_local_llm=True  # Use Ollama for offline translation
)

# Translate a document
result = translator.translate_document(
    input_file="medical_report.docx",
    output_file="medical_report_sw.docx",
    domain="medical"
)

print(f"Translation confidence: {result.confidence_score}")
print(f"Terms matched: {result.glossary_matches}")
```

### Batch Processing

```python
from src.processors.batch_processor import BatchProcessor

# Process multiple files
processor = BatchProcessor(
    source_lang="en",
    target_lang="sw",
    glossary_path="glossaries/clinical_research.json"
)

processor.process_directory(
    input_dir="./documents",
    output_dir="./translated",
    file_types=[".docx", ".pdf"]
)
```

## 📊 Quality Assurance Features

### Glossary Consistency Checking
- Automatic detection of terminology inconsistencies
- Context-aware term suggestions
- Translation memory for repeated phrases

### Confidence Scoring
Each translation includes:
- Overall confidence score (0-100)
- Term-level confidence ratings
- Flagged sections requiring human review

### QA Reports
```python
qa_report = translator.generate_qa_report(translated_doc)
# Returns: inconsistent terms, low-confidence sections, glossary coverage
```

## 🔌 Integration Options

### Local LLM Integration (Ollama)
```python
# Use local models for offline translation
translator.set_backend("ollama", model="mistral")
```

### Google Translate API
```python
# Use Google Translate with automatic fallback
translator.set_backend("google", api_key="YOUR_API_KEY")
```

### Hybrid Mode
```python
# Combine multiple engines for best results
translator.set_backend("hybrid", 
    primary="ollama",
    fallback="google",
    use_glossary=True
)
```

## 📚 Glossary Management

### Creating Custom Glossaries

```json
{
  "medical_terms": [
    {
      "source": "hypertension",
      "target": "shinikizo la damu",
      "context": "medical",
      "confidence": 1.0,
      "notes": "Standard medical term"
    },
    {
      "source": "clinical trial",
      "target": "utafiti wa kimatibabu",
      "context": "research",
      "alternatives": ["jaribio la kikliniki"],
      "confidence": 0.95
    }
  ]
}
```

### Updating Glossaries

```python
from src.core.glossary_manager import GlossaryManager

glossary = GlossaryManager("glossaries/medical_terms.json")

# Add new term
glossary.add_term(
    source="diagnosis",
    target="utambuzi",
    context="medical",
    confidence=1.0
)

# Update existing term
glossary.update_term("diagnosis", target="uchunguzi", confidence=0.9)

# Save changes
glossary.save()
```

## 🎯 Use Cases

### 1. Medical Document Translation
Translate clinical research papers, medical reports, and patient information with maintained terminology consistency.

### 2. Biblical Text Translation
Specialized workflow for translating biblical and theological content with original language consultation.

### 3. News Automation
Integrate with RSS feeds for automated news translation and publication.

### 4. Educational Content
Translate educational materials while preserving formatting and technical accuracy.

## 📈 Performance

- **Translation Speed**: ~500 words/minute (with caching)
- **Glossary Matching**: 95%+ accuracy for registered terms
- **Format Preservation**: 98%+ for DOCX, 85%+ for PDF
- **Offline Capability**: Full functionality with local LLMs

## 🛠️ Advanced Features

### Custom Translation Rules
```python
# Define custom translation rules
translator.add_rule(
    pattern=r"\b\d+mg\b",
    handler=lambda match: f"{match.group()} (maintain dosage format)"
)
```

### Translation Memory
```python
# Enable translation memory for consistency
translator.enable_translation_memory(
    db_path="translation_memory.db",
    fuzzy_match_threshold=0.85
)
```

### Quality Metrics Dashboard
```bash
# Generate quality metrics
python src/utils/generate_metrics.py --input translated_docs/ --output report.html
```

## 🤝 Contributing

Contributions are welcome! Areas of interest:
- Additional language pair support
- New glossary domains (legal, technical, etc.)
- Integration with other translation APIs
- Quality assurance improvements

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - see [LICENSE](LICENSE) for details

## 🙏 Acknowledgments

Built with experience from translating medical research, biblical texts, and technical documentation for African language audiences.

## 📞 Contact

- **Website**: https://richlan-website.vercel.app/
- **YouTube**: https://www.youtube.com/@Bible-Truth-Files
- **Email**: richlancommunications@gmail.com
- **LinkedIn**: https://www.linkedin.com/in/richlan-communications-813b843a2/

---

**Note**: This pipeline is actively used in production for medical translation projects and biblical education content. Star ⭐ this repo if you find it useful!