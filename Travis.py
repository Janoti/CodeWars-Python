known_users = ["Alice","Paulo","Claire","Dan", "Emma","Fred"]
users_qtd = len(known_users)
print("Known Users: {}".format(users_qtd))

while True:
    print("Hi! My name is Travis ")
    usr_name = input("Whats is your name?: ").strip().capitalize()
    if usr_name in known_users:
        print("Hello {} !".format(usr_name))
        remove = input("Would you like to be removed from the system (y/n)? :").lower()
        if remove == "y":
            print(known_users)
            known_users.remove(usr_name)
            print(known_users)
        elif remove == "n":
            print("Ok! Not removed!")
    else:
        print("I don't regconised you {}!".format(usr_name))
        add = input("Would you like to be add to the system (y/n)? :").lower()
        if add == "y":
            known_users.append(usr_name)
            print(known_users)
        elif add == "n":
            print ("OK! Not added!")

