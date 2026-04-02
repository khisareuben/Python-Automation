# PDF Toolkit using PyPDF2
# ------------------------
# Features:
# 1. Extract text from a PDF
# 2. Merge multiple PDFs
# 3. Split a PDF into individual pages
# 4. Rotate pages
# 5. Crop pages
# 6. Encrypt a PDF
# 7. Decrypt a PDF
# 8. Add metadata
# 9. Add watermark
# 10. Work with forms (extract fields)

from PyPDF2 import PdfReader, PdfWriter, PdfMerger

# 1. Extract text from a PDF
def extract_text(pdf_file):
    """Extract and print text from all pages of a PDF."""
    reader = PdfReader(pdf_file)
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        print(f"\n--- Page {i+1} ---\n{text}")

# 2. Merge multiple PDFs
def merge_pdfs(pdf_list, output_file):
    """Merge multiple PDFs into one."""
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_file)
    merger.close()
    print(f"✅ Merged PDFs saved as {output_file}")

# 3. Split a PDF into individual pages
def split_pdf(pdf_file):
    """Split a PDF into separate files for each page."""
    reader = PdfReader(pdf_file)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        filename = f"page_{i+1}.pdf"
        with open(filename, "wb") as f:
            writer.write(f)
        print(f"✅ Saved {filename}")

# 4. Rotate pages
def rotate_pdf(pdf_file, output_file, degrees=90):
    """Rotate all pages in a PDF by given degrees (90, 180, 270)."""
    reader = PdfReader(pdf_file)
    writer = PdfWriter()
    for page in reader.pages:
        page.rotate(degrees)
        writer.add_page(page)
    with open(output_file, "wb") as f:
        writer.write(f)
    print(f"✅ Rotated PDF saved as {output_file}")

# 5. Crop pages
def crop_pdf(pdf_file, output_file):
    """Crop the first page of a PDF to a smaller box."""
    reader = PdfReader(pdf_file)
    writer = PdfWriter()
    page = reader.pages[0]
    # Example crop box (adjust as needed)
    page.mediabox.lower_left = (100, 100)
    page.mediabox.upper_right = (400, 400)
    writer.add_page(page)
    with open(output_file, "wb") as f:
        writer.write(f)
    print(f"✅ Cropped PDF saved as {output_file}")

# 6. Encrypt a PDF
def encrypt_pdf(pdf_file, output_file, password):
    """Encrypt a PDF with a password."""
    reader = PdfReader(pdf_file)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(password)
    with open(output_file, "wb") as f:
        writer.write(f)
    print(f"✅ Encrypted PDF saved as {output_file}")

# 7. Decrypt a PDF
def decrypt_pdf(pdf_file, password):
    """Decrypt a PDF and print text from the first page."""
    reader = PdfReader(pdf_file)
    reader.decrypt(password)
    print(reader.pages[0].extract_text())

# 8. Add metadata
def add_metadata(pdf_file, output_file, metadata):
    """Add custom metadata to a PDF."""
    reader = PdfReader(pdf_file)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.add_metadata(metadata)
    with open(output_file, "wb") as f:
        writer.write(f)
    print(f"✅ Metadata added and saved as {output_file}")

# 9. Add watermark
def add_watermark(pdf_file, watermark_file, output_file):
    """Add a watermark to all pages of a PDF."""
    reader = PdfReader(pdf_file)
    watermark = PdfReader(watermark_file)
    writer = PdfWriter()
    for page in reader.pages:
        page.merge_page(watermark.pages[0])
        writer.add_page(page)
    with open(output_file, "wb") as f:
        writer.write(f)
    print(f"✅ Watermarked PDF saved as {output_file}")

# 10. Work with forms
def extract_form_fields(pdf_file):
    """Extract form fields from a PDF."""
    reader = PdfReader(pdf_file)
    fields = reader.get_fields()
    print("Form fields:", fields)


# ------------------------
# Example usage (uncomment what you need):
extract_text("yourPDF.pdf")
# merge_pdfs(["file1.pdf", "file2.pdf"], "merged.pdf")
# split_pdf("example.pdf")
# rotate_pdf("example.pdf", "rotated.pdf", 180)
# crop_pdf("example.pdf", "cropped.pdf")
# encrypt_pdf("example.pdf", "encrypted.pdf", "mypassword")
# decrypt_pdf("encrypted.pdf", "mypassword")
# add_metadata("example.pdf", "with_metadata.pdf", {"/Title": "My PDF", "/Author": "Harold"})
# add_watermark("example.pdf", "watermark.pdf", "watermarked.pdf")
# extract_form_fields("form.pdf")
