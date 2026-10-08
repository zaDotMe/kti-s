"""
Script otomasi pembuatan dokumen Word skripsi dengan standar layout baku:
A4, Margin 4-3-3-3 cm, Times New Roman 12pt, 1.5 spasi, First Line Indent 1.27 cm.
"""
import docx
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

def create_base_document():
    doc = docx.Document()
    for section in doc.sections:
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.top_margin = Cm(4.0)
        section.bottom_margin = Cm(3.0)
        section.left_margin = Cm(3.0)
        section.right_margin = Cm(3.0)
    return doc

def add_chapter_title(doc, chapter_number_str, chapter_title_str):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(12)
    p.paragraph_format.first_line_indent = None
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p.add_run(chapter_number_str + "\n" + chapter_title_str)
    r1.font.name = "Times New Roman"
    r1.font.size = Pt(12)
    r1.bold = True
    return p

def add_subheading(doc, text_parts):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.first_line_indent = None
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    for text, bold, italic in text_parts:
        r = p.add_run(text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(12)
        r.bold = bold
        r.italic = italic
    return p

def add_body_paragraph(doc, text_runs):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.first_line_indent = Cm(1.27)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    for text, bold, italic in text_runs:
        r = p.add_run(text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(12)
        r.bold = bold
        r.italic = italic
    return p

def add_list_item(doc, num_str, text_runs):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.left_indent = Cm(1.27)
    p.paragraph_format.first_line_indent = Cm(-0.63)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_num = p.add_run(num_str + "\t")
    r_num.font.name = "Times New Roman"
    r_num.font.size = Pt(12)
    for text, bold, italic in text_runs:
        r = p.add_run(text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(12)
        r.bold = bold
        r.italic = italic
    return p
