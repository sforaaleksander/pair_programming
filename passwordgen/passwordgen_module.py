import string
import random


def passwordgen():
    leters_lower = [random.choice(string.ascii_lowercase) for x in range(random.randint(5, 8))]
    letter_upper = [random.choice(string.ascii_uppercase) for x in range(random.randint(2, 5))]
    numbers = [str(random.randint(0, 10)) for x in range(2)]
    symbols = [random.choice(["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_",
                              "+", "{", "}", ":", "|", "<", ">", "?", ">"]) for x in range(2)]
    password = [leters_lower, letter_upper, numbers, symbols]
    password = ["".join(x) for e in password for x in e]
    random.shuffle(password)
    return "".join(password)


def main():
    passwordgen()
    return


if __name__ == '__main__':
    main()
