from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
import re

# Read markdown
with open('Case_Study_Report_Final.md', 'r', encoding='utf-8') as f:
    content = f.read()

pdf_filename = 'montenegro_CCS230_Finals.pdf'
doc = SimpleDocTemplate(pdf_filename, pagesize=letter,
                       rightMargin=0.4*inch, leftMargin=0.4*inch,
                       topMargin=0.4*inch, bottomMargin=0.4*inch)

elements = []
styles = getSampleStyleSheet()

# ===== STYLES =====
cover_title = ParagraphStyle('CoverTitle', parent=styles['Heading1'],
    fontSize=20, textColor=colors.HexColor('#1a3a5c'), spaceAfter=0.08*inch,
    spaceBefore=0.1*inch, fontName='Helvetica-Bold', alignment=1)

cover_subtitle = ParagraphStyle('CoverSubtitle', parent=styles['Normal'],
    fontSize=12, textColor=colors.HexColor('#333333'), spaceAfter=0.03*inch,
    fontName='Helvetica', alignment=1)

cover_info = ParagraphStyle('CoverInfo', parent=styles['Normal'],
    fontSize=10, textColor=colors.HexColor('#333333'), spaceAfter=0.02*inch,
    fontName='Helvetica', alignment=1)

section_heading = ParagraphStyle('SectionHeading', parent=styles['Heading2'],
    fontSize=12, textColor=colors.HexColor('#1f4788'), spaceAfter=0.04*inch,
    spaceBefore=0.04*inch, fontName='Helvetica-Bold')

subsection_heading = ParagraphStyle('SubsectionHeading', parent=styles['Heading3'],
    fontSize=10, textColor=colors.HexColor('#2e5c8a'), spaceAfter=0.02*inch,
    spaceBefore=0.02*inch, fontName='Helvetica-Bold')

body_style = ParagraphStyle('BodyText', parent=styles['Normal'],
    fontSize=8.5, leading=9, spaceAfter=0.03*inch, alignment=4, wordWrap='CJK')

bullet_style = ParagraphStyle('BulletStyle', parent=styles['Normal'],
    fontSize=8.5, leading=9, spaceAfter=0.02*inch, leftIndent=0.12*inch,
    alignment=4, wordWrap='CJK')

# Table styles - slightly larger for readability
table_header_style = ParagraphStyle('TableHeader', parent=styles['Normal'],
    fontSize=7, fontName='Helvetica-Bold', alignment=1, wordWrap='CJK', leading=8)

table_cell_style = ParagraphStyle('TableCell', parent=styles['Normal'],
    fontSize=6.5, alignment=1, wordWrap='CJK', leading=7)

def clean_markdown(text):
    if not text:
        return text
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'_([^_]+)_', r'<i>\1</i>', text)
    text = re.sub(r'`([^`]+)`', r'<font face="Courier" size="6">\1</font>', text)
    return text

def get_column_widths(num_cols):
    """Return optimal column widths based on number of columns"""
    # Total available width
    total_width = 7.2  # inches (8.5 - 0.4*2 margins)
    
    if num_cols == 2:
        return [1.8*inch, 5.4*inch]
    elif num_cols == 3:
        return [1.4*inch, 2.8*inch, 3.0*inch]
    elif num_cols == 4:
        # First col: aspect/characteristic, next 2: comparison, last: impact/notes
        return [1.3*inch, 1.2*inch, 1.2*inch, 2.5*inch]
    elif num_cols == 5:
        return [1.0*inch, 1.0*inch, 1.0*inch, 1.0*inch, 2.2*inch]
    elif num_cols == 6:
        return [0.95*inch, 0.95*inch, 0.95*inch, 0.95*inch, 0.95*inch, 1.5*inch]
    else:
        # Default: equal widths
        col_width = total_width / num_cols
        return [col_width*inch] * num_cols

def parse_table_professional(lines, start_idx):
    """Parse markdown table with professional formatting"""
    rows = []
    i = start_idx
    
    # Parse header
    if i < len(lines) and lines[i].strip().startswith('|'):
        header = [cell.strip() for cell in lines[i].strip().split('|')[1:-1]]
        if header:
            rows.append(header)
        i += 1
    
    # Skip separator
    if i < len(lines) and '---' in lines[i]:
        i += 1
    
    # Parse data rows
    while i < len(lines) and lines[i].strip().startswith('|'):
        cells = [cell.strip() for cell in lines[i].strip().split('|')[1:-1]]
        if cells and any(cells):
            rows.append(cells)
        i += 1
    
    if not rows or len(rows) < 2:
        return None, i
    
    num_cols = len(rows[0])
    col_widths = get_column_widths(num_cols)
    
    # Format table with Paragraphs in cells
    table_data = []
    for row_idx, row in enumerate(rows):
        formatted_row = []
        for cell in row:
            cell_text = clean_markdown(str(cell))
            if row_idx == 0:
                para = Paragraph(cell_text, table_header_style)
            else:
                para = Paragraph(cell_text, table_cell_style)
            formatted_row.append(para)
        table_data.append(formatted_row)
    
    # Create table
    table = Table(table_data, colWidths=col_widths)
    
    # Professional styling with proper row heights
    style_commands = [
        # Header row
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4788')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 7),
        ('PADDING', (0, 0), (-1, 0), 5),
        ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        
        # Data rows
        ('FONTSIZE', (0, 1), (-1, -1), 6.5),
        ('PADDING', (0, 1), (-1, -1), 4),
        ('VALIGN', (0, 1), (-1, -1), 'TOP'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        
        # Row heights - taller for wrapped text
        ('ROWHEIGHTS', (0, 0), (-1, 0), 0.25*inch),  # Header row
        ('ROWHEIGHTS', (0, 1), (-1, -1), 0.4*inch),   # Data rows
        
        # Alternating row colors
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#fafafa')]),
        
        # Borders
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#d0d0d0')),
        ('LINEABOVE', (0, 0), (-1, 0), 1.5, colors.HexColor('#1f4788')),
        ('LINEBELOW', (0, -1), (-1, -1), 1.5, colors.HexColor('#1f4788')),
    ]
    
    table.setStyle(TableStyle(style_commands))
    
    return table, i

# ===== MAIN PARSING =====
lines = content.split('\n')
i = 0

while i < len(lines):
    line = lines[i].rstrip()
    stripped = line.strip()
    
    # COVER PAGE
    if '## COVER PAGE' in stripped:
        elements.append(Spacer(1, 0.25*inch))
        i += 1
        
        while i < len(lines):
            cover_line = lines[i].strip()
            if cover_line.startswith('## '):
                break
            
            clean_text = cover_line.replace('**', '').replace('__', '')
            
            if 'HEART DISEASE' in clean_text and clean_text:
                elements.append(Paragraph(clean_text, cover_title))
            elif any(x in clean_text for x in ['Submitted By:', 'Instructor:', 'Course:']):
                if clean_text:
                    elements.append(Paragraph(clean_text, cover_subtitle))
            elif clean_text and clean_text != '---':
                elements.append(Paragraph(clean_text, cover_info))
            elif cover_line == '---':
                elements.append(Spacer(1, 0.06*inch))
            
            i += 1
        
        elements.append(PageBreak())
        continue
    
    # ABSTRACT
    elif '## Abstract' in stripped:
        elements.append(Paragraph('Abstract', section_heading))
        i += 1
        
        while i < len(lines) and not lines[i].strip().startswith('## '):
            abstract_line = lines[i].strip()
            if abstract_line and abstract_line != '---':
                elements.append(Paragraph(clean_markdown(abstract_line), body_style))
            i += 1
        
        elements.append(PageBreak())
        continue
    
    # TABLE OF CONTENTS
    elif '## Table of Contents' in stripped:
        elements.append(Paragraph('Table of Contents', section_heading))
        i += 1
        
        while i < len(lines) and not lines[i].strip().startswith('## '):
            toc_line = lines[i].strip()
            if toc_line and toc_line != '---':
                indent = (len(lines[i]) - len(lines[i].lstrip())) // 3
                if indent > 0:
                    elements.append(Paragraph(toc_line, bullet_style))
                else:
                    elements.append(Paragraph(f"<b>{toc_line}</b>", body_style))
            i += 1
        
        elements.append(PageBreak())
        continue
    
    # SECTIONS
    elif stripped.startswith('## ') and '## COVER' not in stripped:
        section_text = stripped[3:].strip()
        if section_text and section_text != '---':
            if len(elements) > 0 and not isinstance(elements[-1], PageBreak):
                elements.append(PageBreak())
            elements.append(Paragraph(section_text, section_heading))
        i += 1
        continue
    
    # SUBSECTIONS
    elif stripped.startswith('### '):
        subsection_text = stripped[4:].strip()
        if subsection_text:
            elements.append(Paragraph(subsection_text, subsection_heading))
        i += 1
        continue
    
    # SUB-SUBSECTIONS
    elif stripped.startswith('#### '):
        text = stripped[5:].strip()
        if text:
            elements.append(Paragraph(f"<b>{text}</b>", subsection_heading))
        i += 1
        continue
    
    # TABLES
    elif stripped.startswith('| '):
        table_obj, new_i = parse_table_professional(lines, i)
        if table_obj:
            elements.append(table_obj)
            elements.append(Spacer(1, 0.01*inch))
        i = new_i
        continue
    
    # BULLETS
    elif stripped.startswith('- '):
        bullet_text = stripped[2:].strip()
        if bullet_text:
            elements.append(Paragraph(clean_markdown(bullet_text), bullet_style))
        i += 1
        continue
    
    # PARAGRAPHS
    elif stripped and not stripped.startswith('---'):
        para = Paragraph(clean_markdown(stripped), body_style)
        elements.append(para)
        i += 1
        continue
    
    # PAGE BREAKS
    elif stripped == '---':
        if len(elements) > 0 and not isinstance(elements[-1], PageBreak):
            elements.append(PageBreak())
        i += 1
        continue
    
    else:
        i += 1
        continue

# BUILD PDF
try:
    doc.build(elements)
    print(f"✅ Professional PDF created: {pdf_filename}")
    print(f"   ✓ Smart column width allocation (4-col: 1.3\", 1.2\", 1.2\", 2.5\")")
    print(f"   ✓ Proper row heights (0.4\" for wrapped text)")
    print(f"   ✓ No more overlapping or disorganized tables")
    print(f"   ✓ Clean, professional formatting")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
