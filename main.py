from utils.pdf_reader import pdf_text_reader
from utils.text_cleaner import text_clean
from utils.chunker import make_chunks
from utils.llm import summarize,final_summarize
import time


def main():
    pdf_text=pdf_text_reader("pdfs/document_2.pdf") 
    clean_text=text_clean(pdf_text)
    chunk_list=make_chunks(clean_text,chunk_size=800)
    print(f"Total Chunks: {len(chunk_list)}")
    print()
    all_summaries = []


    for i,chunk in enumerate(chunk_list,start=1):
        print(f"Sumarizing chunk {i}/{len(chunk_list)}...")
        summary=summarize(chunk)
        all_summaries.append(summary)

    print("\nCreating final summary...\n")
    final_summary=final_summarize(all_summaries)

    print("\n===== FINAL SUMMARY ====\n")
    print(final_summary)


if __name__ == "__main__":
    main()