print("Welcome to MoodMatcher AI v2.0")

mood_database = {
    "happy": {
        "keywords": ["good", "great", "fantastic", "joyful", "excited"],
        "recommendations": ["Ice cream shop"]
    },
    "sad": {
        "keywords": ["bad", "terrible", "awful", "depressed", "upset"],
        "recommendations": ["Warm Soup Restaurant"]
    },
    "stressed": {
        "keywords": ["anxious", "nervous", "overwhelmed", "tense", "worried"],
        "recommendations": ["Calm Cafe"]
    }
}
user_input = input("How are you feeling today?").lower()
scores = {}
for mood, data in mood_database.items():
    count = 0
    for word in data["keywords"]:
        if word in user_input:
           count += 1
        scores[mood] = count

dominant_mood = max(scores, key=scores.get)

print(f"\nAnalysis: {scores}")

if scores[dominant_mood] > 0:
    recommendation = mood_database[dominant_mood]["recommendations"][0]
    print(f"Detected mood: {dominant_mood.upper()}")
    print(f"Recommendation: Visit the {recommendation} for a mood boost!")

else:
    print("Mood unclear. Recommendation: Go to your usual buffet or hit the gym")