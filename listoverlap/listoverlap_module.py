import random


def listoverlap(list1, list2):
    res = list(set(list1) & set(list2))
    return res


def main():
    a = [random.randint(0, 101) for x in range(random.randint(5, 20))]
    b = [random.randint(0, 101) for x in range(random.randint(5, 20))]
    print(a)
    print(b)
    print(listoverlap(a, b))


if __name__ == '__main__':
    main()
