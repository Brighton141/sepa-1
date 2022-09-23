from search import search_name_input, search_age_input


print("Hello!")
criteria = input("What criteria would you like to use for search? \n"
                 "1- Search with Name \n"
                 "2- Search with age \n"
                 ">")
if criteria == "1":
    search_name_input()
elif criteria == "2":
    search_age_input()
    print("Invalid choice")