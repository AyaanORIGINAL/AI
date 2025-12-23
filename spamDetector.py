spam_words = ["win", "free", "money", "prize", "urgent"]
user_msg = input("Enter a message: ").lower()
words = user_msg.split()
spam_score = 0
for w in words:
    if w in spam_words:
        spam_score += 1
print("Spam score:", spam_score)
if spam_score >=2:
    print("This message is likely spam.")
else:
    print("This message is likely not spam.")