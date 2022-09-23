def searchname():
    infile = open("names.txt", "r")
    for s in infile:
        print(s)


def searchname():
    infile = open("names.txt", "r")
    for s in infile:
        print(s[:-1])


def searchname():
    infile = open("names.txt", "r")
    keyword = "A"

    for element in infile.readlines():
        if "A" in element:
            print(element)
    infile.close()


def searchname():
    infile = open("names.txt", "r")
    keyword = input("insert keyword: ")

    for element in infile.readlines():
        if keyword in element:
            print(element)
    infile.close()


def searchage():
    infile = open("names.txt", "r")
    for s in infile:
        print(s)
