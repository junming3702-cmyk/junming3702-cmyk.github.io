"""Extract unmodified figures and selected pages from the owner-supplied April 2024 report.
Usage: python scripts/extract_qgis_evidence.py /path/to/source-report.pdf
"""
import sys
from io import BytesIO
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
root=Path(__file__).resolve().parents[1]
reader=PdfReader(sys.argv[1])
figures={10:'qgis-walking-circles.jpg',12:'qgis-diversity-accessibility.jpg'}
for idx,name in figures.items():
    (root/'assets/evidence'/name).write_bytes(reader.pages[idx].images[0].data)
buf=BytesIO()
style=ParagraphStyle('body',fontName='Times-Roman',fontSize=12,leading=18,textColor=colors.HexColor('#20302f'),spaceAfter=16)
title=ParagraphStyle('title',parent=style,fontName='Times-Bold',fontSize=24,leading=29,spaceAfter=24)
parts=[Paragraph('15-minute Community Living Circle<br/>Selected report evidence',title),Paragraph('Hong Kong | Collaborative coursework | April 2024',style),Paragraph('<b>Original title:</b> Construction of 15-minute Community Living Circle (15min-CLC) Diagnostic System: Based on the Demographic Characteristics of Hong Kong',style),Paragraph('<b>Authors:</b> Chen Xinying, Qu Shiyan, Xu Junyi and Zhang Junming.<br/>CA6241, Group 9, Department of Architecture and Civil Engineering, City University of Hong Kong.',style),Paragraph('This portfolio excerpt reproduces selected original pages without changing their figures, findings or contribution statements. It is a historical coursework report, not a current assessment of Hong Kong services or a peer-reviewed publication.',style),Paragraph('<b>Included original pages</b><br/>Cover; walking-circle methodology and Figure 3 (printed page 10); Figure 5 and analysis (page 12); Figure 6 and per-capita results (page 13); limitations (page 16); individual contributions (page 18). Original page numbers are retained.',style),Paragraph('<b>Junming Zhang\'s role</b><br/>Conclusions, implications and limitations; corresponding presentation and report sections; interim-report presentation integration. Maps and spatial-analysis results are group outputs.',style),Paragraph('<b>Portfolio:</b> <a href="https://junming3702-cmyk.github.io/qgis.html" color="#416656">junming3702-cmyk.github.io/qgis.html</a><br/>Excerpt prepared: 28 November 2026',style)]
SimpleDocTemplate(buf,pagesize=A4,leftMargin=54,rightMargin=54,topMargin=55,bottomMargin=55).build(parts)
writer=PdfWriter()
writer.append(PdfReader(buf))
for idx in (0,10,12,13,16,18): writer.add_page(reader.pages[idx])
writer.add_metadata({'/Title':'15-minute Community Living Circle - Selected Report Evidence','/Author':'Chen Xinying; Qu Shiyan; Xu Junyi; Zhang Junming'})
output=root/'assets/docs/Community_Living_Circle_Report_Excerpts.pdf'
writer.write(output)
print(output)
print('Pages:',len(writer.pages))
