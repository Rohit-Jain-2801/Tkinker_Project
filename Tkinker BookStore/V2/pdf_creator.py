from fpdf import FPDF
from datetime import datetime as dt

class CustomPDF(FPDF):
    def header(self):
        self.image('python_logo.png', 10, 8, 33)
        self.set_font('Arial', style='B', size=15)

        self.cell(70)
        self.set_font("helvetica", size=52, style='B')
        self.cell(0, 18, 'BookStore', ln=1)
        
        self.cell(84)
        self.set_font('helvetica', style='BI', size=15)
        self.cell(0, 5, 'A place for book lovers!', ln=1)

        self.ln(20)
        self.line(10, 40, 200, 40)
        self.set_line_width(1.2)

    def footer(self):
        self.set_y(-10)
        self.set_font('Arial', 'I', 8)

        page = 'Page ' + str(self.page_no()) + '/{nb}'
        self.cell(0, 10, page, 0, 0, 'C')

def create_pdf(data):
    pdf_name = dt.now().strftime("%Y-%m-%d %H-%M-%S")+'.pdf'
    body = "Contents:-"
    pdf = CustomPDF(orientation='P', unit='mm', format='A4')
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)

    data.insert(0,('ID','Title','Author','Year','ISBN'))
    col_width = [7,82,60,11,30]
    row_height = 1.2*pdf.font_size
    for row in data:
        i=0
        for item in row:
            pdf.cell(col_width[i], row_height,txt=str(item), border=1,align='C')
            i+=1
        pdf.ln(row_height)

    pdf.output(pdf_name)