from fpdf import FPDF

pdf = FPDF(orientation="P", format="A4")

pdf.add_page()

pdf.set_font('Times', size=60.5)
pdf.cell(0, 50, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')
pdf.image("shirtificate.png", h=pdf.epw, w=pdf.epw)
pdf.set_auto_page_break(10)

pdf.set_font('Helvetica', 'B', size=25)
pdf.set_text_color(255,255,255)
answer = f"{input('Name: ')} took CS50"
pdf.cell(0, -200, answer, align='C')

pdf.output("shirtificate.pdf")
