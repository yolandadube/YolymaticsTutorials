from fpdf import FPDF
from datetime import datetime

# Invoice details
invoice_number = f"INV-{datetime.now().strftime('%Y%m%d-%H%M%S')}_Bella_Grasso"
invoice_date = datetime.now().strftime('%d/%m/%Y')
student_name = "Bella Grasso"
parent_name = "Rosaria Grasso"
subject = "Discrete Maths (Number Theory and Groups)"
rate_per_hour = 350

# Lessons taken
lessons = [
    ("Monday (08/09)", 2),
    ("Wednesday (10/09)", 2),
    ("Friday (12/09)", 2),
    ("Saturday (13/09)", 2),
    ("Sunday (21/09)", 2),
    ("Sunday (28/09)", 2),
]

total_hours = sum(hours for _, hours in lessons)
total_amount = total_hours * rate_per_hour

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Invoice', ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

pdf = PDF()
pdf.add_page()

# Invoice header
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, f"Invoice Number: {invoice_number}", ln=True)
pdf.cell(0, 10, f"Invoice Date: {invoice_date}", ln=True)
pdf.cell(0, 10, f"Invoiced To: {parent_name}", ln=True)
pdf.cell(0, 10, f"Student: {student_name}", ln=True)
pdf.cell(0, 10, f"Subject: {subject}", ln=True)
pdf.ln(10)

# Lessons table header
pdf.set_font('Arial', 'B', 12)
pdf.cell(60, 10, 'Date', 1)
pdf.cell(40, 10, 'Hours', 1)
pdf.cell(40, 10, 'Rate (R)', 1)
pdf.cell(40, 10, 'Amount (R)', 1, ln=True)

pdf.set_font('Arial', '', 12)
for date, hours in lessons:
    amount = hours * rate_per_hour
    pdf.cell(60, 10, date, 1)
    pdf.cell(40, 10, str(hours), 1)
    pdf.cell(40, 10, f"{rate_per_hour}", 1)
    pdf.cell(40, 10, f"{amount}", 1, ln=True)

# Total
pdf.set_font('Arial', 'B', 12)
pdf.cell(140, 10, 'Total', 1)
pdf.cell(40, 10, f"{total_amount}", 1, ln=True)

# Save PDF
output_path = f"invoices/Invoice_{invoice_number}.pdf"
pdf.output(output_path)
print(f"Invoice generated: {output_path}")
