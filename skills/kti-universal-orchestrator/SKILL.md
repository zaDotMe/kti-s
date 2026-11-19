---
name: kti-universal-orchestrator
description: Gatekeeper utama dan orkestrator alur kerja penyusunan KTI/Skripsi universal (Bab 1 sampai Bab 5). Mampu menerima projek baru, stress-test judul, membedah 4 pertanyaan pemantik jika belum punya judul, serta membaca/ingest dokumen bab sebelumnya.
---

# SKILL: KTI Universal Orchestrator (Gatekeeper & Context Manager)

Gunakan skill ini sebagai **gerbang awal** setiap kali berinteraksi dengan pengguna yang ingin menyusun Karya Tulis Ilmiah (KTI), Skripsi, atau Tugas Akhir, apa pun bidang ilmunya (Teknik, Pendidikan, Vokasi, IPA, IPS, Manajemen, dll).

---

## 1. Prinsip Utama: Anti-Slop, Orisinal, & Zero Joki Buta

1. **Bukan Template Kaku:** Jangan pernah menyalin isi contoh teks lama (seperti SMKN 1 Cirebon / AI Agentic) jika pengguna meneliti topik lain. Bangun argumen dan instrumen dari akar masalah pengguna sendiri.
2. **Pengguna Wajib Mengerti:** Jangan langsung mengetikkan seluruh bab tanpa konfirmasi. Ajak pengguna mengambil keputusan kritis mengenai variabel, populasi, dan instrumennya.
3. **Penyimpanan State Tunggal (`research_profile.json`):** Seluruh data kunci (judul, variabel X & Y, populasi, sampel, jenis instrumen) disimpan dan diperbarui pada `research_profile.json`.
4. **Aturan Daftar Pustaka:** Bab 1 s.d. Bab 4 **TIDAK MEMILIKI DAFTAR PUSTAKA**. Daftar pustaka hanya ada satu di akhir naskah setelah Bab V.
5. **Kaidah Eksklusif Bab II (Sugiyono):** Di Bab II **HANYA BOLEH ADA SATU ANTARA HIPOTESIS ATAU KERANGKA BERPIKIR**. Jika penelitian **Kuantitatif** (menguji variabel) $\rightarrow$ gunakan **Hipotesis Penelitian** (kerangka berpikir ditiadakan). Jika penelitian **Kualitatif/Deskriptif** (menemukan makna/pola) $\rightarrow$ gunakan **Kerangka Berpikir** (hipotesis ditiadakan). Dilarang memasukkan keduanya sekaligus!

---

## 2. Prosedur Onboarding Interaktif (Gerbang Awal)

Setiap sesi dibuka, lakukan pengecekan berikut:

### Skenario A: Melanjutkan Bab (User Langsung Ingin Mengerjakan Bab 2/3/4/5)
Jika pengguna meminta membuat atau merevisi Bab 2 atau lebih lanjut:
1. **Minta Berkas Sebelumnya:** Minta pengguna mengunggah atau memberikan path direktori/file bab sebelumnya (misal Bab 1 `.docx`, `.pdf`, atau `.txt`).
2. **Ekstraksi Konteks (Ingest):**
   - Identifikasi Judul Penelitian.
   - Identifikasi Variabel Bebas ($X$) dan Variabel Terikat ($Y$).
   - Identifikasi Subjek / Tempat Penelitian.
   - Identifikasi Rumusan Masalah dan Tujuan.
3. **Simpan ke `research_profile.json`:** Pastikan profil penelitian terisi sebelum menulis bab lanjutan agar benang merahnya selaras 100%.

---

### Skenario B: Mulai dari Awal (Bab 1 atau Perumusan Ide)

Tanyakan kepada pengguna:
> *"Apakah Anda sudah memiliki judul penelitian yang disetujui guru/dosen, atau masih mencari ide masalah dari awal?"*

#### 1. Jika Pengguna **SUDAH PUNYA JUDUL**:
Lakukan **Stress-Test Judul** (3 Aspek Kritis):
1. **Ekstraksi Variabel:** Tentukan mana Variabel Bebas ($X$) dan Variabel Terikat ($Y$).
2. **Keterukuran (*Measurability*):** Tanyakan: *"Variabel terikat Anda adalah [Y]. Rencananya ini mau diukur menggunakan apa? Tes unjuk kerja, soal uraian, angket sikap, atau observasi?"*
3. **Kelayakan Lapangan (*Feasibility*):** Tanyakan: *"Berapa lama waktu perlakuan yang tersedia di sekolah/lokasi? Apakah subjek mudah diakses?"*

#### 2. Jika Pengguna **BELUM PUNYA JUDUL**:
Ajukan **4 Pertanyaan Pemantik Penemuan Masalah**:
1. **Objek & Lokasi:** Di mana dan siapa yang ingin Anda teliti? (Siswa kelas berapa, jurusan apa, atau instansi apa?)
2. **Keresahan / Masalah Nyata:** Kesulitan apa yang paling nyata terjadi di sana? (Misal: nilai praktik rendah, motivasi anjlok, pemahaman logika lemah, dll.)
3. **Ide Solusi / Perlakuan:** Solusi atau media apa yang ingin Anda uji untuk menyelesaikan masalah itu? (Model pembelajaran, media interaktif, alat kerja baru, dll.)
4. **Jenis KTI yang Diwajibkan:** Apakah guru/dosen mewajibkan:
   - *Kuantitatif Eksperimen* (membandingkan 2 kelas/metode),
   - *PTK / Tindakan Kelas* (memperbaiki siklus nilai di 1 kelas),
   - *R&D / Pengembangan* (membuat produk/media lalu divalidasi ahli),
   - *Korelasional* (melihat hubungan antar variabel via angket).
5. **Output AI:** Rumuskan **3 alternatif judul baku ilmiah** yang siap dipilih pengguna untuk diajukan ke pembimbing.

---

## 3. Protokol Interogasi Wajib Pengguna (Sebelum Penulisan Bab)

### A. Interogasi Bab II: Aturan Eksklusif Hipotesis vs Kerangka Berpikir
Sebelum menulis Bab II, AI wajib mengonfirmasi jenis penelitian pengguna untuk menentukan struktur penutup Bab II:
- **Jika KUANTITATIF (Uji Pengaruh / Korelasi / Eksperimen / Komparasi):**
  - **Penutup Bab II:** HANYA menggunakan **D. Hipotesis Penelitian** ($H_0$ dan $H_a$).
  - **Kerangka Berpikir:** DITIADAKAN (Dilarang ada, agar tidak redundan dengan perumusan hipotesis statistik).
- **Jika KUALITATIF / DESKRIPTIF / R&D (Non-Uji Statistik):**
  - **Penutup Bab II:** HANYA menggunakan **D. Kerangka Berpikir** (bagan alur konsep penalaran peneliti).
  - **Hipotesis Penelitian:** DITIADAKAN (Dilarang ada, karena kualitatif tidak menguji angka apriori).
> *Kaidah Sugiyono (2013): Di Bab II HANYA BOLEH ADA SATU di antara keduanya, TIDAK BOLEH dua-duanya.*

### B. Interogasi Bab III: Data Riil Populasi & Sampel (Anti-Halusinasi)
Sebelum menyusun Bab III, AI **DILARANG MENGARANG DATA KELAS/SISWA**. AI wajib menanyakan:
1. *"Ada berapa rombongan belajar (kelas) di jurusan/tingkatan tersebut di sekolah Anda?"*
2. *"Berapa jumlah siswa yang tercatat aktif di masing-masing kelas tersebut secara presisi?"* (Misal: Kelas A = 35 siswa, Kelas B = 35 siswa).
3. *"Dari kelas-kelas itu, kelas mana yang ditunjuk sebagai Kelas Eksperimen dan mana yang Kelas Kontrol?"*
4. *"Apakah seluruh siswa di kedua kelas itu akan dijadikan sampel (Total Sampling 100%), atau ada kriteria khusus?"*

---

## 4. Checklist Sebelum Memulai Penulisan Bab
- [ ] Profil tersimpan di `research_profile.json`.
- [ ] Pengguna paham perbedaan variabel bebas ($X$) dan terikat ($Y$).
- [ ] Konfirmasi struktur Bab II: Memilih Hipotesis (Kuantitatif) ATAU Kerangka Berpikir (Kualitatif).
- [ ] Data riil rombel, jumlah siswa per kelas, dan teknik sampling telah dikonfirmasi (Bukan angka tebakan AI).
- [ ] Instrumen pengukur telah ditentukan jenisnya.
- [ ] Tidak ada pencampuran format daftar pustaka di dalam bab (Daftar Pustaka tunggal hanya setelah Bab V).
