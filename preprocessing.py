import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Pastikan sudah download resource sekali saja
# nltk.download("punkt")
# nltk.download("stopwords")

input_file = "C:/hadoop/bin/wordcount/pageviews-20250901-000000.txt"
output_file = "C:/hadoop/bin/wordcount/pageviews-20250901-000000-cleaned.txt"

stop_words = set(stopwords.words("english"))

with open(input_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8") as fout:
    for line in fin:
        parts = line.strip().split(" ")
        if len(parts) >= 2:
            page_title = parts[1]

            # skip namespace (judul dengan ":")
            if ":" in page_title:
                continue

            # underscore -> spasi + lowercase
            page_title = page_title.replace("_", " ").lower()

            # hapus karakter non-alfanumerik
            page_title = re.sub(r"[^a-z0-9\s]", " ", page_title)

            # rapikan spasi
            page_title = re.sub(r"\s+", " ", page_title).strip()

            # tokenisasi
            tokens = word_tokenize(page_title)

            # filter: buang stopwords, kata <=3 huruf, angka murni
            tokens = [
                t for t in tokens
                if t not in stop_words and len(t) > 2 and not t.isdigit()
            ]

            cleaned_title = " ".join(tokens)

            if cleaned_title:
                fout.write(cleaned_title + "\n")

print(f"[INFO] Preprocessing selesai → {output_file}")