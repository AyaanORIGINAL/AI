from textblob import TextBlob
print("Advanced Review Analyzer v1.0")
review = input("Review: ")
blob = TextBlob(review)
polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity

print(f"\n Sentiment Logic Breakdown: ")
print(f"Polarity Score: {polarity}")
print(f"Subjectivity Score: {subjectivity}")

if polarity > 0.5:
    verdict = "you LOVED it!"
elif polarity > 0:
    verdict = "you liked it."
elif polarity <-0.5:
    verdict = "you HATED it!"
else:
    verdict = "Neutral feelings detected."

if subjectivity > 0.7:
    Note = "Review has a lot of personal opinions."
else:
    Note = "Review is more factual."

print(f"\n AI Verdict: {verdict}")
print(f"Note: {Note}")
