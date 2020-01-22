import datetime


def years(age):
    year_now = datetime.datetime.today().year
    user_is_100 = 100 - age + year_now
    return user_is_100


def main():
    user_name = input("Type in your name: ")
    user_age = int(input("Type in you age: "))
    print(f"{user_name}, you will be 100 year old in {years(user_age)}")


if __name__ == '__main__':
    main()
