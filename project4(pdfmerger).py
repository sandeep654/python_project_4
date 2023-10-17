from PyPDF2 import PdfWriter

Merge=["download.pdf" ,"download2.pdf"]

merger = PdfWriter()

for pdf in Merge:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
