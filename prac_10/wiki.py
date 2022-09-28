import wikipedia


search = input("Input your search string: ")
while search != "":
    content = wikipedia.summary(search)
    print(content)
    search = input("Input your search string: ")

