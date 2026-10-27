#!/usr/bin/env python3
"""Analisis rekaman latihan bicara.

Pakai: python3 -I analyze_speech.py <file audio/video> [--transcript file.txt] [--out hasil.json]

Mengukur: durasi, kata per menit (WPM), jumlah & sebaran jeda (silence >= 0.4 dtk),
variasi volume per detik, filler words Indonesia/Inggris, dan kalimat terpanjang.
Transkrip diambil dengan `bb voice transcribe` kecuali --transcript diberikan.
Butuh: ffmpeg di PATH.
"""
import json, math, re, subprocess, sys, os, statistics, tempfile

FILLERS = {
    # bunyi (non-words)
    "eee": r"\be+h*m*\b|\bem+\b|\behm+\b|\bum+\b|\buh+\b|\bhmm+\b",
    # filler words Indonesia
    "anu": r"\banu\b",
    "apa namanya": r"\bapa (ya )?namanya\b",
    "kayak": r"\bkayak\b|\bkaya\b",
    "gitu": r"\bgitu( loh| lho)?\b|\bbegitu\b",
    "istilahnya": r"\bistilahnya\b",
    "nah": r"\bnah\b",
    "terus": r"\bterus\b|\btrus\b",
    "ya kan": r"\bya kan\b|\bkan\b",
    "sebenarnya": r"\bsebenarnya\b|\bsebenernya\b",
    # filler words Inggris
    "like": r"\blike\b",
    "you know": r"\byou know\b",
    "basically/literally/actually": r"\bbasically\b|\bliterally\b|\bactually\b",
    "so": r"^so\b|(?<=[.!?] )so\b",
}

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def duration(path):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]).stdout.strip()
    return float(out)

def silences(path, noise="-35dB", d=0.4):
    err = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", f"silencedetect=noise={noise}:d={d}", "-f", "null", "-"]).stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", err)]
    lens = [float(x) for x in re.findall(r"silence_duration: ([\d.]+)", err)]
    return list(zip(starts, lens))

def loudness_per_second(path):
    err = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af",
               "asetnsamples=n=16000,astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level",
               "-ar", "16000", "-ac", "1", "-f", "null", "-"]).stderr
    vals = [float(x) for x in re.findall(r"RMS_level=(-?[\d.]+)", err)]
    return [v for v in vals if v > -50]  # buang detik yang hening

def transcribe(path):
    tmp = tempfile.mkdtemp()
    mp3 = os.path.join(tmp, "a.mp3")
    run(["ffmpeg", "-loglevel", "error", "-y", "-i", path, "-vn", "-ac", "1", "-ar", "16000", "-b:a", "32k", mp3])
    r = run(["bb", "voice", "transcribe", "--json", "--type", "audio/mpeg",
             "--prompt", "Latihan bicara. Tulis semua bunyi ragu seperti eee, emm, anu apa adanya.", mp3])
    try:
        return json.loads(r.stdout)["text"]
    except Exception:
        sys.exit(f"Transkripsi gagal: {r.stderr or r.stdout}")

def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    path = a[0]
    tx = open(a[a.index("--transcript") + 1]).read() if "--transcript" in a else transcribe(path)
    out = a[a.index("--out") + 1] if "--out" in a else None

    dur = duration(path)
    sil = silences(path)
    inner = [s for s in sil if s[0] > 0.5 and s[0] + s[1] < dur - 0.5]
    speak_time = max(dur - sum(l for _, l in sil), 1)
    words = re.findall(r"[\w'-]+", tx.lower())
    low = tx.lower()
    fillers = {k: len(re.findall(p, low, re.M)) for k, p in FILLERS.items()}
    fillers = {k: v for k, v in fillers.items() if v}
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", tx) if s.strip()]
    longest = max(sentences, key=lambda s: len(s.split()), default="")
    rms = loudness_per_second(path)

    res = {
        "file": path,
        "durasi_detik": round(dur, 1),
        "jumlah_kata": len(words),
        "wpm_total": round(len(words) / dur * 60),
        "wpm_saat_bicara": round(len(words) / speak_time * 60),
        "jeda": {
            "jumlah_>=0.4s": len(inner),
            "jumlah_>=1s": sum(1 for _, l in inner if l >= 1),
            "jumlah_>=2s": sum(1 for _, l in inner if l >= 2),
            "per_menit": round(len(inner) / dur * 60, 1),
            "terpanjang_detik": round(max((l for _, l in inner), default=0), 1),
        },
        "volume_db": {
            "rata_rata": round(statistics.mean(rms), 1) if rms else None,
            "variasi_stdev": round(statistics.pstdev(rms), 1) if len(rms) > 1 else None,
            "rentang_p10_p90": [round(sorted(rms)[int(len(rms) * .1)], 1), round(sorted(rms)[int(len(rms) * .9) - 1], 1)] if len(rms) > 9 else None,
        },
        "filler": fillers,
        "filler_per_menit": round(sum(fillers.values()) / dur * 60, 1),
        "kalimat": {"jumlah": len(sentences), "terpanjang_kata": len(longest.split()), "terpanjang": longest[:300]},
        "transkrip": tx,
        "catatan": "Transkripsi otomatis sering menghapus bunyi 'eee/emm', jadi hitungan filler bisa lebih rendah dari aslinya. Dengarkan rekamannya untuk memastikan.",
    }
    s = json.dumps(res, ensure_ascii=False, indent=1)
    if out: open(out, "w").write(s)
    print(s)

if __name__ == "__main__":
    main()
