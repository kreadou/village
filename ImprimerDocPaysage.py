# -*- coding:utf-8 -*-
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4,A3,A5,A6,letter, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.rl_config import defaultPageSize
import time

styles = getSampleStyleSheet()

PAGE_HEIGHT=defaultPageSize[1]
PAGE_WIDTH=defaultPageSize[0]


class ImprimerDocPaysage():
    def __init__(self):
        self.temps=''
        self.story=[]
        self.largCol=160 #en portrait
        self.positionPage=7 #en portrait
        self.pageInfo=''
        self.pageInfo1=''
        self.pageInfo2=''
        self.piedPage1=''#"Abidjan - Cocody, route de l'Université, boulevard F. Mitterand face Ecole de Gendarmerie"
        self.piedPage2=""#"Tél.: 22 48 48 12 Fax (225) 22 48 48 14 CC:02 193 40 H RC: 279162 N° Compte standard : 0100101102800"
        self.piedPage3=""#"Centre impôts Cocody 17 BP 84 Abidjan 17 - wwww.hec.ci / e-mail : info@hec.ci"
        self.logo=""
          
        self.entete=[['','','','','','','','','','','','','',''],
                     ['','','','','','','','','','','','','',''],
                     ['','','','','','','','','','','','','',''],
                     ['','','','','','','','','','','','','',''],
                     ['','','','','','','','','','','','','','']]
        ts=TableStyle([#('GRID', (0,0), (-1,-1), 1, colors.black), 
        ('SIZE', (0,0), (-1,-1), 10),
        
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'), 
        ('ALIGN', (0,0), (0,-3), 'LEFT'),
        ('ALIGN', (2,0), (-1,-1), 'RIGHT'),
        
        ('SPAN', (3,2), (10,2)),
        ('ALIGN', (3,2), (10,2), 'CENTER'),
        ('SPAN', (3,3), (10,3)),
        ('ALIGN', (3,3), (10,3), 'CENTER'),
        ('FONTNAME', (3,3), (10,3), 'Times-BoldItalic'),

        ('SIZE', (3,0), (4,0), 8),
        ('ALIGN', (3,0), (4,0), 'CENTER'),
        ])
        self.t=Table(self.entete,[56],len(self.entete)*[0.4*cm])
        self.t.setStyle(ts)
        
    def myFirstPage(self, canvas, doc):
        canvas.saveState()
        #self.story.insert(0,Paragraph('', self.styles["Title"]))
        #self.story.insert(0,Paragraph('', self.styles["Title"]))
        #print 'page ',doc.pageSize
        #if self.format==landscape(A4):self.story.insert(0,self.td)
        self.story.insert(0,self.t)
        #canvas.setFont('Times-Roman',9)
        #canvas.setLineWidth(0.5)
        #canvas.line(200,760,400,760)
        """
        canvas.setFont('Times-Roman',8)
        self.temps=str(time.strftime('%d/%m/%y à %H:%M',time.localtime()))
        canvas.drawString(inch, 0.3*inch, "%s" % self.pageInfo)
        """
        
        canvas.setFont('Times-Roman',10)
        #canvas.setPageSize(landscape(A4))
        if self.piedPage1:canvas.line(inch,0.7*inch, PAGE_WIDTH-inch, 0.7*inch)
        canvas.drawCentredString(PAGE_WIDTH/2, 0.5 * inch, "%s" % (self.piedPage1))
        canvas.drawCentredString(PAGE_WIDTH/2, 0.35 * inch, "%s" % (self.piedPage2))
        canvas.drawCentredString(PAGE_WIDTH/2, 0.2 * inch, "%s" % (self.piedPage3))
        canvas.restoreState()

    def myLaterPages(self, canvas, doc):
        canvas.saveState()
        canvas.setFont('Times-Roman',10)
        
    
        if self.piedPage1:canvas.line(inch,0.7*inch, PAGE_WIDTH-inch, 0.7*inch)
        canvas.drawCentredString(PAGE_WIDTH/2, 0.5 * inch, "%s" % (self.piedPage1))
        canvas.drawCentredString(PAGE_WIDTH/2, 0.35 * inch, "%s" % (self.piedPage2))
        canvas.drawCentredString(PAGE_WIDTH/2, 0.2 * inch, "%s" % (self.piedPage3))
        
        self.temps = str(time.strftime('%d/%m/%y à %H:%M',time.localtime()))
        canvas.drawString(PAGE_WIDTH, 0.2 * inch, "le %s - Page %s" % (self.temps, self.doc.page))
        canvas.restoreState()

    def header(self, txt, style=styles["Heading1"], klass=Paragraph, sep=0.3):
        s = Spacer(0.2*inch, sep*inch)
        self.story.append(s)
        para = klass(txt, style)
        self.story.append(para)
    
    def p(self, txt):
        return self.header(txt, style=self.ParaStyle, sep=0.1)

    def pre(self, txt):
        s=Spacer(0.1*inch, 0.1*inch)
        self.story.append(s)
        p=Preformatted(txt, self.PreStyle)
        self.story.append(p)
    
    def miseAjourEntete(self, canvas, doc):
        pass
    
    def go(self, fichier='fichier.pdf', format=A4, topMargin=20):
        try:
            self.doc=SimpleDocTemplate(fichier,pagesize=format, rightMargin=24,leftMargin=24,topMargin=15,bottomMargin=18)
            self.doc.build(self.story, onFirstPage=self.myFirstPage, onLaterPages=self.myLaterPages)
        except:pass    