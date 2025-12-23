happy_words = ["good", "great", "happy","fun"]
sad_words= ["bad", "sad", "boring", "angry"]

user_text = input("How was ur day?" ).lower()
if any(word in user_text for word in happy_words):
    print("AI:Glad to hear that!")
elif any(word in user_text for word in sad_words):
    print("AI:Sorry to hear that.")
else:
    print("AI: Tell me more!")