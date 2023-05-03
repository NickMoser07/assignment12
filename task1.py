def main():
    baseList = list(range(1, 101))

    list1 = [i for i in baseList if i % 2 == 0]
    print(list1)

    list2 = [i for i in baseList if i < 50 and i % 3 == 0]
    print(list2)

    list3 = [i * 10 for i in baseList if i  > 50 and i % 5 == 0]
    print(list3)

main()