def palindrome(str):
    str = str.lower().replace(" ", "")
    if str == str[::-1]:
        return True
    return False


def main():
    user_str = input("Enter string: ")
    print(user_str)
    return palindrome(user_str)


if __name__ == '__main__':
    main()
 