from brain.engine import Brain


def main():
    print("=" * 50)
    print("        HIM - Local AI Test")
    print("=" * 50)

    brain = Brain()

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            print("\nGoodbye!")
            break

        reply = brain.ask(user_input)

        print(f"\nJungkook: {reply}")


if __name__ == "__main__":
    main()