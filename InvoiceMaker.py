"""
Professional Invoice Generator for Yolymatics Tutorials - TTI Group Focused
Created for generating high-quality PDF invoices with improved formatting

Requirements:
- pip install reportlab

Usage:
    generator = InvoiceGenerator()
    generator.generate_invoice(student_name, course, lessons, rate_per_lesson)
"""

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from datetime import datetime
import os


class InvoiceGenerator:
    def __init__(self):
        """Initialize the invoice generator with company information"""
        self.company_info = {
            'name': 'YOLYMATICS TUTORIALS (PTY) LTD',
            'registration_number': '2024/838115/07',
            'address': '11 Salford Road, Bellville, WC 7530',
            'website': 'www.yolymaticstutorials.com',
            'contact': '084 759 7313',
            'email': 'admin@yolymaticstutorials.com'
        }
        
        # TTI Group billing information (default client)
        self.default_client_info = {
            'name': 'TTI Bursary Management',
            'address_line1': 'Monte Circle, Block A, 1st Floor 178',
            'address_line2': 'Montecasino Blvd, Magaliessig',
            'city': 'Sandton',
            'country': 'South Africa',
            'postal_code': '2191',
            'email': 'thabiso@ttibursaries.co.za'
        }
        
        # Complete banking details
        self.banking_details = {
            'bank_name': 'Capitec Business',
            'account_name': 'YOLYMATICS TUTORIALS (PTY)LTD',
            'account_number': '1052964044',
            'branch': 'Relationship Suite',
            'branch_code': '470010',
            'account_type': 'Capitec Business Account'
        }
        
        self.vat_rate = 0.0  # No VAT for this invoice
        
    def generate_invoice(self, student_name, courses, lessons_per_course, rate_per_lesson, 
                        invoice_number=None, invoice_date=None, 
                        client_info=None, use_tti_default=True, output_dir="invoices"):
        """
        Generate a professional PDF invoice with clear TTI Group billing
        
        Args:
            student_name (str): Name of the student
            course (str): Course/subject name
            lessons (int): Number of lessons
            rate_per_lesson (float): Rate per lesson in Rands
            invoice_number (str, optional): Custom invoice number
            invoice_date (str, optional): Custom invoice date (YYYY-MM-DD)
            client_info (dict, optional): Alternative client information
            use_tti_default (bool): Use TTI Group as default client
            output_dir (str): Directory to save invoices
            
        Returns:
            dict: Invoice details including filename and totals
        """
        
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Generate invoice number and date if not provided
        if invoice_number is None:
            invoice_number = f"INV-{datetime.now().strftime('%Y%m%d')}-{self._get_next_invoice_number()}"
        
        if invoice_date is None:
            invoice_date = datetime.now().strftime('%Y-%m-%d')
        
        # Select client information (TTI Group by default)
        bill_to = (
            self.default_client_info.copy()
            if (use_tti_default and client_info is None)
            else (client_info or self.default_client_info)
        )
        
        # Calculate totals for multiple courses
        subtotal = sum(lessons_per_course) * rate_per_lesson
        vat_amount = round(subtotal * self.vat_rate, 2)
        total_amount = round(subtotal + vat_amount, 2)

        # Create filename
        safe_student_name = student_name.replace(" ", "_").replace("/", "_")
        filename = os.path.join(output_dir, f"Invoice_{invoice_number}_{safe_student_name}.pdf")

        # Create PDF document
        doc = SimpleDocTemplate(filename, pagesize=A4, rightMargin=72, leftMargin=72, 
                              topMargin=72, bottomMargin=18)

        # Build the invoice content
        story = self._build_invoice_content_multi(
            invoice_number, invoice_date, student_name, courses, 
            lessons_per_course, rate_per_lesson, subtotal, vat_amount, total_amount, bill_to
        )

        # Generate PDF
        doc.build(story)

        return {
            'filename': filename,
            'invoice_number': invoice_number,
            'invoice_date': invoice_date,
            'student_name': student_name,
            'courses': courses,
            'lessons_per_course': lessons_per_course,
            'rate_per_lesson': rate_per_lesson,
            'subtotal': subtotal,
            'vat_amount': vat_amount,
            'total_amount': total_amount,
            'bill_to': bill_to
        }
    def _build_invoice_content_multi(self, invoice_number, invoice_date, student_name, courses,
                              lessons_per_course, rate_per_lesson, subtotal, vat_amount, total_amount, bill_to):
        """Build the PDF content structure for multiple courses with improved formatting"""
        
        story = []
        styles = getSampleStyleSheet()
        
        # Define custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=28,
            spaceAfter=20,
            alignment=TA_CENTER,
            textColor=colors.darkblue,
            fontName='Helvetica-Bold'
        )
        
        header_style = ParagraphStyle(
            'HeaderStyle',
            parent=styles['Normal'],
            fontSize=12,
            fontName='Helvetica-Bold',
            textColor=colors.darkblue,
            spaceAfter=8,
            spaceBefore=8
        )
        
        # Updated address styles with better spacing
        address_style = ParagraphStyle(
            'AddressStyle',
            parent=styles['Normal'],
            fontSize=10,
            spaceAfter=4,
            alignment=TA_LEFT,
            leftIndent=8,  # Added left indent for better spacing
            rightIndent=8  # Added right indent for better spacing
        )
        
        footer_style = ParagraphStyle(
            'FooterStyle',
            parent=styles['Normal'],
            fontSize=10,
            alignment=TA_LEFT,
            spaceAfter=6
        )
        
        # Main invoice title
        story.append(Paragraph("INVOICE", title_style))
        story.append(Spacer(1, 20))
        
        # FROM and BILL TO header sections with improved formatting
        from_header = Paragraph("<b>FROM:</b>", header_style)
        bill_to_header = Paragraph("<b>BILL TO:</b>", header_style)
        
        # FROM section (Your company) - better formatted
        from_lines = [
            f"<b>{self.company_info['name']}</b>",
            f"Reg No: {self.company_info['registration_number']}",
            self.company_info['address'],
            f"Tel: {self.company_info['contact']}",
            f"Email: {self.company_info['email']}",
            self.company_info['website']
        ]
        from_paragraph = Paragraph("<br/>".join(from_lines), address_style)
        
        # BILL TO section - better formatted with proper spacing
        bill_lines = [
            f"<b>{bill_to['name']}</b>",
            bill_to.get('address_line1', ''),
            bill_to.get('address_line2', ''),
            bill_to.get('city', ''),
            f"Postal Code: {bill_to.get('postal_code', '')}",
            f"VAT No: {bill_to.get('vat_no', '')}"
        ]
        # Remove empty lines
        bill_lines = [line for line in bill_lines if line.strip() and line.strip() != ',']
        bill_paragraph = Paragraph("<br/>".join(bill_lines), address_style)
        
        # Create two-column table for FROM and BILL TO with improved spacing
        header_table = Table([
            [from_header, bill_to_header],
            [from_paragraph, bill_paragraph]
        ], colWidths=[3.25*inch, 3.25*inch])
        
        header_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),  # Increased left padding
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),  # Increased right padding
            ('BOTTOMPADDING', (0, 0), (-1, -1), 15),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            # Enhanced border styling for BILL TO section
            ('BOX', (1, 0), (1, -1), 2, colors.darkblue),
            ('BACKGROUND', (1, 0), (1, 0), colors.lightblue),
            # Add some spacing around the content
            ('LEFTPADDING', (1, 1), (1, 1), 15),
            ('RIGHTPADDING', (1, 1), (1, 1), 15),
            ('TOPPADDING', (1, 1), (1, 1), 12),
            ('BOTTOMPADDING', (1, 1), (1, 1), 12),
        ]))
        
        story.append(header_table)
        story.append(Spacer(1, 30))
        
        # Invoice details section
        story.append(Paragraph("INVOICE DETAILS", header_style))
        
        invoice_details = [
            ['Invoice Number:', invoice_number],
            ['Invoice Date:', invoice_date],
            ['Student Name:', student_name],
            ['Courses:', ', '.join(courses)]
        ]
        
        invoice_table = Table(invoice_details, colWidths=[2*inch, 4*inch])
        invoice_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.lightgrey),
            ('BACKGROUND', (0, 0), (-1, -1), colors.lightyellow),
        ]))
        
        story.append(invoice_table)
        story.append(Spacer(1, 25))
        
        # Service details table for multiple courses
        story.append(Paragraph("SERVICE DETAILS", header_style))
        
        service_data = [
            ['Description', 'Quantity (hours)', 'Rate (ZAR/hour)', 'Amount (ZAR)']
        ]
        
        for course, hours in zip(courses, lessons_per_course):
            service_data.append([
                f'{course}',
                str(hours),
                f'R {rate_per_lesson:,.2f}',
                f'R {hours * rate_per_lesson:,.2f}'
            ])
        
        # Make Description column narrower and other columns wider and more equal
        service_table = Table(service_data, colWidths=[2*inch, 2*inch, 1.5*inch, 1.5*inch])
        service_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 12),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ALIGN', (0, 1), (0, -1), 'LEFT'),
            ('ALIGN', (1, 1), (-1, -1), 'RIGHT'),
        ]))
        
        story.append(service_table)
        story.append(Spacer(1, 20))
        
        # Totals table (only show if VAT > 0, otherwise just show total)
        if vat_amount > 0:
            totals_data = [
                ['Subtotal:', f'R {subtotal:,.2f}'],
                ['VAT (15%):', f'R {vat_amount:,.2f}'],
                ['TOTAL AMOUNT:', f'R {total_amount:,.2f}']
            ]
        else:
            totals_data = [
                ['TOTAL AMOUNT:', f'R {total_amount:,.2f}']
            ]
        
        totals_table = Table(totals_data, colWidths=[4.25*inch, 1.75*inch])
        totals_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
            ('FONTNAME', (0, 0), (-1, -2), 'Helvetica'),
            ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('FONTSIZE', (0, -1), (-1, -1), 14),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ('LINEABOVE', (0, -1), (-1, -1), 2, colors.black),
            ('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey),
        ]))
        
        story.append(totals_table)
        story.append(Spacer(1, 30))
        
        # Payment terms
        story.append(Paragraph("PAYMENT TERMS", header_style))
        payment_terms_text = """
        • Payment is due within 5 days of invoice date<br/>
        • Please reference the invoice number when making payment<br/>
        • Late payments may incur additional charges<br/>
        """
        story.append(Paragraph(payment_terms_text, footer_style))
        story.append(Spacer(1, 20))
        
        # Force page break before banking details
        story.append(PageBreak())
        
        # Banking details in a well-formatted table
        story.append(Paragraph("BANKING DETAILS", header_style))
        
        banking_data = [
            ['Bank Name:', self.banking_details['bank_name']],
            ['Account Name:', self.banking_details['account_name']],
            ['Account Number:', self.banking_details['account_number']],
            ['Branch:', self.banking_details['branch']],
            ['Branch Code:', self.banking_details['branch_code']],
            ['Account Type:', self.banking_details['account_type']]
        ]
        
        banking_table = Table(banking_data, colWidths=[2.5*inch, 3.5*inch])
        banking_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('LEFTPADDING', (0, 0), (-1, -1), 15),
            ('RIGHTPADDING', (0, 0), (-1, -1), 15),
            ('GRID', (0, 0), (-1, -1), 1.5, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, -1), colors.aliceblue),
            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.aliceblue, colors.white]),
        ]))
        
        story.append(banking_table)
        story.append(Spacer(1, 20))
        
        # Thank you message
        thank_you_text = "<b>Thank you for choosing Yolymatics Tutorials for your educational needs.</b>"
        story.append(Paragraph(thank_you_text, footer_style))
        story.append(Spacer(1, 30))
        
        # Bible verse at the bottom
        bible_verse_style = ParagraphStyle(
            'BibleVerseStyle',
            parent=styles['Normal'],
            fontSize=10,
            alignment=TA_CENTER,
            spaceAfter=6,
            fontName='Helvetica-Oblique',
            textColor=colors.darkblue
        )
        bible_verse_text = '<i>"For I know the plans I have for you," declares the Lord, "plans to prosper you and not to harm you, to give you hope and a future." - Jeremiah 29:11</i>'
        story.append(Paragraph(bible_verse_text, bible_verse_style))
        
        return story
    
    def _get_next_invoice_number(self):
        """Generate a sequential invoice number"""
        return f"{datetime.now().strftime('%H%M%S')}"
    
    def _build_invoice_content(self, invoice_number, invoice_date, student_name, course,
                              lessons, rate_per_lesson, subtotal, vat_amount, total_amount, bill_to):
        """Build the PDF content structure with improved formatting"""
        
        story = []
        styles = getSampleStyleSheet()
        
        # Define custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=28,
            spaceAfter=20,
            alignment=TA_CENTER,
            textColor=colors.darkblue,
            fontName='Helvetica-Bold'
        )
        
        header_style = ParagraphStyle(
            'HeaderStyle',
            parent=styles['Normal'],
            fontSize=12,
            fontName='Helvetica-Bold',
            textColor=colors.darkblue,
            spaceAfter=8,
            spaceBefore=8
        )
        
        # Updated address styles with better spacing
        address_style = ParagraphStyle(
            'AddressStyle',
            parent=styles['Normal'],
            fontSize=10,
            spaceAfter=4,
            alignment=TA_LEFT,
            leftIndent=8,  # Added left indent for better spacing
            rightIndent=8  # Added right indent for better spacing
        )
        
        footer_style = ParagraphStyle(
            'FooterStyle',
            parent=styles['Normal'],
            fontSize=10,
            alignment=TA_LEFT,
            spaceAfter=6
        )
        
        # Main invoice title
        story.append(Paragraph("INVOICE", title_style))
        story.append(Spacer(1, 20))
        
        # FROM and BILL TO header sections with improved formatting
        from_header = Paragraph("<b>FROM:</b>", header_style)
        bill_to_header = Paragraph("<b>BILL TO:</b>", header_style)
        
        # FROM section (Your company) - better formatted
        from_lines = [
            f"<b>{self.company_info['name']}</b>",
            f"Reg No: {self.company_info['registration_number']}",
            self.company_info['address'],
            f"Tel: {self.company_info['contact']}",
            f"Email: {self.company_info['email']}",
            self.company_info['website']
        ]
        from_paragraph = Paragraph("<br/>".join(from_lines), address_style)
        
        # BILL TO section (TTI Group) - better formatted with proper spacing
        bill_lines = [
            f"<b>{bill_to['name']}</b>",
            bill_to.get('address_line1', ''),
            bill_to.get('address_line2', ''),
            f"{bill_to.get('city', '')}, {bill_to.get('country', '')}",
            f"Postal Code: {bill_to.get('postal_code', '')}",
            f"Email: {bill_to.get('email', '')}"
        ]
        bill_paragraph = Paragraph("<br/>".join(bill_lines), address_style)
        
        # Create two-column table for FROM and BILL TO with improved spacing
        header_table = Table([
            [from_header, bill_to_header],
            [from_paragraph, bill_paragraph]
        ], colWidths=[3.25*inch, 3.25*inch])
        
        header_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),  # Increased left padding
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),  # Increased right padding
            ('BOTTOMPADDING', (0, 0), (-1, -1), 15),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            # Enhanced border styling for BILL TO section
            ('BOX', (1, 0), (1, -1), 2, colors.darkblue),
            ('BACKGROUND', (1, 0), (1, 0), colors.lightblue),
            # Add some spacing around the content
            ('LEFTPADDING', (1, 1), (1, 1), 15),
            ('RIGHTPADDING', (1, 1), (1, 1), 15),
            ('TOPPADDING', (1, 1), (1, 1), 12),
            ('BOTTOMPADDING', (1, 1), (1, 1), 12),
        ]))
        
        story.append(header_table)
        story.append(Spacer(1, 30))
        
        # Invoice details section
        story.append(Paragraph("INVOICE DETAILS", header_style))
        
        invoice_details = [
            ['Invoice Number:', invoice_number],
            ['Invoice Date:', invoice_date],
            ['Student Name:', student_name],
            ['Course:', course]
        ]
        
        invoice_table = Table(invoice_details, colWidths=[2*inch, 4*inch])
        invoice_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.lightgrey),
            ('BACKGROUND', (0, 0), (-1, -1), colors.lightyellow),
        ]))
        
        story.append(invoice_table)
        story.append(Spacer(1, 25))
        
        # Service details table
        story.append(Paragraph("SERVICE DETAILS", header_style))
        
        service_data = [
            ['Description', 'Quantity', 'Rate (ZAR)', 'Amount (ZAR)'],
            [f'{course} Tutoring Sessions', 
             str(lessons), 
             f'R {rate_per_lesson:,.2f}', 
             f'R {subtotal:,.2f}']
        ]
        
        service_table = Table(service_data, colWidths=[3*inch, 1*inch, 1.25*inch, 1.25*inch])
        service_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 12),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ALIGN', (0, 1), (0, 1), 'LEFT'),
            ('ALIGN', (1, 1), (-1, -1), 'RIGHT'),
        ]))
        
        story.append(service_table)
        story.append(Spacer(1, 20))
        
        # Totals table
        totals_data = [
            ['Subtotal:', f'R {subtotal:,.2f}'],
            ['VAT (15%):', f'R {vat_amount:,.2f}'],
            ['TOTAL AMOUNT:', f'R {total_amount:,.2f}']
        ]
        
        totals_table = Table(totals_data, colWidths=[4.25*inch, 1.75*inch])
        totals_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
            ('FONTNAME', (0, 0), (-1, 1), 'Helvetica'),
            ('FONTNAME', (0, 2), (-1, 2), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('FONTSIZE', (0, 2), (-1, 2), 14),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ('LINEABOVE', (0, 2), (-1, 2), 2, colors.black),
            ('BACKGROUND', (0, 2), (-1, 2), colors.lightgrey),
        ]))
        
        story.append(totals_table)
        story.append(Spacer(1, 30))
        
        # Payment terms
        story.append(Paragraph("PAYMENT TERMS", header_style))
        payment_terms_text = """
        • Payment is due within 5 days of invoice date<br/>
        • Please reference the invoice number when making payment<br/>
        • Late payments may incur additional charges<br/>
        """
        story.append(Paragraph(payment_terms_text, footer_style))
        story.append(Spacer(1, 20))
        
        # Banking details in a well-formatted table
        story.append(Paragraph("BANKING DETAILS", header_style))
        
        banking_data = [
            ['Bank Name:', self.banking_details['bank_name']],
            ['Account Name:', self.banking_details['account_name']],
            ['Account Number:', self.banking_details['account_number']],
            ['Branch:', self.banking_details['branch']],
            ['Branch Code:', self.banking_details['branch_code']],
            ['Account Type:', self.banking_details['account_type']]
        ]
        
        banking_table = Table(banking_data, colWidths=[2.5*inch, 3.5*inch])
        banking_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('LEFTPADDING', (0, 0), (-1, -1), 15),
            ('RIGHTPADDING', (0, 0), (-1, -1), 15),
            ('GRID', (0, 0), (-1, -1), 1.5, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, -1), colors.aliceblue),
            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.aliceblue, colors.white]),
        ]))
        
        story.append(banking_table)
        story.append(Spacer(1, 20))
        
        # Thank you message
        thank_you_text = "<b>Thank you for choosing Yolymatics Tutorials for your educational needs.</b>"
        story.append(Paragraph(thank_you_text, footer_style))
        
        return story


# Example usage
if __name__ == "__main__":
    generator = InvoiceGenerator()

    # Rosaria Grasso billing info
    rosaria_grasso_info = {
        'name': 'Rosaria Grasso',
        'address_line1': '',
        'address_line2': '',
        'city': '',
        'country': '',
        'postal_code': '7441',
        'email': ''
    }

    # Lessons for Bella Grasso
    lessons = [
        ("Monday (08/09)", 2),
        ("Wednesday (10/09)", 2),
        ("Friday (12/09)", 2),
        ("Saturday (13/09)", 2),
        ("Sunday (21/09)", 2),
        ("Sunday (28/09)", 2),
    ]
    total_hours = sum(hours for _, hours in lessons)

    result = generator.generate_invoice(
        student_name="Bella Grasso",
        courses=["Discrete Mathematics"],
        lessons_per_course=[total_hours],
        rate_per_lesson=350.00,
        client_info=rosaria_grasso_info,
        use_tti_default=False
    )

    print(f"Invoice generated: {result['filename']}")
    print(f"Total Amount: R{result['total_amount']:,.2f}")
    print(f"Billed to: {result['bill_to']['name']}")
