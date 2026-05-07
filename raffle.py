import random


def draw_winner(total_lists: int, numbers_per_list: int = 10) -> tuple[int, int]:
    """Return a random (list_number, number_in_list) winner."""
    list_number = random.randint(1, total_lists)
    winning_number = random.randint(1, numbers_per_list)
    return list_number, winning_number


def main() -> None:
    print("Street Dogs Raffle")
    print("------------------")

    while True:
        try:
            total_lists = int(input("Enter the number of lists sold: "))
            if total_lists <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid whole number.")

    while True:
        prize_name = input("Prize name (example: Food basket): ").strip()
        if not prize_name:
            prize_name = "Prize"

        list_number, winning_number = draw_winner(total_lists)

        print("\nWinner drawn!")
        print(f"{prize_name}: List #{list_number} - Number #{winning_number}\n")

        again = input("Draw another prize? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Thanks for helping street dogs! 🐶")
            break


if __name__ == "__main__":
    main()
