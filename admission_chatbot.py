import difflib
responses = {
    "greeting": "Hello! How can I assist you with your admission process today?",
    "application_deadline": "The application deadline for the fall semester is March 1st.",
    "required_documents": "You will need to submit your transcripts, letters of recommendation, and a personal statement.",
    "tuition_fees": "The tuition fees vary depending on the program. Please visit our website for detailed information.",
    "contact_admissions": "You can contact the admissions office",
    "age_requirement": "The minimum age requirement for applicants is 17 years old.",
}
def best_match(query):
    keys = list(responses.keys())
    match = difflib.get_close_matches(query, keys, n=1, cutoff=0.6)
    return match [0] if match else None

def admission_chatbot():
    print("Welcome to the Admissions Chatbot!")
    print("You can ask me about application deadlines, required documents, tuition fees, and more.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit" or user_input == "quit":
            print("AI: Thank you for using the admission chatbot. Goodbye!")
            break
        if user_input == "help":
            print("AI: How may I assist you today? You can ask about: "+", ".join(responses.keys())+".")
            continue

        key = best_match(user_input)
        if key:
            print(f"AI: {responses[key]}")

        else:
            print("AI: Im sorry I cannot answer that, please talk to the admissions office for further assistance.")

if __name__ == "__main__":
    admission_chatbot()
