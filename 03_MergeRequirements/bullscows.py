def bullscows(guess: str, secret: str) -> (int, int):
    bulls = sum(1 for i in range(len(guess)) if guess[i] == secret[i])
    cows = set(guess).intersection(set(secret)).__len__()

    return bulls, cows
