import pymupdf
def pdf_text_reader(pdf_path):
    print("Opening PDF...")
    doc=pymupdf.open(pdf_path)
    print("PDF loaded successfully")
    print(f"Total Pages = {len(doc)}")
    all_text=""
    for page_number,page in enumerate(doc,start=1):
        print(f"Reading page {page_number}")
        all_text += page.get_text()
        all_text +="\n"
    doc.close()
    return all_text