import wikipedia

def main():
    search_thing = input("Pleasr input the page title or search phrase: ")
    while search_thing != "":
        content = wikipedia.summary(search_thing)
        print(content)
        search_thing = input("Pleasr input the page title or search phrase: ")

main()