# 🎓 KTI-Agent Universal Framework (Bab 1 - Bab 5)

Framework cerdas berbasis *Agentic Skills* dan bimbingan sokratik untuk membantu siswa, mahasiswa, dan guru menyusun **Karya Tulis Ilmiah (KTI), Skripsi, atau Tugas Akhir** dari dasar (*from scratch*), topik apa saja, berstandar akademik tinggi, bebas plagiasi (*anti-slop*), dan mendidik pengguna agar paham 100% apa yang mereka teliti.

---

## 🌟 Mengapa Framework Ini Berbeda?

1. **Agnostik Topik (Bisa Dipakai Siapa Saja):**  
   Tidak terkunci pada satu judul atau sekolah. Bisa digunakan untuk topik Informatika, Teknik, Pendidikan, IPA, IPS, Manajemen, dll.
2. **Anti-Slop & Membangun dari Dasar:**  
   Bukan template kaku yang isinya sama untuk semua orang. Naskah dirajut murni dari masalah nyata pengguna di lapangan.
3. **State Management Berkelanjutan (`research_profile.json`):**  
   Mampu melanjutkan pengerjaan di tengah jalan (misal langsung lompat ke Bab 2 atau Bab 3) dengan membaca (*ingest*) berkas bab sebelumnya.
4. **Socratic Mentoring & Defense Simulation:**  
   AI tidak bertindak sebagai joki buta, melainkan sebagai **Dosen Pembimbing Kritis** yang menjelaskan istilah teknis dalam bahasa awam dan menyiapkan simulasi pertanyaan sidang penguji di setiap bab.
5. **Kaidah Tunggal Daftar Pustaka:**  
   Daftar Pustaka **hanya ada satu** di bagian paling akhir skripsi (setelah Bab V). Bab I, II, III, dan IV tidak memuat daftar pustaka terpisah.

---

## 🗂️ Arsitektur Direktori Repositori

```text
kti-s/
├── README.md                                # Dokumentasi utama repositori
├── research_profile.example.json            # Contoh skema state konteks penelitian
├── docs/
│   ├── panduan_penggunaan_framework.md      # Panduan langkah demi langkah penggunaan framework
│   ├── metodologi_sugiyono_kuantitatif.md   # Bedah metodologi kuantitatif eksperimen Sugiyono
│   ├── struktur_bab3_metodologi.md          # Spesifikasi baku struktur Bab III
│   └── aturan_tata_tulis_skripsi.md         # Kaidah tipografi baku dan istilah asing
├── skills/
│   ├── kti-universal-orchestrator/
│   │   └── SKILL.md                         # Gatekeeper: Onboarding, Ingest file bab lama, Stress-test judul
│   ├── kti-socratic-mentor/
│   │   └── SKILL.md                         # Edukasi konsep bahasa awam & simulasi ujian sidang penguji
│   ├── skripsi-master/
│   │   └── SKILL.md                         # Master orchestrator penghubung Bab 1 s.d. Bab 5
│   ├── bab1-pendahuluan/
│   │   └── SKILL.md                         # Panduan piramida terbalik 10 paragraf latar belakang
│   ├── bab2-kajian-teori/
│   │   └── SKILL.md                         # 5 poin teori per variabel, sintesis mandiri & hipotesis
│   ├── bab3-metodologi-penelitian/
│   │   └── SKILL.md                         # Desain penelitian, sampel 50%+1, analisis & paket instrumen
│   ├── bab4-hasil-dan-pembahasan/
│   │   └── SKILL.md                         # Statistik deskriptif, uji prasyarat, uji-t, dan diskusi hasil
│   ├── bab5-kesimpulan-dan-saran/
│   │   └── SKILL.md                         # Simpul simetris, saran operasional & Daftar Pustaka tunggal
│   └── format-dan-layout/
│       └── SKILL.md                         # Standar margin 4-3-3-3 cm, font TNR 12pt, 1.5 spasi
└── templates/
    ├── universal_docx_generator.py          # Generator Python dokumen Word berstandar akademik
    ├── kti_profile_manager.py               # CLI tool untuk stress-test judul & ingest berkas
    └── skripsi_docx_generator.py            # Generator dasar docx
```

---

## 🚀 Cara Menggunakan Framework

### 1. Inisialisasi Proyek Baru
Jalankan stress-test judul untuk memastikan judul memiliki variabel X, Y, dan subjek yang terukur:
```bash
python templates/kti_profile_manager.py stress-test "Pengaruh Media Pembelajaran Interaktif terhadap Hasil Belajar Siswa Kelas XI RPL"
```

### 2. Melanjutkan dari Bab Sebelumnya
Jika Anda sudah memiliki draf Bab 1 atau Bab 2 dan ingin langsung membuat Bab 3:
```bash
python templates/kti_profile_manager.py ingest "draf/Bab1_Pendahuluan.docx"
```

### 3. Eksekusi dengan AI Agent
Cukup panggil skill `kti-universal-orchestrator` atau `skripsi-master` di AI agent Anda (Claude Code, Antigravity, OpenCode, Cursor, Cline, dll). Agen akan memandu proses pengerjaan secara dialogis dan menghasilkan naskah `.docx` siap cetak!
