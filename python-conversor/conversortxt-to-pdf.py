from fpdf import FPDF

# Read .txt file 
with open("entrance.txt", "r", encoding="utf-8") as file:
  text = file.read()

# Create a PDF with ,txt content
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, text)

pdf.output("exit.pdf")