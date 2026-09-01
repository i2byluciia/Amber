from core import process_input

def main():
    print("Amber is starting...")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit"]:
            print("Amber: Goodbye! ")
            break

        response = process_input(user_input)
        print(f"Amber: {response}")

if __name__ == "__main__":
    main()