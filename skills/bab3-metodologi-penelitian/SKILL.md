---
name: bab3-metodologi-penelitian
description: Panduan dan generator otomatis Bab 3 Metodologi Penelitian (A-F) serta penyusunan instrumen penelitian lengkap (Pretest/Posttest, Rubrik Polya, Lembar Observasi Sintaks AI Agentic, dan Angket Skala Likert).
---

# SKILL: Bab 3 Metodologi Penelitian & Instrumen Lengkap

Skill ini mengorkestrasi penyusunan **Bab III Metodologi Penelitian** skripsi kuantitatif serta seluruh paket instrumen pengumpulan data lapangan secara otomatis, presisi, dan bebas halusinasi sesuai standar Prof. Dr. Sugiyono (2013).

---

## 1. Sistematika Baku Bab III (A sampai F)

```text
BAB III METODOLOGI PENELITIAN
A. Metode Penelitian
   1. Pendekatan Kuantitatif Filsafat Positivisme (Sugiyono, 2013: 7)
   2. Metode Eksperimen Deduktif Kausal Bivariat (X -> Y)
   3. Operasionalisasi Variabel (X: Alur Kerja AI Agentic, Y: Problem Solving Polya)
B. Desain Penelitian
   1. Quasi-Experimental Design (Alasan Intact Group / Rombel SMK)
   2. Nonequivalent Control Group Design (Sugiyono, 2013: 79)
   3. Tabel Paradigma Desain (O1 - X - O2 vs O3 - [—] - O4)
C. Populasi dan Sampel
   1. Populasi Target: 2 Rombel Kelas XI RPL SMKN 1 Cirebon (N = 70 siswa)
   2. Kaidah Keterwakilan Penuh (Total Sampling / Sampling Jenuh 100%)
   3. Teknik Sampling: Total Purposive Sampling (XI RPL 1 Eksperimen = 35 siswa, XI RPL 2 Kontrol = 35 siswa, total n = 70 siswa / 100%)
D. Teknik Penelitian
   1. Tes Kinerja Pemrograman (Pretest & Posttest)
   2. Observasi Terstruktur Keterlaksanaan Pembelajaran AI Agentic di Lab
   3. Angket Respon / Kuesioner Penerimaan Teknologi & Kognitif (Skala Likert 4 Poin)
E. Teknik Analisis Data
   1. Statistik Deskriptif (Mean, Median, Modus, Standar Deviasi, Varians)
   2. Uji Prasyarat Analisis (Normalitas Shapiro-Wilk n=35≤50 & Homogenitas Levene)
   3. Uji Peningkatan Kemampuan (N-Gain Score Hake, 1999: g >= 0.70 Tinggi, 0.30 <= g < 0.70 Sedang, g < 0.30 Rendah)
   4. Uji Hipotesis Inferensial (Independent Samples t-test df=35+35-2=68 Sig.(2-tailed)/2 < 0.05 atau Mann-Whitney U)
   5. Analisis Korelasi & Komparasi Sub-Kelompok Intensitas Penggunaan AI Agentic vs Nilai
F. Instrumen Penelitian
   1. Kisi-Kisi 4 Tahap George Polya ke Tugas Pemrograman (Skor Ideal 100)
   2. Uji Kualitas: Validitas Isi (Expert Judgment), Validitas Butir (Pearson Product Moment r >= 0.30), Reliabilitas (Cronbach Alpha r11 >= 0.70), Tingkat Kesukaran (P), dan Daya Pembeda (D)
```

> **ATURAN TATA LETAK DAFTAR PUSTAKA:**  
> Bab 3 berakhir langsung pada **F. Instrumen Penelitian** (poin F.2 Pengujian Kualitas Instrumen).  
> **Dilarang menaruh Daftar Pustaka per bab.** Seluruh rujukan digabungkan ke dalam satu bagian tersendiri (**DAFTAR PUSTAKA**) di bagian paling akhir skripsi setelah **BAB V KESIMPULAN DAN SARAN**.

---

## 2. Paket Instrumen Lapangan Wajib (Field Instruments)

Setiap penelitian eksperimen kuantitatif di SMK mewajibkan 4 paket instrumen yang terverifikasi:

### Paket 1: Naskah Soal Tes Problem Solving (Pretest & Posttest)
- **Format:** Studi kasus rekayasa perangkat lunak autentik.
- **Kasus 1:** Logika Pemrosesan Data & Validasi Input (Struktur Kontrol, Array/Objek, Penanganan Exception).
- **Kasus 2:** Perancangan Modul CRUD & Integrasi Basis Data / API Backend.
- **Tingkat Kesukaran:** Setara antara Pretest dan Posttest (*parallel forms*) untuk mencegah bias instrumen.

### Paket 2: Rubrik Penilaian Analitik 4 Tahap George Polya
1. **Memahami Masalah (*Understanding the Problem* - Skor 0-25):**
   - Skor 25: Mampu mendeskripsikan masukan (*input*), luaran (*output*), batasan masalah (*constraints*), dan *edge cases* secara lengkap dan tepat.
   - Skor 15: Memahami sebagian besar masalah namun melewatkan batasan kritis.
   - Skor 5: Hanya mencatat ulang soal tanpa memahami alur data.
   - Skor 0: Tidak menuliskan identifikasi masalah.
2. **Merencanakan Penyelesaian (*Devising a Plan* - Skor 0-25):**
   - Skor 25: Merancang dekomposisi logika, struktur data, pseudocode/alur modul secara terstruktur dan efisien.
   - Skor 15: Rencana ada tetapi kurang terdekomposisi atau struktur data kurang efisien.
   - Skor 5: Rencana parsial dan tidak logis.
   - Skor 0: Tidak membuat perancangan rencana.
3. **Melaksanakan Rencana (*Carrying out the Plan* - Skor 0-25):**
   - Skor 25: Kode program tertulis valid secara sintaksis, modular, bersih (*clean code*), dan seluruh fungsionalitas berjalan sukses.
   - Skor 15: Kode berjalan tetapi terdapat galat kecil (*minor bug*) pada kondisi tertentu.
   - Skor 5: Kode program macet (*syntax error / runtime crash*).
   - Skor 0: Tidak ada kode program yang ditulis.
4. **Memeriksa Kembali (*Looking Back / Debugging* - Skor 0-25):**
   - Skor 25: Melakukan pengujian dengan minimal 3 *test cases* (normal, ekstrim, galat), melakukan refactor, dan optimasi efisiensi.
   - Skor 15: Menguji kode hanya pada masukan normal tanpa pengetesan kasus batas.
   - Skor 5: Melakukan penelusuran galat tetapi tidak mampu menemukan solusi perbaikan.
   - Skor 0: Tidak melakukan pemeriksaan ulang luaran program.

### Paket 3: Lembar Observasi Keterlaksanaan Pembelajaran AI Agentic
Observasi keterlaksanaan alur kerja agentik (*fidelity of treatment*) pada kelas eksperimen dengan 5 tahapan siklus:
1. *Goal Formulation & Task Prompting:* Siswa merumuskan spesifikasi masalah ke dalam instruksi terarah.
2. *Autonomous Task Decomposition:* Siswa meninjau rencana sub-tugas yang didekomposisi oleh agen AI.
3. *Tool Invocation & Execution:* Siswa mengamati dan memandu eksekusi eksternal (linter, compiler, debugger).
4. *Self-Reflection & Debugging:* Siswa memverifikasi koreksi mandiri yang diajukan agen terhadap logika galat.
5. *Human-in-the-Loop Review:* Siswa mengambil keputusan akhir sebelum mengintegrasikan kode ke dalam repositori tugas.

### Paket 4: Angket / Kuesioner Respon Siswa (Skala Likert 4 Poin)
Menghindari opsi netral (1 = Sangat Tidak Setuju, 2 = Tidak Setuju, 3 = Setuju, 4 = Sangat Setuju) dengan 4 dimensi utama:
1. **Persepsi Kemudahan (*Perceived Ease of Use*):** Interaksi dengan alur kerja AI agentic mudah dipahami dan tidak membebani mental.
2. **Persepsi Kebergunaan (*Perceived Usefulness*):** Agen AI membantu memecahkan kebuntuan logika algoritma dan mempercepat pemahaman modul.
3. **Regulasi Kognitif & Metakognisi (*Metacognitive Regulation*):** Agen AI memicu siswa berpikir kritis saat meninjau hasil evaluasi kode, bukan sekadar menyalin kode.
4. **Efikasi Diri Pemrograman (*Programming Self-Efficacy*):** Peningkatan rasa percaya diri dalam menuntaskan tugas pemrograman mandiri.

---

## 3. Skrip Otomasi Pembangkit Dokumen
- Generator Word Python: `C:\Users\USER\kti-s\templates\skripsi_docx_generator.py`
- Pembangkit Bab 3 Master: `C:\Users\USER\build_bab3_metodologi.py`
- Pembangkit Paket Instrumen Lengkap: `C:\Users\USER\build_paket_instrumen_bab3.py`
