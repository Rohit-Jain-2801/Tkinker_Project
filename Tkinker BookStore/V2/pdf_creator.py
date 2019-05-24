from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import portrait
from reportlab.platypus import Image, Table
from datetime import datetime as dt
import backend as bk

def create_pdf():
        try:
                rows = bk.view()
                print(rows)
        except Exception as err:
                tkmb.showwarning('Records',err,parent=window)
        pdf_name = dt.now().strftime("%Y-%m-%d %H-%M-%S")+'.pdf'

        c = canvas.Canvas(pdf_name, pagesize=portrait(A4))

        c.setFont('Helvetica', 48, leading=None)
        c.drawCentredString(215, 700, "Book Store")

        c.setFont('Helvetica', 20, leading=None)
        for i in range(0,len(rows)):
                c.drawString(20, 600-25*(i+1), str(i+1)+'\t'+rows[i][1]+'\t'+rows[i][2]+'\t'+str(rows[i][3])+'\t'+str(rows[i][4]))

        c.showPage()
        c.save()