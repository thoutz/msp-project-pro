
from reportlab.pdfgen import canvas

class BillingService:
    def generate_invoice(self, client_name, items):
        filename = f"{client_name}_invoice.pdf"
        c = canvas.Canvas(filename)
        c.drawString(100, 800, f"Invoice for {client_name}")
        y = 750
        for item in items:
            c.drawString(100, y, f"{item['desc']} - ${item['amount']}")
            y -= 20
        c.save()
        return filename
