name = input("What's your name? ")

match name:
    case "Harry Potter" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print('Who?')
    #case _ é como se fosse o default
