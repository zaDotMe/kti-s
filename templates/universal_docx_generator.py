"""
Universal KTI DOCX Generator Engine
Membangun dokumen Word berstandar akademik tinggi (A4, 4-3-3-3 cm, Times New Roman, 1.5 spasi, XML List Numbering terisolasi).
Dapat digunakan untuk segala topik KTI/Skripsi tanpa template kaku.
"""
import os, sys, shutil, zipfile
import docx
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml

sys.stdout.reconfigure(encoding='utf-8')

class KTIDocumentBuilder:
    def __init__(self, output_path, top_cm=4.0, left_cm=4.0, bottom_cm=3.0, right_cm=3.0):
        self.output_path = output_path
        self.doc = docx.Document()
        self.used_num_ids = []
        self.current_num_id = 500
        
        # Atur margin halaman
        for sec in self.doc.sections:
            sec.top_margin = Cm(top_cm)
            sec.bottom_margin = Cm(bottom_cm)
            sec.left_margin = Cm(left_cm)
            sec.right_margin = Cm(right_cm)
            sec.page_width = Cm(21.0)
            sec.page_height = Cm(29.7)

    def get_next_num_id(self):
        self.current_num_id += 1
        return self.current_num_id

    def add_p(self, runs_data, align=WD_ALIGN_PARAGRAPH.JUSTIFY, first_indent=Cm(1.27), left_indent=None, space_before=Pt(0), space_after=Pt(0), line_spacing=1.5):
        p = self.doc.add_paragraph()
        p.paragraph_format.line_spacing = line_spacing
        p.paragraph_format.space_before = space_before
        p.paragraph_format.space_after = space_after
        if first_indent is not None:
            p.paragraph_format.first_line_indent = first_indent
        if left_indent is not None:
            p.paragraph_format.left_indent = left_indent
        p.alignment = align
        
        for item in runs_data:
            text = item[0]
            italic = item[1] if len(item) > 1 else False
            bold = item[2] if len(item) > 2 else False
            font_size = item[3] if len(item) > 3 else Pt(12)
            font_name = item[4] if len(item) > 4 else 'Times New Roman'
            
            r = p.add_run(text)
            r.font.name = font_name
            r.font.size = font_size
            r.italic = italic
            r.bold = bold
        return p

    def add_chapter_title(self, chapter_roman, chapter_name):
        self.add_p([(f"BAB {chapter_roman}", False, True, Pt(12))], align=WD_ALIGN_PARAGRAPH.CENTER, first_indent=None, space_before=Pt(0), space_after=Pt(2))
        return self.add_p([(chapter_name.upper(), False, True, Pt(12))], align=WD_ALIGN_PARAGRAPH.CENTER, first_indent=None, space_before=Pt(0), space_after=Pt(12))

    def add_subheading_A(self, prefix, title, italic=False):
        runs = [(prefix, False, True, Pt(12)), (title, italic, True, Pt(12))]
        return self.add_p(runs, align=WD_ALIGN_PARAGRAPH.JUSTIFY, first_indent=Cm(-0.63), left_indent=Cm(0.63), space_before=Pt(10), space_after=Pt(3))

    def add_subheading_1(self, prefix, title, italic=False):
        runs = [(prefix, False, True, Pt(12)), (title, italic, True, Pt(12))]
        return self.add_p(runs, align=WD_ALIGN_PARAGRAPH.JUSTIFY, first_indent=Cm(-0.63), left_indent=Cm(1.27), space_before=Pt(5), space_after=Pt(2))

    def add_list_item(self, num_id, runs_data, left_indent=Cm(1.27), hanging_indent=Cm(-0.63)):
        p = self.doc.add_paragraph()
        p.style = 'List Paragraph'
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.left_indent = left_indent
        p.paragraph_format.first_line_indent = hanging_indent
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        
        numPr_xml = f'''<w:numPr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
            <w:ilvl w:val="0"/>
            <w:numId w:val="{num_id}"/>
        </w:numPr>'''
        p._p.get_or_add_pPr().append(parse_xml(numPr_xml))
        
        for item in runs_data:
            text = item[0]
            italic = item[1] if len(item) > 1 else False
            bold = item[2] if len(item) > 2 else False
            font_size = item[3] if len(item) > 3 else Pt(12)
            font_name = item[4] if len(item) > 4 else 'Times New Roman'
            
            r = p.add_run(text)
            r.font.name = font_name
            r.font.size = font_size
            r.italic = italic
            r.bold = bold
        return p

    def add_table_data(self, headers, rows_data, col_widths=None):
        table = self.doc.add_table(rows=len(rows_data) + 1, cols=len(headers))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        
        # Terapkan border hitam tegas (single 0.5 pt) dan margin sel agar tidak ditolak pembimbing
        self.apply_table_borders(table)
        self.apply_table_margins(table)
        
        # Header
        for col_idx, h in enumerate(headers):
            cell = table.cell(0, col_idx)
            cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
            cell.paragraphs[0].paragraph_format.line_spacing = 1.0
            cell.paragraphs[0].paragraph_format.space_before = Pt(2)
            cell.paragraphs[0].paragraph_format.space_after = Pt(2)
            r = cell.paragraphs[0].add_run(h)
            r.bold = True
            r.font.name = 'Times New Roman'
            r.font.size = Pt(10.5)

        # Rows
        for row_idx, rdata in enumerate(rows_data):
            for col_idx, val in enumerate(rdata):
                cell = table.cell(row_idx + 1, col_idx)
                cell.paragraphs[0].paragraph_format.line_spacing = 1.0
                cell.paragraphs[0].paragraph_format.space_before = Pt(2)
                cell.paragraphs[0].paragraph_format.space_after = Pt(2)
                cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx == 0 or len(val) < 8 else WD_ALIGN_PARAGRAPH.JUSTIFY
                r = cell.paragraphs[0].add_run(val)
                r.font.name = 'Times New Roman'
                r.font.size = Pt(10)
        return table

    @staticmethod
    def apply_table_borders(table, color="000000", sz="4", val="single"):
        """Menambahkan border tegas pada tabel Word (w:tblBorders)."""
        tblPr = table._tbl.tblPr
        existing = tblPr.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tblBorders')
        if existing is not None:
            tblPr.remove(existing)
        
        borders_xml = f'''<w:tblBorders xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
            <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
        </w:tblBorders>'''
        tblPr.append(parse_xml(borders_xml))

    @staticmethod
    def apply_table_margins(table, top_d=80, bottom_d=80, left_d=120, right_d=120):
        """Menambahkan bantalan teks (padding/margin sel) agar tulisan tidak menabrak garis border."""
        tblPr = table._tbl.tblPr
        existing = tblPr.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tblCellMar')
        if existing is not None:
            tblPr.remove(existing)
            
        cell_mar_xml = f'''<w:tblCellMar xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
            <w:top w:w="{top_d}" w:type="dxa"/>
            <w:bottom w:w="{bottom_d}" w:type="dxa"/>
            <w:left w:w="{left_d}" w:type="dxa"/>
            <w:right w:w="{right_d}" w:type="dxa"/>
        </w:tblCellMar>'''
        tblPr.append(parse_xml(cell_mar_xml))

    def save_and_patch(self):
        """
        Menyimpan dokumen dan melakukan patching pada word/numbering.xml
        agar seluruh penomoran list me-reset ke angka 1 dengan benar.
        """
        temp_saved = self.output_path + ".tmp.docx"
        temp_fixed = self.output_path + ".fixed.docx"
        
        self.doc.save(temp_saved)
        
        with zipfile.ZipFile(temp_saved, 'r') as zin:
            with zipfile.ZipFile(temp_fixed, 'w') as zout:
                for item in zin.infolist():
                    data = zin.read(item.filename)
                    if item.filename == 'word/numbering.xml':
                        xml_str = data.decode('utf-8')
                        num_entries = []
                        for nid in sorted(list(set(self.used_num_ids))):
                            entry = f"""  <w:num w:numId="{nid}">
    <w:abstractNumId w:val="1"/>
    <w:lvlOverride w:ilvl="0">
      <w:startOverride w:val="1"/>
    </w:lvlOverride>
  </w:num>"""
                            num_entries.append(entry)
                        nums_to_insert = '\n'.join(num_entries) + '\n'
                        if '</w:numbering>' in xml_str:
                            xml_str = xml_str.replace('</w:numbering>', nums_to_insert + '</w:numbering>')
                        data = xml_str.encode('utf-8')
                    zout.writestr(item, data)

        if os.path.exists(self.output_path):
            try:
                os.remove(self.output_path)
            except PermissionError:
                pass

        shutil.move(temp_fixed, self.output_path)
        if os.path.exists(temp_saved):
            os.remove(temp_saved)
        print(f"[SUCCESS] Dokumen terstandar selesai dibuat: {self.output_path}")

if __name__ == "__main__":
    print("Universal KTI DOCX Builder Ready.")
