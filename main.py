from core import process_input
from memory import init_database


def main():
    init_database()

    print("AMBER is starting...")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("AMBER: Goodbye.")
            break

        response = process_input(user_input)
        print(f"AMBER: {response}")


if __name__ == "__main__":
    main()