from docx import Document

def extract_text_from_docx(file_path):
    """
    Extracts text from a DOCX file and prints it.

    Parameters:
    file_path (str): The path to the uploaded .docx file.

    Returns:
    str: The extracted text.
    """
    document = Document(file_path)
    full_text = []

    for para in document.paragraphs:
        full_text.append(para.text)

    extracted_text = "\n".join(full_text)

    print("Extracted Text:\n")
    print(extracted_text)

    return extracted_text
