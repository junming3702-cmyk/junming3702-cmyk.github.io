"""Rebuild the portfolio's public CV with ReportLab. No private source files required."""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, HRFlowable

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/docs/Junming_Zhang_Public_CV.pdf'
INK = colors.HexColor('#20302f')
GREEN = colors.HexColor('#416656')
styles = {
    'name': ParagraphStyle('name', fontName='Times-Bold', fontSize=29, leading=33, textColor=INK, spaceAfter=7),
    'tag': ParagraphStyle('tag', fontName='Times-Roman', fontSize=12, leading=16, textColor=GREEN, spaceAfter=5),
    'section': ParagraphStyle('section', fontName='Times-Bold', fontSize=13, leading=16, textColor=GREEN, spaceBefore=13, spaceAfter=7, keepWithNext=True),
    'title': ParagraphStyle('title', fontName='Times-Bold', fontSize=11.5, leading=14, textColor=INK, spaceBefore=6, spaceAfter=3, keepWithNext=True),
    'body': ParagraphStyle('body', fontName='Times-Roman', fontSize=10.5, leading=14, textColor=INK, spaceAfter=5),
    'meta': ParagraphStyle('meta', fontName='Times-Italic', fontSize=10, leading=13, textColor=GREEN, spaceAfter=5),
}
story=[]
def p(text, style='body'): story.append(Paragraph(text,styles[style]))
def section(text): p(text,'section')
def link(url,label): return f'<a href="{url}" color="#416656">{label}</a>'

def footer(canvas,doc):
    canvas.setStrokeColor(colors.HexColor('#d5ded7'))
    canvas.line(45,39,A4[0]-45,39)
    canvas.setFont('Times-Roman',9)
    canvas.setFillColor(GREEN)
    canvas.drawString(45,25,'Junming Zhang | Public CV | November 2026')
    canvas.drawRightString(A4[0]-45,25,str(doc.page))

p('Junming Zhang <font size="17">(Tom)</font>','name')
p('Construction management | Digital methods | Applied AI','tag')
p(link('mailto:junming3702@gmail.com','junming3702@gmail.com')+' &nbsp; | &nbsp; '+link('https://junming3702-cmyk.github.io/','Portfolio')+' &nbsp; | &nbsp; '+link('https://github.com/junming3702-cmyk','GitHub'))
p('I combine quantity-surveying practice with digital methods to design and evaluate AI-assisted workflows for construction decision-making. Open to applied AI roles and PhD research opportunities.')
section('EDUCATION')
p('MSc in Construction Management | City University of Hong Kong','title')
p('2023-2024','meta')
p('Dissertation: <i>Development and Application of BIM-Based Virtual Reality Support Tools in MiC Projects.</i> Coursework included virtual design and construction, digital construction, research methods, statistics and geographic data analysis.')
p('BEng in Quantity Surveying | Chengdu University','title')
p('2018-2022','meta')
p('Undergraduate thesis: <i>Application of VR in Architectural Education.</i>')
section('PROFESSIONAL EXPERIENCE')
p('Assistant Quantity Surveyor | Currie &amp; Brown (China) Limited','title')
p('Hong Kong | September 2024-September 2025','meta')
p('Prepared and checked quantities and Bills of Quantities for structural metalwork, concrete and reinforcement on residential and public-housing work. Reviewed drawings, progress records and variation instructions; supported material-price enquiries, budget checks and variation review.')
p('Assistant Quantity Surveyor | RongHui Project Management Co., Ltd','title')
p('Mainland China | June 2022-June 2023','meta')
p('Prepared budgets, Bills of Quantities and monthly fund-utilisation plans. Coordinated drawings, site records and subcontractor quantity checks, and helped resolve material-specification and quantity discrepancies.')
section('RESEARCH INTERESTS')
p('Industry digitalization; evidence-grounded decision support; human-AI collaboration; and, as a longer-term direction, cross-sector transfer. Current questions concern decisions under incomplete or changing project information, the use of expert corrections, and evaluation of decision quality and review effort.')
section('METHODS, TOOLS AND LANGUAGES')
p('<b>Construction:</b> quantity take-off, cost estimating, BoQ preparation, variation assessment and design-information review; Excel, Glodon TBQ, Bluebeam and Microsoft Project.')
p('<b>Digital methods:</b> BIM and VR research, spatial analysis and practitioner feedback; Revit, Navisworks, QGIS, SPSS and Power BI.')
p('<b>Applied AI:</b> Python, LangChain/LCEL, RAG, BM25 and dense retrieval, structured outputs, evidence gates, functional tests and professional appraisal.')
p('<b>Languages:</b> Mandarin (native), English (working proficiency), Cantonese (intermediate).')
story.append(PageBreak())
p('Selected research and projects','name')
p('Project evidence and materials: '+link('https://junming3702-cmyk.github.io/#project','junming3702-cmyk.github.io/#project'))
section('EVIDENCE-GROUNDED AI FOR CONSTRUCTION TENDERING')
p('Independent applied research | February 2026-present | Manuscript submitted','meta')
p('Developed a task-bound human-AI pre-review prototype connecting tender excerpts, candidate regulatory evidence and inspectable professional dispositions.')
p('<b>My contribution:</b> independently defined the project purpose and research questions; designed the complete architecture, legal-authority RAG layers, ordered L1-L4 retrieval and BM25 + dense ranking; designed source-bound reasoning, deterministic release gates and evaluation; implemented, reviewed and refined the program.')
p('<b>Reported evaluation:</b> on one previously unseen project (IPV01), 24 records were delivered from 30 selected tasks. Each of two domain evaluators passed source traceability on 23 of 24 delivered records; they accepted 21 and 16 records, respectively. These separate outcomes support task-level pre-review feasibility; they do not establish full-tender deployment or measured productivity gains.')
p('<b>Collaboration:</b> AI tools assisted code implementation and experimental tables under my direction. Domain practitioners appraised outputs and contributed interview feedback to evaluation design.')
p(link('https://junming3702-cmyk.github.io/tendering.html','Case study')+' | '+link('https://github.com/junming3702-cmyk/-LLM','Public code and synthetic examples')+'. Task-level IPV01 records and the submitted manuscript are not public.')
section('BIM-VR FOR MODULAR INTEGRATED CONSTRUCTION')
p('Individual MSc dissertation | City University of Hong Kong | 2023-2024','meta')
p('Developed BIM-based VR support for MiC, including an interactive VR prototype, addressing lifting-path planning, spatial coordination and site logistics. Analysed qualitative practitioner feedback.')
p('<b>Output:</b> master\'s dissertation and interactive prototype. Demonstration materials are not yet public; '+link('https://junming3702-cmyk.github.io/bim-vr.html','research brief')+' available online.')
section('15-MINUTE COMMUNITY LIVING CIRCLE IN HONG KONG')
p('Co-authored coursework | City University of Hong Kong | April 2024','meta')
p('Four-person QGIS study combining points of interest and demographic data to assess service diversity, walking accessibility and per-capita equity across 103 community centres.')
p('<b>My contribution:</b> conclusions, implications and limitations; the corresponding report and presentation sections; integration of the interim presentation. Spatial-analysis outputs are credited to the group.')
p('<b>Team:</b> Chen Xinying, Qu Shiyan, Xu Junyi and Zhang Junming. '+link('https://junming3702-cmyk.github.io/qgis.html','Original maps, results and contribution-table excerpts')+' are available online.')
section('RELATED PUBLIC MECHANISM STUDY')
p('Design-revision-to-BoQ attribution: a separate 24-case synthetic study of source-supported mappings and abstention. '+link('https://github.com/junming3702-cmyk/-LLM/tree/main/phase1_public/experiments/design_revision_boq_fpa','Public study materials')+'.')
OUT.parent.mkdir(parents=True,exist_ok=True)
SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=45,leftMargin=45,topMargin=38,bottomMargin=52,title='Junming Zhang - Public CV',author='Junming Zhang').build(story,onFirstPage=footer,onLaterPages=footer)
print(OUT)
