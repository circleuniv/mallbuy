from fpdf import FPDF

def pdf_generator(items):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    for txt_content in items:
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"{txt_content}", ln=1)

    pdf.output("receipt.pdf")

if __name__ == '__main__':
    items = ["Receipt nr.1", "Article: Laptop Sven", "Price: 999"]
    pdf_generator(items)