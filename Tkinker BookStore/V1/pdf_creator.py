# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.pagesizes import portrait
# from reportlab.platypus import Image, Table
# from datetime import datetime as dt

# def create_pdf(rows):
#         pdf_name = dt.now().strftime("%Y-%m-%d %H-%M-%S")+'.pdf'

#         c = canvas.Canvas(pdf_name, pagesize=portrait(A4))

#         c.setFont('Helvetica', 48, leading=None)
#         c.drawCentredString(215, 700, "Book Store")

#         c.setFont('Helvetica', 20, leading=None)
#         for i in range(0,len(rows)):
#                 c.drawString(20, 600-25*(i+1), str(i+1)+'\t'+rows[i][1]+'\t'+rows[i][2]+'\t'+str(rows[i][3])+'\t'+str(rows[i][4]))

        ## table.wrapOn(c, width, height)
#         c.showPage()
#         c.save()



from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch
from reportlab.platypus import SimpleDocTemplate, Image, Spacer, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_RIGHT
from datetime import datetime as dt

def create_pdf(data):
        pdf_name = dt.now().strftime("%Y-%m-%d %H-%M-%S")+'.pdf'
        doc = SimpleDocTemplate(pdf_name, pagesize=A4)

        logo = "python_logo.png"
        title = "BookStore"
        date = dt.now().strftime("%Y-%m-%d")
        body = "Contents:-"

        elements = []
        im = Image(logo, 1*inch, 1*inch)
        # im.hAlign = 'LEFT'
        d=[[]]
        d[0].append(im)
        styles=getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        styles.add(ParagraphStyle(name='Left', alignment=TA_LEFT))
        styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))
        ptext = '<font size=48>%s</font>' % title
        d[0].append(Paragraph(ptext, styles["Normal"]))
        t1=Table(d)
        t1.setStyle(TableStyle([
                ('ALIGN',(0,0),(0,0),'CENTER'),
                ('ALIGN',(1,0),(1,0),'LEFT'),
                ('VALIGN',(0,0),(0,0),'MIDDLE'),
                ('VALIGN',(1,0),(1,0),'TOP'),
        ]))
        elements.append(t1)
        elements.append(Spacer(1, 12))
        ptext = '<font size=12>Date: <u>%s</u></font>' % date
        elements.append(Paragraph(ptext, styles["Right"]))
        elements.append(Spacer(1, 16))
        ptext = '<font size=24><u>%s</u></font>' % body
        elements.append(Paragraph(ptext, styles["Left"]))
        elements.append(Spacer(1, 0.6*inch))

        # container for the 'Flowable' objects
        data.insert(0,('ID','Title','Author','Year','ISBN'))
        t2=Table(data)
        t2.setStyle(TableStyle([
                        ('TEXTFONT',(0, 0),(4, 0),'Helvetica-Bold'),
                        ('FONTSIZE',(0, 0),(4, 0),18),
                        ('VALIGN',(0, 0),(4, 0),'TOP'),
                        ('GRID',(0, 0),(4, 0),1,colors.black),
                        ('TEXTCOLOR',(0,0),(0,-1),colors.green),
                        ('TEXTCOLOR',(1,0),(1,-1),colors.blue),
                        ('TEXTCOLOR',(2,0),(2,-1),colors.cyan),
                        ('TEXTCOLOR',(3,0),(3,-1),colors.magenta),
                        ('TEXTCOLOR',(4,0),(4,-1),colors.red),
                        ('ALIGN',(0,0),(-1,-1),'CENTER'),
                        ('VALIGN',(0,1),(-1,-1),'MIDDLE'),
                        ('INNERGRID',(0,0),(-1,-1),0.5,colors.black),
                        ('BOX',(0,0),(-1,-1),1,colors.black)
                ]))
        for i in [0,3,4]:
                t2._argW[i]=1.1*inch
        t2._argH[0]=0.5*inch
        elements.append(t2)

        # write the document to disk
        doc.build(elements)