import datetime
def save_log():
    name = input("Enter name: ")
    status = input("Enter status (present/absent/absent): ").lower()
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open ("log.csv", "a") as file:
        entry = f"{name},{status},{time_now}\n"
        file.write(entry)

    print(f"Log saved for {name} as {status} at {time_now}")

save_log()