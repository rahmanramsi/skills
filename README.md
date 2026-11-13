# Skills

Kumpulan skill untuk agent AI seperti Claude Code, Codex, dan agent lain yang membaca format `SKILL.md`.

## Pasang

```bash
npx skills@latest add rahmanramsi/skills
```

Untuk memasang satu skill saja:

```bash
npx skills@latest add rahmanramsi/skills --skill best-practices
```

Kalau kamu tidak terbiasa memakai terminal, tempel perintah ini ke agent AI-mu, misalnya Codex atau Claude Code:

```text
Pasang skill best-practices dengan menjalankan perintah ini di terminal: npx skills@latest add rahmanramsi/skills --skill best-practices -g -y. Setelah selesai, beri tahu aku apakah skill-nya sudah terpasang.
```

## Daftar skill

- **[best-practices](./skills/best-practices/SKILL.md)**: mencari dan menilai praktik kerja terbaik untuk tugasmu, lengkap dengan sumber, kekuatan bukti, dan cara mengujinya.
- **[communication](./skills/communication/SKILL.md)**: menulis dan memperbaiki script komunikasi lisan, seperti presentasi, pitch, video konten, dan sambutan, lengkap dengan cue cara mengucapkannya.
- **[sistem-konten](./skills/sistem-konten/SKILL.md)**: sistem membuat konten media sosial dari niche dan audiens, rencana dengan content funnel, riset referensi, script Hook-Tension-Payoff-Call to value, sampai verdict performa. Alurnya diadaptasi dari The Ultimate Content Creation Toolkit karya [Bukan Cuma Posting](https://bukancumaposting.com).

## Skill `communication`

### Cara pakai

Panggil dengan `/communication`, atau cukup minta dengan bahasa biasa. Skill akan terpicu sendiri:

```
/communication buatkan script video LinkedIn 60 detik tentang pentingnya 1-on-1
/communication rapikan naskah presentasi ini biar enak diucapkan: <tempel naskah>
/communication ubah presentasi 10 menit ini jadi pitch 3 menit
/communication tandai naskah ini dengan cue delivery, jangan ubah teksnya
/communication bantu bikin cerita pembuka dari pengalaman saya waktu …
```

### Yang dihasilkan

Setiap script keluar dalam format yang sama:

1. **Ringkasan:** format, audiens, tujuan/CTA, pesan inti, durasi, asumsi
2. **Peta struktur:** blok Connect → Why → What → How → Connect, dengan archetype dan durasinya
3. **Script versi bersih:** enak dibaca dan diucapkan
4. **Script versi bertanda:** teks yang sama dengan cue delivery
5. **Kartu pegangan:** kata kunci per blok untuk dibawa ke panggung atau ditempel di samping kamera
6. **Catatan:** jumlah kata dan estimasi durasi, placeholder yang harus diisi, bagian yang perlu dihafal

Notasi cue:

| Cue | Arti |
|---|---|
| `[R3]` … `[R7]` | kecepatan bicara (3 = lambat untuk menekankan, 7 = cepat) |
| `[V5]` … `[V8]` | volume 1–10 |
| `/` `//` `///` | jeda pendek, sedang, panjang |
| `↘` | akhiri kalimat dengan nada turun |
| `~melodi~` | perlebar variasi nada |
| `{sedih}` `{kaget}` … | emosi atau ekspresi wajah |
| `<Friend 3>` `<Coach 6>` … | vocal archetype dan intensitasnya |
| `↓↑` | transisi archetype: turunkan dulu, lalu naikkan |
| `[gestur: …]` `[pindah: …]` | cue tubuh dan gerak |

**Script tidak mengarang pengalaman pribadi.** Cerita, angka, kutipan, dan testimoni harus datang dari kamu. Kalau belum ada, skill memasang placeholder `[…]` untuk diisi.

### Menguji script

Rekam dirimu membaca script, lalu jalankan:

```bash
python3 -I ~/.claude/skills/communication/scripts/analyze_speech.py rekaman.m4a --out hasil.json
```

Skrip ini mengukur durasi, kata per menit, jumlah dan panjang jeda, variasi volume, filler words (Indonesia dan Inggris), serta kalimat terpanjang.

Kebutuhan:
- `ffmpeg`
- Python 3
- CLI `bb` untuk transkripsi (`bb voice transcribe`). Kalau sudah punya transkrip, pakai `--transcript file.txt` dan `bb` tidak dibutuhkan.

Catatan: transkripsi otomatis sering menghapus bunyi "eee/emm", jadi hitungan filler bisa lebih rendah dari aslinya.

### Struktur

```
skills/communication/
├── SKILL.md                         # alur kerja utama dan aturan
├── references/
│   ├── script-writing.md            # intake, anggaran kata, template per format, aturan menulis, checklist, contoh
│   ├── storytelling.md              # 4 chemicals, Incident → Point → Linking, memendekkan cerita, story library
│   ├── vocal-archetypes.md          # Friend / Motivator / Educator / Coach, intensitas, transisi
│   ├── vocal-mastery.md             # rate, volume, pitch & melodi, tonality, pause, notasi cue
│   ├── body-language.md             # postur, gestur, ekspresi, eye contact, gerak, panggung, virtual
│   ├── coaching-patterns.md         # anatomi keynote, pola diagnosis → koreksi, template feedback
│   ├── rehearsal-nerves-and-plan.md # 7-step rehearsal, mengatasi gugup, rencana 12 minggu
│   ├── foundations-and-laws.md      # mindset dan prinsip dasar
│   └── drills.md                    # katalog latihan
└── scripts/
    └── analyze_speech.py            # analisis rekaman pembacaan script
```

### Sumber

Kerangka di skill ini diringkas dan diparafrasekan dari kursus **STAGE Academy** karya **Vinh Giang** ([vinhgiang.com](https://www.vinhgiang.com)). Repo ini tidak berafiliasi dengan STAGE Academy, dan tidak berisi transkrip atau materi asli kursus. Untuk materi lengkapnya, ikuti kursusnya langsung.
