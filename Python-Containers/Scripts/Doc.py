from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


def create_structured_pdf(output_file):
    # Define the output PDF file
    doc = SimpleDocTemplate(output_file, pagesize=letter)

    # Create a list to hold the content
    content = []

    # Add the header
    header_text = "Economics - BR"
    header_style = ParagraphStyle('HeaderStyle', parent=getSampleStyleSheet()['Normal'], fontName='Helvetica-Bold',fontSize=20)
    content.append(Paragraph(header_text, header_style))
    
    # Add a space between paragraphs
    content.append(Spacer(1, 12))
    
    # Add the main content
    main_text = "This project aims to collect and analyse data from CVM, like DRE and other reports"
    main_style = ParagraphStyle('TitleStyle', parent=getSampleStyleSheet()['Normal'], fontName='Helvetica',fontSize=14)
    content.append(Paragraph(main_text, main_style))
    
    # Add a space between paragraphs
    content.append(Spacer(1, 12))
    
    # Add the describing content
    _main_text = "In order to achieve a secure and modern enviroment, it was used a Stack like described bellow.\nFor Iac it was performed a terraform script"
    _main_style = ParagraphStyle('MainStyle', parent=getSampleStyleSheet()['Normal'], fontName='Helvetica')
    content.append(Paragraph(_main_text, _main_style))
    
    # Add a space between paragraphs
    content.append(Spacer(1, 12))
    
    # Add the footer
    footer_text = "Footer: This is the footer content"
    footer_style = ParagraphStyle('FooterStyle', parent=getSampleStyleSheet()['Normal'], fontName='Helvetica-Bold')
    content.append(Paragraph(footer_text, footer_style))

    # Build the PDF file
    doc.build(content)

# Example usage
if __name__ == "__main__":
    output_file = r"C:\Users\SALA443\Desktop\Nova pasta (2)\curriculo.pdf"  # Replace with the desired output file name
    create_structured_pdf(output_file)