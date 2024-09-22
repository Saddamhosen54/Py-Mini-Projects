# pip install pdfplumber, tkinter:

import pdfplumber
from docx import Document
import tkinter as tk
from tkinter import filedialog

def pdf_to_docx(pdf_path, docx_path):
    """Converts a PDF file to a DOCX file."""
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Create a new Document
        doc = Document()
        
        # Loop through all the pages in the PDF
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                doc.add_paragraph(text)
        
        # Save the DOCX file
        doc.save(docx_path)
        print(f"PDF file has been successfully converted to: {docx_path}")

def select_files():
    """Opens file dialogs for user input and output file selection."""
    # Open file dialog to select the input PDF file
    pdf_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF Files", "*.pdf")]
    )
    
    if pdf_path:
        # Open file dialog to select where to save the DOCX file
        docx_path = filedialog.asksaveasfilename(
            title="Save as DOCX file",
            defaultextension=".docx",
            filetypes=[("Word Document", "*.docx")]
        )
        
        if docx_path:
            # Convert the PDF to DOCX
            pdf_to_docx(pdf_path, docx_path)

if __name__ == "__main__":
    # Initialize the Tkinter application
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Call the function to start file selection
    select_files()
