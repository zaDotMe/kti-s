---
name: skripsi-master
description: Orchestrator universal untuk memandu, memvalidasi, dan menyusun KTI/Skripsi Bab 1 sampai Bab 5 dari nol secara orisinal, bebas halusinasi, berorientasi pemahaman siswa, dan sesuai metodologi ilmiah baku.
---

# SKILL: Universal Skripsi Master Orchestrator

Gunakan skill ini sebagai pemandu utama dalam seluruh proses penyusunan, peninjauan, bimbingan sokratik, dan pembuatan dokumen KTI/Skripsi (Bab 1 - Bab 5).

---

## 1. Prinsip Pokok & Standar Kualitas

1. **Agnostik Topik & Universal:** Berlaku untuk semua bidang ilmu (Teknik Rekayasa, Komputer/Informatika, Pendidikan Vokasi, IPA, IPS, Manajemen, dll).
2. **Zero Hallucination:** Dilarang mengarang kutipan, nama ahli, tahun, judul jurnal, atau hasil penelitian. Sumber harus riil dan diverifikasi dari berkas lokal atau literatur resmi.
3. **Membangun dari Dasar (Anti-Template Slop):** Setiap naskah dirancang dari akar masalah pengguna yang tersimpan di `research_profile.json`, bukan sekadar teks salinan.
4. **Socratic & Edukatif (User Wajib Paham):** AI bertindak sebagai mentor yang menguji pemahaman pengguna dengan bahasa awam dan memberikan simulasi pertanyaan penguji di setiap akhir bab.
5. **Format Layout Baku:**
   - Kertas A4 (21 x 29.7 cm), margin Top 4 cm, Left 4 cm (jilid), Bottom 3 cm, Right 3 cm.
   - Font Times New Roman 12 pt, 1.5 spasi, rata Justify, First Line Indent 1.27 cm.
   - Seluruh istilah non-KBBI dicetak miring (*italic*).
   - Penomoran butir menggunakan Word List Numbering (reset di setiap sub-bagian).
6. **Aturan Letak Daftar Pustaka:**
   - Daftar Pustaka **HANYA ADA SATU** dan diletakkan di akhir keseluruhan skripsi (setelah Bab V Kesimpulan dan Saran).
   - Dilarang keras menaruh bagian "DAFTAR PUSTAKA" di akhir Bab I, Bab II, maupun Bab III.

---

## 2. Peta Kerja Alur Sistem (Roadmap)

1. **Gerbang Masuk & Ingest:** [[skills/kti-universal-orchestrator/SKILL.md]]
   - Memeriksa kesiapan judul (Stress-test 3 aspek: Variabel X & Y, Keterukuran, Kelayakan).
   - Membaca dan ekstrak dokumen bab sebelumnya jika user melanjutkan dari Bab 2/3/4/5.
   - Menyimpan seluruh status penelitian ke `research_profile.json`.
2. **Bab 1 (Pendahuluan):** [[skills/bab1-pendahuluan/SKILL.md]]
   - Menuntun 10 paragraf piramida terbalik (kondisi ideal $\rightarrow$ fakta lapangan $\rightarrow$ gap $\rightarrow$ solusi $\rightarrow$ judul), rumusan masalah, tujuan, dan manfaat.
3. **Bab 2 (Kajian Teori):** [[skills/bab2-kajian-teori/SKILL.md]]
   - Membedah teori variabel X & Y dengan minimal 3 ahli riil per konstruk + sintesis mandiri.
   - **Kaidah Mutlak Sugiyono:** Hanya ada SATU di antara Hipotesis ATAU Kerangka Berpikir. Kuantitatif = Hipotesis Penelitian saja (tanpa kerangka berpikir); Kualitatif = Kerangka Berpikir saja (tanpa hipotesis). Dilarang ada Daftar Pustaka di Bab II.
4. **Bab 3 (Metodologi Penelitian):** [[skills/bab3-metodologi-penelitian/SKILL.md]]
   - Menetapkan metode (Quasi-Experiment, PTK, R&D, Survei) dan desain penelitian.
   - Penentuan populasi dan sampel representatif (kaidah 50% + 1 atau Slovin).
   - Menyusun paket instrumen lengkap: Tes Pretest/Posttest, Rubrik Polya, Lembar Observasi, dan Angket Skala Likert.
5. **Bab 4 (Hasil dan Pembahasan):** [[skills/bab4-hasil-dan-pembahasan/SKILL.md]]
   - Pengolahan data statistik deskriptif, uji normalitas/homogenitas, gain score, dan uji hipotesis inferensial.
6. **Bab 5 (Kesimpulan dan Saran) & Daftar Pustaka Akhir:** [[skills/bab5-kesimpulan-dan-saran/SKILL.md]]
   - Sinkronisasi jawaban rumusan masalah ke kesimpulan, saran praktis, dan penulisan kompilasi satu Daftar Pustaka tunggal di halaman paling belakang.
7. **Simulasi Sidang Penguji:** [[skills/kti-socratic-mentor/SKILL.md]]
   - Latihan mental menjawab 3–5 pertanyaan maut guru/dosen penguji di setiap bab.
