from azure.ai.formrecognizer import AnalyzeResult
from utils import get_form_recognizer_client

def analyze_document(file_path: str) -> AnalyzeResult:
    client = get_form_recognizer_client()
    
    with open(file_path, "rb") as document:
        poller = client.begin_analyze_document("prebuilt-document", document)
        result = poller.result()

    return result

def extract_text(result: AnalyzeResult):
    print("Document Analyzed:")
    for page in result.pages:
        print(f"Page {page.page_number}")
        for line in page.lines:
            print(line.content)
