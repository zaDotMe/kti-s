---
name: bab3-metodologi-penelitian
description: Panduan dan generator otomatis Bab 3 Metodologi Penelitian (A-F) serta penyusunan instrumen penelitian lengkap dengan protokol wajib interogasi populasi/sampel riil.
---

# SKILL: Bab 3 Metodologi Penelitian & Instrumen Lengkap

Skill ini mengorkestrasi penyusunan **Bab III Metodologi Penelitian** skripsi kuantitatif serta seluruh paket instrumen pengumpulan data lapangan secara otomatis, presisi, dan bebas halusinasi sesuai standar Prof. Dr. Sugiyono (2013).

---

## ⚠️ PROTOKOL WAJIB: INTEROGASI POPULASI & SAMPEL RIIL (ANTI-HALUSINASI)

> **DILARANG KERAS MENGARANG ATAU MENGASUMSIKAN JUMLAH KELAS DAN JUMLAH SISWA!**  
> Sebelum menyusun Sub-bab C (Populasi dan Sampel), AI **WAJIB** menanyakan secara terperinci kepada pengguna:
> 
> 1. **Berapa jumlah rombongan belajar (rombel/kelas)** yang ada pada tingkatan/jurusan target di sekolah tersebut? (Contoh: Apakah ada 2 kelas, 3 kelas, atau 4 kelas?)
> 2. **Berapa jumlah siswa riil di masing-masing rombel/kelas tersebut?** (Contoh: RPL 1 = 35 siswa, RPL 2 = 35 siswa).
> 3. **Berapa total populasi ($N$) gabungan seluruh kelas tersebut?**
> 4. **Kelas mana yang ditetapkan sebagai Kelas Eksperimen** (diberi perlakuan/media baru) dan **mana yang menjadi Kelas Kontrol** (model konvensional)?
> 5. **Apakah menggunakan Total Sampling / Sampling Jenuh (100% populasi jika kelas terbatas)** atau **Cluster Random / Purposive Sampling**?
>
> Simpan seluruh data riil ini ke `research_profile.json` sebelum naskah Bab III digenerate.

---

## 1. Sistematika Baku Bab III (A sampai F)

```text
BAB III METODOLOGI PENELITIAN
A. Metode Penelitian
   1. Pendekatan Kuantitatif Filsafat Positivisme (Sugiyono, 2013: 7)
   2. Metode Kausal-Komparatif (Ex-Post Facto) Mengamati Fenomena Adopsi AI Lapangan
   3. Operasionalisasi Variabel (X: Penggunaan Alur Kerja AI Agentic, Y: Problem Solving Polya DPK)
B. Desain Penelitian
   1. Desain Kausal-Komparatif Dua Kelompok Pengukuran Awal-Akhir (Static Group Pretest-Posttest Design)
   2. Nilai Awal DPK Semester 1 (Pretest Alami Pra-Adopsi AI O1 & O3) vs Nilai Akhir DPK Semester 2 (Posttest Alami Pasca-Adopsi AI O2 & O4)
   3. Tabel Paradigma Desain Penelitian Kausal-Komparatif Ex-Post Facto
C. Populasi dan Sampel
   1. Populasi Target: 2 Rombel Kelas XI RPL SMKN 1 Cirebon (N = 70 siswa)
   2. Kaidah Keterwakilan Penuh (Total Sampling / Sampling Jenuh 100%)
   3. Pemilahan Subjek via Angket Verifikasi Adopsi AI (Kelompok Pengguna AI n1 vs Kelompok Non-Pengguna n2)
D. Teknik Penelitian
   1. Dokumentasi Nilai Ujian Prestasi Koding DPK (Semester 1 & Semester 2)
   2. Angket Daring Verifikasi Adopsi AI Agentic (Google Form 4 Butir Pertanyaan Faktual Terarah)
E. Teknik Analisis Data
   1. Statistik Deskriptif (Mean, Median, Modus, Standar Deviasi, Varians)
   2. Uji Prasyarat Analisis (Normalitas Shapiro-Wilk n≤50 & Homogenitas Levene)
   3. Uji Peningkatan Kemampuan (N-Gain Score Hake, 1999: g >= 0.70 Tinggi, 0.30 <= g < 0.70 Sedang, g < 0.30 Rendah)
   4. Uji Hipotesis Komparatif (Independent Samples t-test df=n1+n2-2 Sig.(2-tailed)/2 < 0.05 atau Mann-Whitney U)
   5. Analisis Ragam Perangkat AI Agentic vs Capaian Prestasi
F. Instrumen Penelitian
   1. Kisi-Kisi 4 Tahap George Polya Soal Ujian Prestasi DPK (Skor Maksimal 100)
   2. Uji Kualitas Instrumen Ujian: Validitas Isi (Expert Judgment Keselarasan CP/ATP) dan Standarisasi Penilaian
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
