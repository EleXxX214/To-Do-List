from tkinter import N


choice = -1
tasks = []
while choice != "5":
    print("")
    print("1.Dodaj zadanie")
    print("2.Usun zadanie") 
    print("3.Wyswietl zadania")
    print("5.Wyjdz\n")

    

    choice = input("Podaj liczbe: ")
    def add_task():
        task = input("Nazwa zadania: ")
        tasks.append(task)



    if choice == "1":                                       #Add task
        add_task()
    if choice == "2":                                       #Delete task
        print("---------")
        nr = 1
        while nr < len(tasks):
            for i in tasks:
                print(str(nr) + "." + i)
                nr = nr + 1
            
        print("---------") 
        nr_taska = int(input("Podaj nr zadania: "))
        nr_taska = nr_taska - 1
        tasks.pop(nr_taska)
    
    if choice == "3":                                       #Show task
        print("---------")
        nr = 1
        while nr <= len(tasks):
            for i in tasks:
                print(str(nr) + "." + i)
                nr = nr + 1
            
        print("---------")    

    if choice == "5":                                       #Exit
        break


