#!/usr/bin/env python3
import sys
import pandas as pd

#baca hasil reducer
data = []
for line in sys.stdin:
    word, count = line.strip().split("\t")
    data.append((word, int(count)))

df = pd.DataFrame(data, columns=["word", "count"])

#analisis deskriptif
total_words = df["count"].sum()
unique_words = df["word"].nunique()
mean_freq = df["count"].mean()
max_word = df.loc[df["count"].idxmax()]

print("=== Analisis Deskriptif ===")
print(f"Total kemunculan kata   : {total_words}")
print(f"Jumlah kata unik        : {unique_words}")
print(f"Rata-rata frekuensi     : {mean_freq:.2f}")
print(f"Kata paling sering      : {max_word['word']} ({max_word['count']})")

#simpan hasil analisis ke CSV
summary = pd.DataFrame({
    "Total Words": [total_words],
    "Unique Words": [unique_words],
    "Mean Frequency": [mean_freq],
    "Most Frequent Word": [max_word['word']],
    "Max Count": [max_word['count']]
})

summary.to_csv("descriptive_output.csv", index=False)
