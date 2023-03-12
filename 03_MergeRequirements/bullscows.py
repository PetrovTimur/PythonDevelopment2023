def bullscows(guess: str, secret: str) -> (int, int):
    bulls = sum(1 for i in range(len(guess)) if guess[i] == secret[i])
    cows = set(guess).intersection(set(secret)).__len__()

    return bulls, cows


def ask(prompt: str, valid: list[str] = None) -> str:
    if valid:
        word = input(prompt)
        while word not in valid:
            print("Неизвестное слово, повторите попытку...")
            word = input(prompt)

        return word
    else:
        return input(prompt)
