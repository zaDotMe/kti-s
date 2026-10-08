# KTI-S: Sistem Skill & Standar Penyusunan Skripsi (Bab 1 - Bab 5)

Repositori ini memuat seluruh sistem aturan, pedoman baku (*skills*), tata cara penulisan, serta basis rujukan metodologis untuk menyusun dokumen skripsi secara presisi dan sistematis dari **Bab 1 hingga Bab 5**.

## 📌 Landasan Rujukan Utama Proyek
1. **Dokumen Skripsi Riil (Bab 1 & Bab 2):**
   - Bab 1: `C:\Users\USER\Downloads\tugaz\Skripsi_Bab1_AI_Agentic_SMKN1Cirebon_ACC.docx`
   - Bab 2: `C:\Users\USER\Downloads\tugaz\Skripsi_Bab2_AI_Agentic_SMKN1Cirebon_ACC_EXACT.docx`
   - Judul Penelitian: *"Pengaruh Penggunaan AI Agentic terhadap Kemampuan Problem Solving Siswa Kelas XI RPL SMKN 1 Cirebon"*
2. **Buku Metodologi Penelitian:**
   - Prof. Dr. Sugiyono, *Metode Penelitian Kuantitatif, Kualitatif, dan R&D* (Penerbit Alfabeta).
   - Berkas lokal: `C:\Users\USER\Downloads\Buku_Sugiyono_Metode_Penelitian.pdf`.
3. **Standar Layout & Tipografi:**
   - Kertas A4, Margin 4-3-3-3 cm, Times New Roman 12 pt, 1.5 spasi, Rata Justify, Indentasi 1.27 cm, Istilah Asing *Italic*.

---

## 🗂️ Struktur Direktori Repositori

```text
kti-s/
├── README.md
├── .gitignore
├── docs/
│   ├── metodologi_sugiyono_kuantitatif.md   # Bedah metodologi kuantitatif eksperimen Sugiyono
│   └── aturan_tata_tulis_skripsi.md         # Kaidah ejaan, sitasi, dan istilah asing
├── skills/
│   ├── skripsi-master/
│   │   └── SKILL.md                         # Orchestrator & guardrail anti-halusinasi
│   ├── bab1-pendahuluan/
│   │   └── SKILL.md                         # Aturan 10 paragraf latar belakang & sistematika
│   ├── bab2-kajian-teori/
│   │   └── SKILL.md                         # Struktur 5 poin teori & perumusan hipotesis
│   ├── bab3-metodologi-penelitian/
│   │   └── SKILL.md                         # Desain quasi-experiment Sugiyono & analisis data
│   ├── bab4-hasil-dan-pembahasan/
│   │   └── SKILL.md                         # Penyajian deskriptif, uji prasyarat & uji hipotesis
│   ├── bab5-kesimpulan-dan-saran/
│   │   └── SKILL.md                         # Sinkronisasi kesimpulan-rumusan masalah & saran
│   └── format-dan-layout/
│       └── SKILL.md                         # Parameter layout halaman, nomor otomatis Word
└── templates/
    └── skripsi_docx_generator.py            # Skrip otomatisasi format Word baku python-docx
```

---

## 🚀 Cara Menjalankan & Berkolaborasi
Setiap penyusunan bab dikawal langsung oleh panduan skill terkait di folder `skills/`. Pengguna dan AI agent bekerja selaras langkah demi langkah (*step-by-step*) dengan prinsip:
- **Zero Halusinasi:** Teori, nama ahli, tahun, dan rujukan wajib riil dan terverifikasi.
- **Konsistensi Metodologis:** Konsep kuantitatif selalu mengacu pada rujukan bab Sugiyono.
- **Standar Format Presisi:** Tidak ada penomoran manual tab yang melenceng; semua menggunakan standar Word XML yang rapi.
