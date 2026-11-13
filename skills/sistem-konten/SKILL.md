---
name: sistem-konten
description: Sistem membuat konten media sosial dari fondasi sampai evaluasi, mencakup niche dan audiens, rencana mingguan dan bulanan dengan content funnel, riset referensi FLSR, brief dan script HTPC, hook, CTA atau CTV, caption, serta verdict performa. Pakai saat diminta merencanakan konten, mencari ide atau hook, menulis script atau caption, atau mengevaluasi performa konten.
example-prompt: Bikinin rencana konten minggu depan buat akun TikTok dan Instagram aku. Niche-nya AI untuk produktivitas kerja, audiensnya pemilik usaha kecil. Konten yang paling jalan minggu lalu soal prompting.
---

# Sistem konten

Bantu pengguna membuat konten secara terencana: tentukan arah, riset dulu, tulis dengan struktur yang jelas, lalu ukur hasilnya dan bawa pelajarannya ke putaran berikutnya.

Sistem ini diadaptasi dari The Ultimate Content Creation Toolkit karya Bukan Cuma Posting.

## Alur kerja

| Langkah | Kapan | Baca |
|---|---|---|
| 1. Niche, value, dan bio | Sekali di awal, tinjau tiap 3 sampai 6 bulan | [fondasi.md](references/fondasi.md) |
| 2. Profil audiens | Sekali di awal | [fondasi.md](references/fondasi.md) |
| 3. Rencana bulanan dan mingguan | Awal bulan dan awal minggu | [perencanaan.md](references/perencanaan.md) |
| 4. Riset referensi (FLSR) | Untuk setiap topik | [perencanaan.md](references/perencanaan.md) |
| 5. Brief, script HTPC, hook, dan caption | Untuk setiap konten | [brief-htpc.md](references/brief-htpc.md) |
| 6. Verdict dan diagnosis | Dua minggu setelah terbit | [performa.md](references/performa.md) |
| 7. Review bulanan | Tanggal 1 atau 2 setiap bulan | [performa.md](references/performa.md) |

Mulai dari langkah yang diminta pengguna. Jangan memaksa pengguna mengulang dari langkah 1. Kalau sebuah langkah butuh hasil dari langkah sebelumnya, misalnya persona atau niche, cari dulu di percakapan atau file pengguna. Kalau tetap tidak ada, tanyakan hanya bagian yang benar-benar mengubah hasil.

## Ide, hook, dan penutup

Buat hook dari 6 kategori: Negativity (takut, rugi, menyesal), Curiosity (rasa penasaran), Controversy (melawan anggapan umum yang bisa dipertanggungjawabkan), List/Number (angka spesifik), FOMO (takut tertinggal), dan Authority (kredibilitas dari bukti nyata). Tawarkan 3 sampai 5 pilihan dari kategori yang berbeda, lalu sarankan satu.

Untuk penutup, utamakan CTV (call to value): tawarkan nilai, misalnya "simpan ini untuk dipakai saat ...". Kurangi CTA yang hanya meminta tindakan, seperti "like dan follow".

Kalau pengguna punya bank hook, ide, atau penutup sendiri, pakai itu lebih dulu dan ganti setiap bagian [dalam kurung] dengan topik, audiens, dan pengalamannya.

## Aturan yang wajib diikuti

- **Jangan mengarang bukti.** Hook Authority, testimoni, kelangkaan slot, garansi, atau angka hasil hanya boleh dipakai kalau pengguna punya buktinya. Kalau belum ada, ganti dengan hook dari kategori lain, atau tulis angka sebagai target dan sebut jelas bahwa itu target.
- **Gaya bahasa mengikuti pengguna.** Ikuti sapaan, campuran bahasa, dan nada sesuai cara bicara pengguna dan aturan gaya tulis yang dia punya.
- **FLSR meniru pola, bukan isi.** Jangan menyalin kalimat, visual, atau cerita dari konten referensi.
- **Riset butuh sumber.** Untuk tren, kompetitor, atau data pasar, pakai pencarian web kalau tersedia, lalu sertakan link-nya. Kalau tidak tersedia, sampaikan bahwa jawabannya berasal dari pengetahuan umum yang belum dicek.
- **Verdict dihitung, bukan ditebak.** Pakai `scripts/verdict.py` saat datanya lebih dari beberapa baris.
- **Skill ini tidak memberi izin untuk memposting,** menjadwalkan, atau mengirim pesan. Serahkan hasilnya ke pengguna, kecuali dia meminta langkah itu secara eksplisit.

## Menghitung verdict

Siapkan CSV dengan kolom `topik`, `views`, dan `save`. Tambahkan kolom `platform` kalau datanya campuran, supaya rata-rata dihitung per platform. Lalu jalankan:

```bash
python3 scripts/verdict.py data.csv
```

Hasilnya berisi rata-rata views, save rate, dan verdict untuk setiap konten. Setelah itu, lakukan diagnosis THS untuk konten yang STOP atau OPTIMASI.

## Memeriksa hasil

Sebelum menyerahkan hasil, cek:

- Setiap konten punya lapisan funnel, hook, dan call to value yang sesuai dengan funnel-nya.
- Komposisi rencana masuk akal untuk waktu produksi pengguna.
- Tidak ada angka, testimoni, atau klaim yang tidak bisa dibuktikan pengguna.
- Bahasa terdengar seperti pengguna, bukan seperti template.
