import sys
from src.gemini_client import generate_text

if len(sys.argv) < 2:
    print("Usage: python ask.py '<your question here>'")
    sys.exit(1)

print(generate_text(sys.argv[1]))
