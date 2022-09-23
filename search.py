def searchname():
    infile = open("names.txt", "r")
    keyword = "A"

    for element in infile.readlines():
        if "A" in element:
            print(element)
        infile.close()


def search_name_input():
    infile = open("names.txt", "r")
    user_input = input("Insert keyword: ")

    for element in infile.readlines():
        if user_input in element:
            print(element)


def search_age():
    infile = open("names.txt", "r")
    for s in infile:
        print(s)


def search_age_input():
    infile = open("names.txt", "r")
    age = "5"
    for element in infile.readlines():
        if "5" in element:
            print(element)
        infile.close()


def search_age_input():
    infile = open("names.txt", "r")
    user_age = input("Insert age: ")

    for element in infile.readlines():
        if user_age in element:
            print(element)
        infile.close()
