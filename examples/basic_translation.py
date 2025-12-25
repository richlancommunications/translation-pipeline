"""
Basic translation example using the translation pipeline.

This script demonstrates:
- Initializing the translator with a glossary
- Translating text with domain context
- Accessing translation metadata
- Displaying glossary matches
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.translator import Translator


def main():
    print("=" * 70)
    print("BASIC TRANSLATION EXAMPLE")
    print("=" * 70)
    print()
    
    # Initialize translator with medical glossary
    print("Initializing translator...")
    translator = Translator(
        source_lang="en",
        target_lang="sw",
        glossary_path="glossaries/medical_terms.json",
        use_local_llm=True  # Set to False to use Google Translate
    )
    print(f"✓ Translator initialized: {translator.source_lang} → {translator.target_lang}")
    print(f"✓ Glossary loaded: {len(translator.glossary)} terms")
    print()
    
    # Sample medical text
    text = """
    The patient presents with hypertension and elevated blood sugar levels.
    Current medication includes insulin and blood pressure medication.
    Follow-up appointment scheduled for blood test and heart rate monitoring.
    """
    
    print("Source text:")
    print("-" * 70)
    print(text.strip())
    print("-" * 70)
    print()
    
    # Translate with medical domain context
    print("Translating...")
    result = translator.translate_text(text.strip(), domain="medical")
    print("✓ Translation complete")
    print()
    
    # Display translation
    print("Translation:")
    print("-" * 70)
    print(result.text)
    print("-" * 70)
    print()
    
    # Display metadata
    print("Translation Metadata:")
    print("-" * 70)
    print(f"Confidence Score:    {result.confidence_score * 100:.1f}%")
    print(f"Word Count:          {result.word_count}")
    print(f"Engine Used:         {result.engine_used}")
    print(f"Glossary Matches:    {len(result.glossary_matches)}")
    print(f"Status:              {result.status}")
    print()
    
    # Show glossary matches
    if result.glossary_matches:
        print("Glossary Terms Applied:")
        print("-" * 70)
        for i, match in enumerate(result.glossary_matches, 1):
            print(f"{i}. {match['source']:25} → {match['target']}")
            print(f"   Context: {match['context']}")
            print(f"   Confidence: {match['confidence']}")
            print()
    else:
        print("No glossary terms were matched in this text.")
        print()
    
    # Additional information
    if result.metadata:
        print("Additional Information:")
        print("-" * 70)
        coverage = result.metadata.get('glossary_coverage', 0)
        print(f"Glossary Coverage:   {coverage * 100:.1f}%")
        if result.metadata.get('domain'):
            print(f"Domain Context:      {result.metadata['domain']}")
        print()
    
    print("=" * 70)
    print("Example completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)