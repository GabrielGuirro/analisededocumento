import sys
from analyze_document import analyze_document, extract_text

def main(file_path: str):
    result = analyze_document(file_path)
    extract_text(result)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path-to-document>")
        sys.exit(1)
    
    document_path = sys.argv[1]
    main(document_path)
