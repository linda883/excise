books = ["lanuage", ["python", "java"], "life", ["tom ", "sophoie"], 88]


for book in books:
    if isinstance(book, list):
        for item in book:
            print(item)
    else:
        print(book)

