from reportlab.platypus import SimpleDocTemplate,Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_report(path,text):
    doc=SimpleDocTemplate(path)
    doc.build([Paragraph(text,getSampleStyleSheet()['BodyText'])])
