from docx import Document
from PyPDF2 import PdfReader, PdfWriter

def convert_docx_to_pdf(docx_file, pdf_file):
    doc = Document(docx_file)
    doc.save(pdf_file)

def convert_pdf_to_docx(pdf_file, docx_file):
    pdf_reader = PdfReader(pdf_file)
    pdf_writer = PdfWriter()
    for page in pdf_reader.pages:
        pdf_writer.add_page(page)
    with open(docx_file, 'wb') as output:
        pdf_writer.write(output)
