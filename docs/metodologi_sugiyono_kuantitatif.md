# Bedah Metodologi Penelitian Kuantitatif (Berdasarkan Prof. Dr. Sugiyono)

Rujukan Utama: **Prof. Dr. Sugiyono (2013), *Metode Penelitian Kuantitatif, Kualitatif, dan R&D*, Bandung: Alfabeta.**

---

## 1. Landasan Filsafat & Karakteristik (Sugiyono Bab 1)
- **Filsafat Positivisme:** Realitas dipandang konkret, teramati, terukur, dapat diklasifikasikan, dan gejala memiliki relasi sebab-akibat (kausalitas).
- **Proses Berpikir Deduktif:** Masalah dirumuskan $\rightarrow$ ditelaah melalui teori-teori mapan $\rightarrow$ dirumuskan hipotesis $\rightarrow$ diuji secara empiris dengan instrumen baku di lapangan.

---

## 2. Paradigma Hubungan Variabel (Sugiyono Bab 2)
Penelitian ini mengadopsi **Paradigma Sederhana (Hubungan Kausal Bivariat)**:
$$\boxed{X \longrightarrow Y}$$

1. **Variabel Independen / Bebas ($X$):**
   - *Penggunaan Alur Kerja AI Agentic*
   - Karakteristik: intervensi pembelajaran dengan agen cerdas otonom yang melibatkan siklus *goal planning*, *code execution*, dan *self-debugging reflection*.
2. **Variabel Dependen / Terikat ($Y$):**
   - *Kemampuan Problem Solving Siswa*
   - Indikator acuan 4 tahap George Polya:
     1. Memahami masalah (*understanding the problem*)
     2. Merencanakan penyelesaian (*devising a plan*)
     3. Melaksanakan rencana (*carrying out the plan*)
     4. Memeriksa kembali (*looking back*)

---

## 3. Desain Eksperimen (Sugiyono Bab 4, Halaman 72–79)
- **Jenis:** *Quasi-Experimental Design* (Eksperimen Semu).
- **Alasan Pemilihan:** Di lingkungan sekolah (SMKN 1 Cirebon), siswa terikat dalam rombongan belajar (rombel) tetap, sehingga pengacakan individu secara murni (*pure random assignment*) tidak memungkinkan tanpa mengganggu proses belajar-mengajar sekolah.
- **Model Desain:** **Nonequivalent Control Group Design**.

### Pola Paradigma Desain:
$$\begin{array}{lccc}
\text{Kelompok Eksperimen} & O_1 & X & O_2 \\
\hline
\text{Kelompok Kontrol} & O_3 & - & O_4
\end{array}$$

**Keterangan:**
- $O_1$ = Tes awal (*pretest*) kemampuan *problem solving* kelompok eksperimen.
- $O_3$ = Tes awal (*pretest*) kemampuan *problem solving* kelompok kontrol.
- $X$ = Perlakuan pembelajaran menggunakan alur kerja *AI agentic*.
- $-$ = Pembelajaran menggunakan pendekatan konvensional (tanpa *AI agentic*).
- $O_2$ = Tes akhir (*posttest*) kelompok eksperimen.
- $O_4$ = Tes akhir (*posttest*) kelompok kontrol.
- Besarnya pengaruh perlakuan dihitung melalui selisih peningkatan skor: $(O_2 - O_1) - (O_4 - O_3)$ atau melalui uji perbedaan rata-rata *N-Gain*.

---

## 4. Populasi dan Sampling (Sugiyono Bab 5, Halaman 80–91)
- **Populasi Target:** Seluruh siswa kelas XI Konsentrasi Keahlian Rekayasa Perangkat Lunak (RPL) SMKN 1 Cirebon tahun ajaran berjalan.
- **Teknik Sampling:** *Purposive Sampling* atau *Cluster Random Sampling* (memilih 2 kelas rombel yang memiliki kesetaraan kemampuan awal/homogen).

---

## 5. Instrumen & Uji Kualitas (Sugiyono Bab 6 & 7)
1. **Instrumen Pengukuran:**
   - Tes kinerja/uraian *problem solving* pemrograman berbasis studi kasus (misal: analisis kebutuhan modul, perancangan basis data, implementasi backend API, dan pelacakan *bug*).
   - Rubrik penilaian analitik berbasis indikator Polya (skor 1–4 per indikator).
2. **Uji Validitas:**
   - *Content Validity* (Validitas Isi): Penilaian oleh pakar (*expert judgment* oleh guru senior dan dosen ahli).
   - *Construct Validity* (Validitas Konstruk): Uji korelasi *Product Moment Pearson* pada setiap butir soal.
3. **Uji Reliabilitas:**
   - Uji konsistensi internal menggunakan rumus *Cronbach's Alpha* (nilai $\alpha \ge 0{,}70$ dikategorikan reliabel).

---

## 6. Teknik Analisis Data & Pengujian Hipotesis (Sugiyono Bab 8 & 9)
1. **Statistik Deskriptif:**
   - Menghitung mean, median, modus, varians, standar deviasi, dan tabel distribusi frekuensi skor *pretest* dan *posttest*.
2. **Uji Prasyarat Analisis:**
   - **Uji Normalitas:** Menguji sebaran data kelompok (uji *Shapiro-Wilk* atau *Kolmogorov-Smirnov* dengan signifikansi $\alpha = 0{,}05$).
   - **Uji Homogenitas:** Menguji kesamaan varians kelompok (uji *Levene's Test* dengan signifikansi $\alpha = 0{,}05$).
3. **Uji Hipotesis (Inferensial):**
   - **Jika data berdistribusi normal dan homogen:** Menggunakan **Independent Samples t-test** pada skor gain ternormalisasi (*Normalized Gain / N-Gain*).
   - **Jika data tidak berdistribusi normal:** Menggunakan uji non-parametrik **Mann-Whitney U Test**.
4. **Kriteria Pengambilan Keputusan:**
   - Jika nilai $\text{Sig. (2-tailed)} < 0{,}05$, maka $H_0$ ditolak dan $H_a$ diterima (Terdapat pengaruh yang signifikan).
   - Jika nilai $\text{Sig. (2-tailed)} \ge 0{,}05$, maka $H_0$ diterima dan $H_a$ ditolak.
