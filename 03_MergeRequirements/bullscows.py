from random import choice
from urllib.request import urlopen
from os.path import isfile
import argparse
import cowsay
from io import StringIO


def bullscows(guess: str, secret: str) -> (int, int):
    bulls = sum(1 for i in range(len(guess)) if guess[i] == secret[i])
    cows = set(guess).intersection(set(secret)).__len__()

    return bulls, cows


def ask(prompt: str, valid: list[str] = None) -> str:

    owl = cowsay.read_dot_cow(StringIO("""
    $the_cow = <<EOC;
             $thoughts
              $thoughts
               ___
              (o o)
             (  V  )
            /--m-m-
    EOC
    """))

    if valid:
        word = input(cowsay.cowsay(prompt, cowfile=owl) + '\n')
        while word not in valid:
            print(cowsay.cowsay("Неизвестное слово, повторите попытку...", cowfile=owl) + '\n')
            word = input(cowsay.cowsay(prompt, cowfile=owl) + '\n')

        return word
    else:
        return input(cowsay.cowsay(prompt, cowfile=owl) + '\n')


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(cowsay.cowsay(format_string.format(bulls, cows), cow=cowsay.get_random_cow()))


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    word = choice(words)
    guess = ask("Введите слово: ", words)
    tries = 0

    while guess != word:
        tries += 1
        inform("Быки: {}, Коровы: {}", *bullscows(guess, word))
        guess = ask("Введите слово: ", words)

    return tries + 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('dictionary', help='provide dictionary to use')
    parser.add_argument('-l', help='specify length of words used', type=int, default=5, metavar='length')

    args = parser.parse_args()

    if isfile(args.dictionary):
        with open(args.dictionary, "r") as f:
            dictionary = f.read().split()
    else:
        dictionary = urlopen(args.dictionary).read().decode().split()

    new_dictionary = [word for word in dictionary if len(word) == args.l]

    print("Вы угадали слово за {} попыток!".format(gameplay(ask, inform, new_dictionary)))
