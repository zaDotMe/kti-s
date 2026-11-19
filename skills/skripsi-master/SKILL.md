---
name: skripsi-master
description: Orchestrator utama untuk memandu, memvalidasi, dan menyusun skripsi Bab 1 sampai Bab 5 secara konsisten, bebas halusinasi, dan sesuai metodologi Sugiyono.
---

# SKILL: Skripsi Master Orchestrator

Gunakan skill ini sebagai pemandu utama dalam seluruh proses penyusunan dan peninjauan draf skripsi (Bab 1 - Bab 5).

## Prinsip Pokok
1. **Zero Hallucination:** Dilarang mengarang kutipan, nama ahli, tahun, judul jurnal, atau hasil penelitian. Sumber harus riil dan diverifikasi dari berkas lokal atau literatur resmi.
2. **Kepatuhan Rujukan Utama:**
   - Bab 1 & Bab 2: Mengikuti draf acc pemilik (`Skripsi_Bab1_AI_Agentic_SMKN1Cirebon_ACC.docx` & `Skripsi_Bab2_AI_Agentic_SMKN1Cirebon_ACC_EXACT.docx`).
   - Metodologi Analisis: Mengacu langsung pada buku Prof. Dr. Sugiyono (*Metode Penelitian Kuantitatif, Kualitatif, dan R&D*).
3. **Format Layout Baku:**
   - Kertas A4 (21 x 29.7 cm), margin Top 4 cm, Left 3 cm, Bottom 3 cm, Right 3 cm.
   - Font Times New Roman 12 pt, 1.5 spasi, rata Justify, First Line Indent 1.27 cm.
   - Seluruh istilah non-KBBI dicetak miring (*italic*).
   - Penomoran butir menggunakan Word List Numbering (reset di setiap sub-bagian).
4. **Aturan Letak Daftar Pustaka:**
   - Daftar Pustaka HANYA ADA SATU dan diletakkan di akhir keseluruhan skripsi (setelah Bab V Kesimpulan dan Saran).
   - Dilarang keras menaruh bagian "DAFTAR PUSTAKA" di akhir Bab I, Bab II, maupun Bab III.

## Peta Kerja Bab (Roadmap)
- **Bab 1:** [[skills/bab1-pendahuluan/SKILL.md]] -> Pola 10 paragraf latar belakang, rumusan, tujuan, manfaat.
- **Bab 2:** [[skills/bab2-kajian-teori/SKILL.md]] -> Teori 3 variabel/fokus (5 sub-poin per variabel) + D. Hipotesis Penelitian (tanpa kerangka berpikir jika diminta khusus).
- **Bab 3:** [[skills/bab3-metodologi-penelitian/SKILL.md]] -> Struktur A-F sesuai permintaan pengguna (Metode, Desain Kuasi-Eksperimen, Populasi-Sampel 50%+1, Teknik Penelitian, Analisis Data, Instrumen).
- **Bab 4:** [[skills/bab4-hasil-dan-pembahasan/SKILL.md]] -> Deskripsi data pretest/posttest, uji prasyarat (normalitas, homogenitas), uji hipotesis (t-test/N-gain), pembahasan komparatif.
- **Bab 5:** [[skills/bab5-kesimpulan-dan-saran/SKILL.md]] -> Sinkronisasi simpul jawaban rumusan masalah dan saran tindak lanjut praktis/teoretis.
