"""Hitung save rate dan verdict konten dari file CSV.

Kolom wajib: topik, views, save. Kolom platform bersifat opsional; kalau ada,
rata-rata views dihitung per platform.

Pemakaian: python3 verdict.py data.csv
"""

import csv
import sys
from collections import defaultdict

STOP_RATIO = 0.5
WINNING_SAVE_RATE = 0.05


def to_number(value):
    text = str(value or "").strip()
    if not text:
        return 0.0
    try:
        return float(text)
    except ValueError:
        return float(text.replace(".", "").replace(",", ""))


def verdict(views, save_rate, average):
    if views < STOP_RATIO * average:
        return "STOP"
    if views > average and save_rate > WINNING_SAVE_RATE:
        return "WINNING"
    if views > average:
        return "GOOD"
    return "OPTIMASI"


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    views_by_platform = defaultdict(list)
    for row in rows:
        views_by_platform[row.get("platform", "semua")].append(to_number(row["views"]))
    averages = {key: sum(values) / len(values) for key, values in views_by_platform.items()}

    writer = csv.writer(sys.stdout)
    writer.writerow(["topik", "platform", "views", "rata_rata_views", "save_rate_persen", "verdict"])
    for row in rows:
        platform = row.get("platform", "semua")
        views = to_number(row["views"])
        save_rate = to_number(row["save"]) / views if views else 0.0
        average = averages[platform]
        writer.writerow([row["topik"], platform, int(views), round(average), round(save_rate * 100, 1), verdict(views, save_rate, average)])

    if len(rows) < 10:
        print(f"Catatan: baru {len(rows)} konten. Rata-rata belum stabil, verdict masih sementara.", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1])
