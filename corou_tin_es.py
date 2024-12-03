def searcher():
    import time
    # 3 sec time consuming task
    book = "This is nitin barfa learning python"
    time.sleep(3)


    while True:
        text = (yield)
        if text in book:
            print("Your text is in book")

        else:
            print("Your text is not in book")


search = searcher()
next(search)
search.send("nitin")
input("Press any key")
search.send("nitin barfa")