from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(text, path):

    c = canvas.Canvas(path, pagesize=letter)

    y = 750

    for line in text.split("\n"):

        c.drawString(50, y, line)

        y -= 15

        if y < 50:
            c.showPage()
            y = 750

    c.save()
