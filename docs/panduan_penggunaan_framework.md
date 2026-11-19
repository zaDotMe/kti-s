# Panduan Penggunaan Framework KTI-Agent Universal

Dokumen ini menjelaskan cara kerja dan cara menggunakan **KTI-Agent Universal Framework** untuk membantu siswa, mahasiswa, atau peneliti pemula menyusun Karya Tulis Ilmiah (KTI) / Skripsi dari awal (*from scratch*) dengan standar akademik tinggi dan pemahaman mandiri.

---

## 🎯 4 Pilar Utama Framework

1. **Topik Agnostik (Bisa untuk Siapa Saja):**
   Tidak terkunci pada satu judul atau sekolah tertentu. Framework dapat digunakan untuk bidang RPL, Rekayasa, IPA, IPS, Manajemen, Desain, dll.
2. **State Management Berkelanjutan (`research_profile.json`):**
   Semua variabel, populasi, instrumen, dan progres bab tersimpan di file profil terpusat. Jika pengguna berpindah perangkat atau memulai sesi baru, konteks penelitian tidak akan hilang.
3. **Socratic Mentoring & Defense Simulation:**
   Siswa tidak hanya menerima teks jadi, tetapi diedukasi melalui analogi bahasa awam dan simulasi pertanyaan sidang penguji di setiap akhir bab.
4. **Single Centralized Bibliography:**
   Daftar Pustaka **hanya ada satu** di paling akhir dokumen skripsi (setelah Bab V). Bab I, II, III, dan IV tidak memuat daftar pustaka terpisah.
5. **Kaidah Eksklusif Bab II (Sugiyono):**
   Di Bab II **hanya boleh ada SATU antara Hipotesis Penelitian ATAU Kerangka Berpikir** (dilarang keduanya sekaligus). Penelitian **Kuantitatif** (uji pengaruh/komparasi) wajib menggunakan **Hipotesis** (tanpa kerangka berpikir); penelitian **Kualitatif/Deskriptif** menggunakan **Kerangka Berpikir** (tanpa hipotesis).

---

## 🔄 Alur Penggunaan (User Journey)

### 1. Masuk Sesi (Onboarding)
Saat pengguna menyapa agen, sistem akan mengecek status penelitian:
- **Jika Melanjutkan Bab (misal langsung Bab 2 atau Bab 3):**
  Agen akan meminta file bab sebelumnya (`.docx`, `.pdf`, atau `.txt`) untuk diekstrak variabel X, Y, rumusan masalah, dan subjeknya ke dalam `research_profile.json`.
- **Jika Memulai dari Awal:**
  - *Sudah Punya Judul:* Agen melakukan **Stress-Test Judul** (cek Variabel X & Y, keterukuran indikator, dan kelayakan waktu/alat).
  - *Belum Punya Judul:* Agen menanyakan 4 pertanyaan pemantik (Lokasi, Keresahan/Masalah Nyata, Ide Solusi, dan Jenis KTI) lalu merumuskan 3 opsi judul baku.

### 2. Pengerjaan Bab demi Bab
- **Bab I (Pendahuluan):** Formula piramida terbalik 10 paragraf (kajian X, kajian Y, 3 jurnal relevan, dan perumusan judul).
- **Bab II (Kajian Teori):** 5 sub-poin per variabel (Pengertian, Ciri, Jenis, Fungsi, Manfaat) dengan minimal 3 ahli riil + sintesis penulis sendiri, serta perumusan hipotesis penelitian.
- **Bab III (Metodologi Penelitian):** Penentuan metode kuantitatif (Quasi-Eksperimen, PTK, R&D, dll.), kaidah sampel representatif 50% + 1, prosedur perlakuan, teknik analisis data (deskriptif, prasyarat, gain, inferensial), serta paket instrumen lengkap.
- **Bab IV (Hasil dan Pembahasan):** Uji statistik, tabel komparasi, interpretasi pedagogis, dan konfirmasi terhadap teori & studi terdahulu.
- **Bab V (Kesimpulan dan Saran):** Sinkronisasi kesimpulan dengan rumusan masalah, saran aplikatif, dan kompilasi satu Daftar Pustaka lengkap di akhir.

### 3. Simulasi Sidang Penguji
Setiap bab selesai di-generate ke file `.docx`, agen memandu simulasi 3–5 pertanyaan yang sering ditanyakan guru/dosen penguji beserta kunci jawaban cerdasnya.

---

## 🛠️ Perkakas Otomasi Python (Tools)

- `templates/universal_docx_generator.py`: Generator dokumen Word baku (A4, 4-3-3-3 cm, Times New Roman, 1.5 spasi, XML numbering reset).
- `templates/kti_profile_manager.py`: Modul CLI untuk menguji judul (`stress-test`) dan membaca dokumen bab sebelumnya (`ingest`).

Contoh perintah terminal:
```bash
# Melakukan stress-test judul baru
python templates/kti_profile_manager.py stress-test "Pengaruh Media Pembelajaran Interaktif terhadap Hasil Belajar Siswa"

# Membaca file bab sebelumnya untuk diekstrak konteksnya
python templates/kti_profile_manager.py ingest "draf/Bab1_Pendahuluan.docx"
```
