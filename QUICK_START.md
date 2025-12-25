# Quick Start Guide

Get up and running with the translation pipeline in 10 minutes.

## Prerequisites

- Python 3.8 or higher
- pip package manager
- (Optional) Git for cloning the repository
- (Optional) Ollama for local LLM support

## Step 1: Get the Code

### Option A: Clone from GitHub
```bash
git clone https://github.com/richlancommunications/translation-pipeline/git
cd translation-pipeline
```

### Option B: Download ZIP
1. Download ZIP from GitHub
2. Extract to a folder
3. Open terminal in that folder

## Step 2: Install Dependencies

```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

## Step 3: Configure Settings

```bash
# Copy example configuration
cp config/translation_settings.example.yaml config/translation_settings.yaml

# Edit the configuration file
# - Add your Google Translate API key (optional)
# - Configure Ollama settings (if using local LLM)
# - Adjust language pairs as needed
```

**Minimum configuration** (edit `config/translation_settings.yaml`):
```yaml
translation:
  default_source_lang: "en"
  default_target_lang: "sw"
  
  engines:
    ollama:
      enabled: true
      base_url: "http://localhost:11434"
```

## Step 4: Test the Installation

Run the basic example:

```bash
python examples/basic_translation.py
```

You should see:
- Translator initialization
- Sample text translation
- Translation metadata
- Glossary matches

## Step 5: Try Your Own Translation

### Simple Text Translation

Create a file `my_test.py`:

```python
from src.core.translator import Translator

# Initialize
translator = Translator(
    source_lang="en",
    target_lang="sw",
    glossary_path="glossaries/medical_terms.json"
)

# Translate
text = "The patient has high blood pressure."
result = translator.translate_text(text)

print(f"Original: {text}")
print(f"Translation: {result.text}")
print(f"Confidence: {result.confidence_score * 100}%")
```

Run it:
```bash
python my_test.py
```

### Document Translation

```python
from src.core.translator import Translator

translator = Translator(
    source_lang="en",
    target_lang="sw",
    glossary_path="glossaries/medical_terms.json"
)

result = translator.translate_document(
    input_file="your_document.docx",
    output_file="translated_document.docx"
)

print(f"Translation completed with {result.confidence_score * 100}% confidence")
```

## Common Setup Issues

### Issue: "Module not found"
**Solution:** Make sure you're in the project directory and virtual environment is activated

```bash
# Check if in right directory
ls  # Should see src/, glossaries/, etc.

# Activate virtual environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### Issue: "Ollama connection failed"
**Solution:** Either install Ollama or use Google Translate instead

```python
# Use Google Translate instead
translator = Translator(
    source_lang="en",
    target_lang="sw",
    use_local_llm=False  # This will use Google Translate
)
```

### Issue: "Glossary file not found"
**Solution:** Verify the glossary path

```bash
# Check if file exists
ls glossaries/medical_terms.json

# If missing, you may need to create it or check the path
```

## Next Steps

Once you have the basic setup working:

1. **Read the full documentation**
   - [USAGE.md](docs/USAGE.md) for detailed examples
   - [SERVICES.md](SERVICES.md) for professional services

2. **Customize for your needs**
   - Add your own glossaries
   - Configure for your language pairs
   - Adjust quality settings

3. **Try advanced features**
   - Batch processing
   - Custom glossaries
   - Quality assurance

## Need Help?

- **Documentation issues:** Check [docs/USAGE.md](docs/USAGE.md)
- **Technical questions:** Open a GitHub issue
- **Professional services:** Email [richlancommunications@gmail.com]

## Uninstallation

To remove the installation:

```bash
# Deactivate virtual environment
deactivate

# Remove the directory
cd ..
rm -rf translation-pipeline  # or delete folder manually
```

---

**Estimated setup time:** 5-10 minutes  
**Difficulty:** Beginner-friendly

For more advanced usage, see the full [USAGE.md](docs/USAGE.md) documentation.