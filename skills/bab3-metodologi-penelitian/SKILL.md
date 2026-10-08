---
name: bab3-metodologi-penelitian
description: Panduan penyusunan Bab 3 Metodologi Penelitian kuantitatif eksperimen dengan struktur A sampai F (Metode, Desain, Populasi-Sampel 50%+1, Teknik Penelitian, Analisis Data, Instrumen).
---

# SKILL: Bab 3 Metodologi Penelitian

Skill ini mengatur penyusunan **Bab III Metodologi Penelitian** skripsi kuantitatif secara presisi sesuai struktur khusus yang ditentukan.

## Struktur Wajib Bab III (A - F)
```text
BAB III METODOLOGI PENELITIAN
A. Metode Penelitian
B. Desain Penelitian
C. Populasi dan Sampel
D. Teknik Penelitian
E. Teknik Analisis Data
F. Instrumen Penelitian
```

---

## Rincian Per Bagian

### A. Metode Penelitian
- **Pilihan Acuan:** Memilih dan merujuk secara mendalam pada **Sugiyono** (atau diperbandingkan dengan Ali Muto).
- **Karakteristik:** Pendekatan **Kuantitatif** berlandaskan filsafat positivisme. Data berupa angka numerik yang diuji melalui analisis statistik inferensial untuk membuktikan ada tidaknya hubungan kausal sebab-akibat antara variabel $X$ (*AI agentic*) dan $Y$ (*problem solving*).

### B. Desain Penelitian
- **Klasifikasi:** Penelitian **Eksperimen Semu (*Quasi-Experimental Design*)**.
- **Alasan Pemilihan (Konteks SMK):** Peneliti tidak dapat merombak/mengacak siswa secara individual (*pure random*) karena akan mengganggu jadwal pelajaran dan struktur rombel kelas XI RPL SMKN 1 Cirebon.
- **Model Desain:** **Nonequivalent Control Group Design** (Sugiyono, 2013).
  $$\begin{array}{lccc}
  \text{Kelompok Eksperimen} & O_1 & X & O_2 \\
  \hline
  \text{Kelompok Kontrol} & O_3 & - & O_4
  \end{array}$$
  - $O_1, O_3$: Tes awal (*pretest*)
  - $X$: Perlakuan menggunakan alur kerja *AI agentic*
  - $-$: Pembelajaran konvensional
  - $O_2, O_4$: Tes akhir (*posttest*)

### C. Populasi dan Sampel
- **Populasi:** Seluruh siswa kelas XI Konsentrasi Keahlian Rekayasa Perangkat Lunak (RPL) SMKN 1 Cirebon tahun ajaran berjalan.
- **Sampel (Aturan 50% + 1):**
  - Mengambil minimal **50% + 1** dari total populasi siswa / rombel kelas XI RPL untuk menjamin keterwakilan yang kuat dan memenuhi syarat sampel kuantitatif.
  - Penentuan rombel dilakukan menggunakan teknik **Purposive Sampling** atau **Cluster Sampling** dengan memastikan kedua kelas (eksperimen & kontrol) memiliki kondisi awal yang homogen.

### D. Teknik Penelitian
- **Teknik Utama:**
  1. **Tes Kinerja / Uraian Studi Kasus Pemrograman:** Diberikan saat *pretest* dan *posttest* untuk mengukur 4 indikator *problem solving* Polya.
  2. **Observasi (*Observation*):** Lembar observasi keterlaksanaan intervensi *AI agentic workflow* pada proses pembelajaran di laboratorium komputer.
  3. **Kuesioner / Angket (Opsional Pendukung):** Digunakan untuk mengukur persepsi kemudahan (*perceived ease of use*) dan keterlibatan kognitif siswa selama berinteraksi dengan *AI agentic*.

### E. Teknik Analisis Data
Mengacu pada Sugiyono (Bab 8 & 9):
1. **Statistik Deskriptif:** Mean, median, modus, standar deviasi, varians, dan tabel distribusi frekuensi.
2. **Uji Prasyarat Analisis:**
   - **Uji Normalitas:** Menguji apakah sebaran skor berdistribusi normal (Shapiro-Wilk / Kolmogorov-Smirnov, taraf signifikansi $\alpha = 0{,}05$).
   - **Uji Homogenitas:** Menguji kesamaan varians antar kelompok (Levene's Test, taraf signifikansi $\alpha = 0{,}05$).
3. **Uji Peningkatan Kemampuan (N-Gain Score):**
   $$g = \frac{\text{Posttest} - \text{Pretest}}{\text{Skor Maksimal} - \text{Pretest}}$$
4. **Uji Hipotesis (Statistik Inferensial):**
   - Jika data normal dan homogen: **Independent Samples t-test**.
   - Jika data tidak berdistribusi normal: **Mann-Whitney U Test**.
   - Kriteria: Tolak $H_0$ jika nilai $\text{Sig. (2-tailed)} < 0{,}05$.

### F. Instrumen Penelitian
1. **Kisi-kisi Instrumen Tes:** Mengacu pada 4 tahapan Polya (Memahami Masalah, Merencanakan Solusi, Menjalankan Rencana/Debugging, Meninjau Ulang Hasil).
2. **Pengujian Kualitas Instrumen (Sugiyono Bab 6 & 7):**
   - **Uji Validitas Isi (*Content Validity*):** *Expert judgment* oleh guru pengampu dan dosen ahli.
   - **Uji Validitas Konstruk/Butir:** Korelasi *Product Moment Pearson* ($r_{\text{hitung}} > r_{\text{tabel}}$).
   - **Uji Reliabilitas:** Rumus *Cronbach's Alpha* ($\alpha \ge 0{,}70$).
   - **Uji Tingkat Kesukaran & Daya Pembeda Soal.**
