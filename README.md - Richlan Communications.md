# African Language Translation Pipeline

A reference implementation demonstrating Richlan Communications' approach to building specialized translation systems for medical, biblical, and technical content with focus on African languages.

## 🌍 Overview

This repository showcases the translation workflow methodology used in our client projects, featuring:

- **Glossary-driven translation** with domain-specific terminology management
- **Multi-engine support** (cloud APIs + local LLM integration)
- **Quality assurance workflows** with consistency checking
- **Batch processing capabilities** for scalable operations
- **Offline translation** using local models (Ollama, Mistral)
- **African language specialization** with cultural context awareness

> **Note:** This is a demonstration of our translation pipeline approach. Production deployments for clients are customized based on specific requirements and integration needs. See [DISCLAIMER.md](DISCLAIMER.md) for details.

## ✨ Key Capabilities

### 🎯 Specialized Translation Domains
- **Medical & Clinical Research**: Standardized medical terminology with glossary enforcement
- **Biblical & Religious Texts**: Original language consultation with linguistic precision
- **Technical Documentation**: Consistent technical vocabulary across versions
- **General Content**: News, articles, and educational materials

### 🔧 Technical Features
- **Terminology management** with automatic term matching and validation
- **Translation memory** for maintaining consistency across projects
- **Multi-format support** (DOCX, PDF, TXT, HTML, SRT)
- **Confidence scoring** to flag sections needing review
- **Hybrid translation** with automatic fallback between engines

### 🌐 Language Focus
Primary expertise in African languages with specialized glossaries:
- English ↔ Swahili (primary)
- Biblical Hebrew → Modern languages
- Extensible framework for additional language pairs

## 🏗️ System Architecture

```
Input Document
      ↓
Glossary Application (domain-specific terms)
      ↓
Translation Engine (cloud API or local LLM)
      ↓
Quality Assurance (consistency checks, confidence scoring)
      ↓
Output Document (format preserved)
```

See the full [architecture diagram](docs/architecture.md) for detailed flow.

## 📁 Repository Structure

```
translation-pipeline/
├── README.md              # This file
├── SERVICES.md            # Translation services offered
├── DISCLAIMER.md          # Important usage information
├── LICENSE                # MIT License
├── requirements.txt       # Python dependencies
├── src/
│   ├── core/              # Core translation logic
│   ├── integrations/      # API wrappers (Google, Ollama)
│   ├── processors/        # Document handling
│   └── utils/             # Support functions
├── glossaries/            # Domain-specific term databases
│   ├── medical_terms.json
│   └── README.md
├── config/                # Configuration templates
├── docs/                  # Additional documentation
├── examples/              # Usage examples
└── tests/                 # Validation tests
```

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/richlancommunications/translation-pipeline.git
cd translation-pipeline

pip install -r requirements.txt

# Copy and configure settings
cp config/translation_settings.example.yaml config/translation_settings.yaml
# Edit translation_settings.yaml with your API keys and preferences
```

### Basic Usage

```python
from src.core.translator import Translator

# Initialize with medical glossary
translator = Translator(
    source_lang="en",
    target_lang="sw",
    glossary_path="glossaries/medical_terms.json",
    use_local_llm=True
)

# Translate document
result = translator.translate_document(
    input_file="medical_report.docx",
    output_file="medical_report_sw.docx",
    domain="medical"
)

print(f"Confidence: {result.confidence_score}")
print(f"Terms matched: {len(result.glossary_matches)}")
```

See [docs/USAGE.md](docs/USAGE.md) for comprehensive examples.

## 📊 Example Results

Using this approach on medical content translation:

- **Terminology consistency**: Glossary terms matched and applied accurately
- **Format preservation**: Document structure and formatting maintained
- **Batch efficiency**: Multiple documents processed with consistent quality
- **Quality scoring**: Low-confidence sections flagged for human review

*Results vary based on content complexity, domain, and glossary coverage.*

## 🎯 Real-World Applications

This methodology has been used as the foundation for:

### Medical Translation Projects
- Clinical research documentation (English → Swahili)
- Patient information materials with medical term standardization
- Health education content with glossary-enforced consistency

### Biblical Education Content
- Scripture study materials with original language consultation
- Video script translation for biblical Hebrew teaching
- Theological text translation with semantic precision

### Content Automation
- RSS feed translation for news aggregation
- Automated multilingual content pipelines
- Batch processing for documentation updates

## 📚 Documentation

- **[USAGE.md](docs/USAGE.md)** - Detailed usage guide with code examples
- **[SERVICES.md](SERVICES.md)** - Translation and development services offered
- **[DISCLAIMER.md](DISCLAIMER.md)** - Important information about this repository
- **[PROJECT_SETUP.md](docs/PROJECT_SETUP.md)** - Complete setup instructions
- **[GLOSSARY_FORMAT.md](docs/GLOSSARY_FORMAT.md)** - Glossary structure specification

## 🔌 Integration Capabilities

### Translation Engines
- **Google Translate API** - Cloud-based translation with broad language support
- **Local LLMs (Ollama)** - Offline translation for privacy-sensitive content
- **Hybrid mode** - Automatic fallback for optimal results

### Workflow Integration
- API-accessible for system integration
- Batch processing for large-scale operations
- Translation memory for project consistency
- Quality reporting for human review workflows

## 💼 Professional Services

Interested in custom translation solutions or specialized translation services?

**See [SERVICES.md](SERVICES.md)** for:
- Translation service packages
- Custom pipeline development
- Consultation offerings
- Technical capabilities

**Contact:** richlancommunications@gmail.com

## 🤝 Use Cases

This approach is particularly valuable for:

- **Medical organizations** requiring precise terminology in African languages
- **Religious institutions** producing multilingual biblical content
- **Translation agencies** needing specialized domain expertise
- **NGOs** working in African contexts with consistent translation needs
- **Tech companies** localizing content for African markets

## 🛠️ Technology Stack

- **Python 3.8+** - Core implementation
- **Google Translate API** - Cloud translation service
- **Ollama/Mistral** - Local LLM integration
- **python-docx** - Document processing
- **PyPDF2** - PDF handling
- **YAML** - Configuration management

## 📈 Development Approach

This repository demonstrates:
- Modular architecture for extensibility
- Configuration-driven behavior
- Error handling and fallback strategies
- Quality assurance integration
- Production-inspired design patterns

## 🏢 About Richlan Communications

Richlan Communications provides specialized translation and language technology services with expertise in medical, biblical, and technical content for African languages.

**Website:** Coming soon  
**Email:** richlancommunications@gmail.com  
**GitHub:** github.com/richlancommunications

## 📄 License

MIT License - See [LICENSE](LICENSE) for details

## 📞 Contact

**For translation services or custom development:**
- **Email:** richlancommunications@gmail.com
- **GitHub:** github.com/richlancommunications

---

**Important:** This repository demonstrates our technical approach to translation challenges. For production projects, we provide customized solutions tailored to your specific needs, compliance requirements, and integration context. See [DISCLAIMER.md](DISCLAIMER.md) for full details.