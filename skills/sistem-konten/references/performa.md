# Performa: verdict, diagnosis THS, dan review bulanan

## Kapan mengukur

Masukkan data setiap konten dua minggu setelah terbit, setelah angkanya relatif stabil. Kolom yang dicatat: tanggal, topik, funnel, format, link, views, likes, komen, share, save, tanggal evaluasi, dan pelajaran atau aksi berikutnya.

## Verdict

Rata-rata views dihitung dari semua konten yang sudah dicatat di platform yang sama. Save rate = save / views.

Cek berurutan, dan berhenti di kondisi pertama yang cocok:

1. **STOP:** views kurang dari 50% rata-rata. Jangan ulangi topik atau format ini tanpa perubahan besar.
2. **WINNING:** views di atas rata-rata dan save rate di atas 5%. Ulangi kombinasi topik, hook, dan formatnya.
3. **GOOD:** views di atas rata-rata. Layak dijadikan referensi.
4. **OPTIMASI:** sisanya, yaitu di bawah rata-rata tapi tidak terlalu jauh. Cek topik dan hook-nya.

Pakai `scripts/verdict.py` untuk menghitung dari file CSV, supaya hasilnya tidak salah hitung. Batas 50% dan 5% adalah aturan praktis dari toolkit, bukan standar industri. Kalau datanya kurang dari 10 konten, rata-ratanya belum stabil, jadi sampaikan bahwa verdict masih sementara. Satu konten viral bisa menaikkan rata-rata jauh di atas angka normal, sehingga konten lain ikut tampak STOP. Kalau ada konten dengan views lebih dari 5 kali median, sebutkan konten itu, lalu hitung ulang verdict tanpa konten tersebut sebagai pembanding. Sesuaikan juga dengan tujuan funnel: konten Sales dinilai dari klik dan pembelian, bukan dari views.

## Diagnosis THS

Untuk konten yang STOP atau OPTIMASI, cek berurutan:

1. **Topic:** apakah topiknya memang dicari audiens? Bandingkan dengan referensi FLSR dan pertanyaan di kepala audiens.
2. **Hook:** apakah 3 detik pertama atau slide 1 cukup kuat? Cek retensi di awal video kalau datanya ada.
3. **Style:** format, tempo, visual, audio, dan caption.

Perbaiki satu faktor saja dalam setiap percobaan, supaya hasilnya bisa dibaca.

## Analisis pola (minimal 10 konten, idealnya 20)

1. Pola konten yang menang: kesamaan topik, format, dan funnel.
2. Diagnosis konten yang gagal dengan THS, serta pola yang sebaiknya dihentikan.
3. Topik dengan save rate tertinggi (sinyal Authority) dan share rate tertinggi (sinyal Engagement).
4. Audit funnel: apakah komposisi Engagement, Authority, dan Sales sudah seimbang, dan apakah konten Sales menghasilkan klik atau malah membuat audiens pergi.
5. Rekomendasi: 3 jenis konten yang perlu diperbanyak, 2 yang perlu dikurangi, dan 1 eksperimen.

Jangan membuat prediksi angka pertumbuhan seolah-olah pasti. Kalau diminta, berikan sebagai rentang kasar dan sebutkan asumsinya.

## Analisis hook

Bandingkan hook dari konten yang berhasil dengan yang gagal: kata, struktur, emosi yang dipicu, dan panjang kalimatnya. Hasilnya berupa 5 sampai 7 aturan hook khusus untuk akun pengguna, ditambah hook untuk 5 konten berikutnya. Lakukan ini setiap bulan.

## Review bulanan

Lakukan di tanggal 1 atau 2 setiap bulan:

1. **Debrief:** apa yang berjalan sesuai harapan, apa yang tidak dan kenapa, serta satu insight terpenting.
2. **Pola:** topik, format, dan waktu posting yang paling berhasil.
3. **Strategi bulan depan:** komposisi funnel, 10 topik, format yang diprioritaskan, dan 1 eksperimen.
4. **Akselerasi:** 3 hal paling penting untuk mencapai target bulan depan.
5. **Red flag:** tanda bahaya yang perlu segera ditangani.

Masukkan 10 topik yang dihasilkan ke rencana bulan berikutnya.
