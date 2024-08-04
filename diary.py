def main():
    print("Welcome to your Personal Diary!")
    while True:
        entry = input("Write your entry (type 'exit' to quit):\n")
        if entry.lower() == 'exit':
            break
        with open('diary.txt', 'a') as diary_file:
            diary_file.write(entry + '\n')
            print("Entry saved successfully!\n")
    print("Exiting Diary...")

if __name__ == "__main__":
    main()
