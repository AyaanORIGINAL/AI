print("Hello! Im your snack helper AI.")

time = (input("Is it morning or afternoon? ")).lower()
hunger = (input("Are you hungry? (yes/no) ")).lower()
if time == "morning":
    if hunger == "yes":
        print("AI: You should have a big breakfast with eggs and toast.")
    else:
        print("AI: Maybe just have some coffee then.")

elif time == "afternoon":
    if hunger == "yes":
        print("AI: How about a yummt snack like a sandwich?")
    else:
        print("AI: You can just have some tea")
else:
    print("AI: Im still learning about other times of the day!")