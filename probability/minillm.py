import random

token_options = {
    "am happy": (50, "cheerful"),
    "will study": (40, "focused"),
    "eat robots": (10, "unhinged"),
}

def generate_sentence(start_word):
    words = list(token_options.keys())
    weights = [token_options[word][0] for word in words]

    prediction = random.choices(words, weights=weights, k=3)[0]
    tone = token_options[prediction][1]

    return f"[Tone: {tone}], {start_word} {prediction}."

start = input("Start the sentence, e.g, I ")
print(f"Ai prediction: {generate_sentence(start)}")
