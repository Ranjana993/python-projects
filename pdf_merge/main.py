from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs=[]
n = int(input("How many pdfs you want to merge?\n"))
for i in range(n):
  name = input(f"Enter the name of pdfs {i+1}: ")
  pdfs.append(name)

for pdf in pdfs:
  merger.append(pdf)

merger.write("merged_pdf.pdf")
merger.close()    
