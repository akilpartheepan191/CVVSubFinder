import openpyxl
from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def convert_excel_to_pdf(excel_file, pdf_file, title,size):
    # Load the Excel file
    workbook = openpyxl.load_workbook(excel_file)
    sheet = workbook.active

    # Convert the sheet data to a list of lists
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(list(row))

    # Create a PDF document with landscape orientation
    doc = SimpleDocTemplate(pdf_file, pagesize=landscape(letter))
    elements = []

    # Add title to the document
    title_text = title
    styles = getSampleStyleSheet()
    title = Paragraph(title_text, styles['Heading1'])
    elements.append(title)

    # Create a table and add data
    table = Table(data)

    # Define table style
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 14),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), size),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    # Apply table style
    table.setStyle(style)

    # Add table to the document
    elements.append(table)

    # Define the footer
    footer_text = "Created by the members of the computing club"

    # Build the PDF document
    doc.build(elements, onFirstPage=lambda canvas, doc: canvas.drawCentredString(300, 30, footer_text), onLaterPages=lambda canvas, doc: canvas.drawCentredString(300, 30, footer_text))

