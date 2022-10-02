import wikipedia

search_phrase = input("Please enter the thing you want to search: ")
while search_phrase != "":
    try:
        page = wikipedia.page(search_phrase)
        print(page.title)
        print(page.summary)
        print(page.url)
        search_phrase = input("Please enter the thing you want to search: ")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)

