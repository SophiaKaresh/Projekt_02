"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Sophia Karešová
email: karesovasophia@seznam.cz
"""
import random
import time

CODE_LENGTH = 4
SEPARATOR = "-" * 55


def greet():
    print("Hi there!")
    print(SEPARATOR)
    print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
    print(SEPARATOR)


def secret_number():
    """Vytvoří tajné unikátní čtyřmístné číslo, nezačínající nulou a bez duplicit."""
    first_number = random.choice("123456789")
    all_numbers = "0123456789"
    rest_of_numbers = random.sample([n for n in all_numbers if n != first_number], CODE_LENGTH - 1)
    return first_number + "".join(rest_of_numbers)


def control_tip(tip):
    """Zkontroluje, zda tip splňuje podmínky."""
    if not tip.isdigit():
        print("The input must contain only digits.")
        return False
    elif len(tip) != CODE_LENGTH:
        print(f"The number must contain {CODE_LENGTH} characters.")
        return False
    elif tip[0] == "0":
        print("The number couldn't start with zero.")
        return False
    elif len(set(tip)) != CODE_LENGTH:
        print("The number must contain unique characters.")
        return False
    return True


def evaluate_tip(secret, tip):
    """Spočítá kolik je shod čísla na správné pozici - bulls,
    a kolik je uhodnutých čísel na nesprávné pozici - cows"""
    bulls = sum(tip[i] == secret[i] for i in range(CODE_LENGTH))
    cows = sum(c in secret for c in tip) - bulls
    return bulls, cows


def pluralize(count, word):
    """Vrátí správný tvar slova podle počtu."""
    return f"{count} {word}" if count == 1 else f"{count} {word}s"


def main():
    greet()
    game_stats = []  # ukládání počtu pokusů pro každou hru

    while True:  # více her za sebou
        secret = secret_number()
        bulls = 0
        attempts = 0
        start_time = time.time()

        first_prompt = True
        try:
            while bulls != CODE_LENGTH:
                prompt = "Enter a number: " if first_prompt else ">>> "
                tip = input(prompt)
                first_prompt = False

                if not control_tip(tip):
                    continue

                attempts += 1
                bulls, cows = evaluate_tip(secret, tip)

                if bulls == CODE_LENGTH:
                    elapsed = time.time() - start_time
                    minutes = int(elapsed // 60)
                    seconds = int(elapsed % 60)

                    print(f"Correct, you've guessed the right number\nin {attempts} guesses!")
                    print(f"Time: {minutes} min {seconds} sec")
                    print(SEPARATOR)
                    print("That's amazing!")
                    game_stats.append(attempts)
                    break
                else:
                    print(f"{pluralize(bulls, 'bull')}, {pluralize(cows, 'cow')}")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting game. Bye! 👋")
            break

        again = input("Do you want to play again? (y/n): ").lower()
        if again != "y":
            print(SEPARATOR)
            print("Game statistics:")
            for i, g in enumerate(game_stats, 1):
                print(f"Game {i}: {g} guesses")
            print("Thanks for playing, bye! 👋")
            break


if __name__ == "__main__":
    main()
