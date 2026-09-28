import csv
import random

filename = "data/PhiUSIIL_Phishing_URL_Dataset.csv"
unique_urls = {}

with open(filename, encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        url = row["URL"].strip()
        label = row["label"].strip()

        if not url or not label:
            continue

        if url in unique_urls and unique_urls[url] != label:
            raise ValueError(f"Conflicting labels for URL: {url}")

        unique_urls[url] = label

print("Unique URLs:", len(unique_urls))

examples = list(unique_urls.items())
random.Random(42).shuffle(examples)

split_point = int(len(examples) * 0.80)
train = examples[:split_point]
test = examples[split_point:]

train_urls = {url for url, label in train}
test_urls = {url for url, label in test}
shared_urls = train_urls & test_urls

print("Training examples:", len(train))
print("Test examples:", len(test))
print("URLs in both groups:", len(shared_urls))
