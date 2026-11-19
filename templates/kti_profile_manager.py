"""
KTI Profile Manager & Prior Chapter Ingestor
Modul untuk mengelola konteks penelitian (research_profile.json) dan membaca bab sebelumnya.
"""
import os, sys, json, re
try:
    import docx
except ImportError:
    docx = None

PROFILE_PATH = "research_profile.json"

def load_profile(path=PROFILE_PATH):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def save_profile(data, path=PROFILE_PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"[OK] Profil penelitian berhasil disimpan di: {path}")

def stress_test_title(title):
    """
    Menganalisis judul penelitian untuk mengekstrak Variabel X, Variabel Y, dan Subjek.
    """
    clean_title = title.strip().strip('"').strip("'")
    
    # Deteksi Variabel X dan Y
    var_x = None
    var_y = None
    subjek = None
    
    match_pengaruh = re.search(r"pengaruh\s+(.+?)\s+terhadap\s+(.+?)\s+pada\s+(.+)", clean_title, re.IGNORECASE)
    if not match_pengaruh:
        match_pengaruh = re.search(r"pengaruh\s+(.+?)\s+terhadap\s+(.+?)\s+(siswa|mahasiswa|peserta didik)\s+(.+)", clean_title, re.IGNORECASE)
        if match_pengaruh:
            var_x = match_pengaruh.group(1).strip()
            var_y = match_pengaruh.group(2).strip()
            subjek = (match_pengaruh.group(3) + " " + match_pengaruh.group(4)).strip()
    else:
        var_x = match_pengaruh.group(1).strip()
        var_y = match_pengaruh.group(2).strip()
        subjek = match_pengaruh.group(3).strip()
        
    analysis = {
        "judul_asli": clean_title,
        "terdeteksi": {
            "variabel_bebas_X": var_x if var_x else "Perlu konfirmasi spesifik",
            "variabel_terikat_Y": var_y if var_y else "Perlu konfirmasi spesifik",
            "subjek_penelitian": subjek if subjek else "Perlu konfirmasi spesifik"
        },
        "catatan_keterukuran": (
            f"Variabel Y ('{var_y}') wajib memiliki indikator operasional yang terukur (misal: soal tes, rubrik unjuk kerja, atau angket standar)."
            if var_y else "Pastikan variabel terikat dapat diukur secara kuantitatif."
        ),
        "kelayakan": "Format judul telah memenuhi struktur kausal baku (X -> Y)." if (var_x and var_y) else "Struktur judul perlu dirapikan ke format standar hubungan variabel."
    }
    return analysis

def ingest_document(file_path):
    """
    Mengekstrak teks dan mendeteksi bab/variabel dari dokumen docx atau teks.
    """
    if not os.path.exists(file_path):
        return {"error": f"File tidak ditemukan: {file_path}"}
    
    text_content = []
    if file_path.lower().endswith(".docx"):
        if not docx:
            return {"error": "Modul python-docx belum terinstall"}
        doc = docx.Document(file_path)
        for p in doc.paragraphs:
            t = p.text.strip()
            if t:
                text_content.append(t)
    elif file_path.lower().endswith((".txt", ".md")):
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            text_content = [line.strip() for line in f if line.strip()]
    else:
        return {"error": "Format berkas tidak didukung. Harap gunakan file .docx, .md, atau .txt"}
    
    full_text = "\n".join(text_content)
    
    # Deteksi Judul
    detected_title = None
    for p in text_content[:15]:
        if "PENGARUH" in p.upper() or "HUBUNGAN" in p.upper() or "EFEKTIVITAS" in p.upper():
            detected_title = p
            break
            
    # Deteksi Rumusan Masalah
    rumusan = []
    found_rm = False
    for p in text_content:
        if "RUMUSAN MASALAH" in p.upper() or "PERUMUSAN MASALAH" in p.upper():
            found_rm = True
            continue
        if found_rm:
            if p.startswith(("1.", "2.", "3.", "a.", "b.", "1)", "2)")):
                rumusan.append(p)
            elif "TUJUAN" in p.upper() or "MANFAAT" in p.upper():
                break

    return {
        "file": file_path,
        "total_paragraf": len(text_content),
        "total_karakter": len(full_text),
        "judul_terdeteksi": detected_title,
        "rumusan_masalah_terdeteksi": rumusan
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "stress-test" and len(sys.argv) > 2:
            title_input = " ".join(sys.argv[2:])
            print(json.dumps(stress_test_title(title_input), indent=2, ensure_ascii=False))
        elif cmd == "ingest" and len(sys.argv) > 2:
            print(json.dumps(ingest_document(sys.argv[2]), indent=2, ensure_ascii=False))
        else:
            print("Penggunaan: python kti_profile_manager.py [stress-test <judul> | ingest <file_path>]")
    else:
        print("KTI Profile Manager Helper Active.")
