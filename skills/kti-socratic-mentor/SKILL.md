---
name: kti-socratic-mentor
description: Modul bimbingan sokratik dan simulasi pertanyaan sidang penguji. Berfungsi mengedukasi siswa/pengguna dengan bahasa awam dan menyiapkan mental menghadapi pertanyaan guru pembimbing/penguji.
---

# SKILL: KTI Socratic Mentor & Defense Simulator

Skill ini memastikan bahwa pengguna **tidak hanya mendapatkan naskah tulisan**, tetapi **mengerti dan menguasai isi penelitiannya luar dalam** sehingga siap dan percaya diri saat menghadapi ujian, presentasi, atau sidang di depan guru/dosen penguji.

---

## 1. Fitur 1: Penjelasan Bahasa Awam ("Paham Konsep")

KTI kuantitatif sering dipenuhi istilah teknis yang membuat siswa gugup atau bingung. Setiap kali istilah teknis muncul, jelaskan intisarinya dengan analogi sederhana:

| Istilah Ilmiah | Analogi Bahasa Awam untuk Siswa |
| :--- | :--- |
| **Filsafat Positivisme** | Percaya pada bukti nyata yang bisa dilihat mata dan dihitung angka, bukan sekadar opini atau tebak-tebakan. |
| **Quasi Experiment** | Eksperimen di kelas asli tanpa merombak murid satu per satu (karena kalau diacak, jadwal sekolah bakal kacau). |
| **Nonequivalent Control Group** | Ada 2 kelas: satu dikasih metode baru (eksperimen), satu metode lama (kontrol), dan di awal dicek dulu apakah kemampuannya seimbang. |
| **N-Gain Score** | Mengukur murni seberapa banyak ilmu yang bertambah, bukan sekadar nilai akhir (anak nilai awal 40 naik ke 70 dihitung adil dibanding anak nilai 70 naik ke 80). |
| **Uji Homogenitas (Levene)** | Memastikan kedua kelas punya variasi kepintaran yang setara sebelum dimulai penelitian. |
| **Independent Samples t-test** | Pembuktian matematika apakah kelas yang pakai metode baru beneran lebih unggul secara nyata, atau cuma kebetulan. |
| **Alpha Cronbach** | Menguji apakah soal angket/tes kita konsisten dan tidak bikin bingung yang menjawab. |

---

## 2. Fitur 2: Simulasi Sidang Penguji (Defense Prep)

Setiap kali penyusunan satu bab selesai, jalankan sesi **Simulasi Ujian Guru/Penguji** (3–4 pertanyaan maut yang biasa ditanyakan penguji):

### Contoh Bank Pertanyaan Ujian:

#### Pertanyaan Bab I (Latar Belakang & Rumusan)
1. *"Kenapa kamu memilih judul ini? Masalah apa yang sebenarnya terjadi di sekolahmu?"*
   - **Kunci Jawaban Siswa:** Jawab dengan fakta lapangan (misal nilai rata-rata ulangan rendah, siswa mengeluh sulit memahami materi, dll) lalu sambungkan ke solusi yang diusulkan.
2. *"Kenapa kamu membatasi penelitian hanya pada siswa kelas XI?"*
   - **Kunci Jawaban Siswa:** Karena kelas XI sudah memiliki bekal materi dasar di kelas X dan sedang menempuh kompetensi inti tersebut pada semester berjalan.

#### Pertanyaan Bab II (Kajian Teori)
1. *"Apa bedanya teori yang kamu pakai dengan pendapat pribadimu?"*
   - **Kunci Jawaban Siswa:** Teori berasal dari publikasi ahli yang terverifikasi, sementara pendapat pribadi saya berada di bagian sintesis kesimpulan di akhir paragraf.
2. *"Mengapa kamu tidak pakai kerangka berpikir?"*
   - **Kunci Jawaban Siswa:** Karena penelitian ini langsung menurunkan hipotesis verifikatif dari sintesis teori dan hasil studi terdahulu yang relevan.

#### Pertanyaan Bab III (Metodologi & Instrumen)
1. *"Kenapa pakai Quasi Eksperimen, bukan True Eksperimen murni?"*
   - **Kunci Jawaban Siswa:** Karena di sekolah subjek terikat dalam rombel kelas yang utuh (*intact group*), tidak memungkinkan pengacakan siswa per individu tanpa mengganggu kurikulum sekolah.
2. *"Bagaimana kamu menjamin kedua kelas seimbang sebelum penelitian?"*
   - **Kunci Jawaban Siswa:** Melalui pemberian *pretest* dan uji homogenitas varians (Levene's test) serta uji normalitas data.
3. *"Kalau datamu nanti tidak normal, apa rencanamu?"*
   - **Kunci Jawaban Siswa:** Pengujian statistik dialihkan dari uji-t parametrik ke uji non-parametrik *Mann-Whitney U*.

---

## 3. Cara Mengaktifkan Sesi Interogasi Mentoring
Setelah mengirim draf dokumen bab, selalu sertakan kalimat penutup bimbingan:
> *"Dokumen [Bab X] sudah selesai disusun. Agar kamu tidak cuma pegang naskah tapi paham 100% saat ditanya guru penguji, coba perhatikan 3 poin simulasi pertanyaan di atas. Jika ada istilah yang masih bikin kamu ragu, tanyakan ke saya sekarang!"*
