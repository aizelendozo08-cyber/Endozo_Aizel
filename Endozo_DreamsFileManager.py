import os
os.system("cls")

while True:
    print("----------choose an option----------")
    print("1 - Read inspiring messages\n2 - Add a new insporing message\n3 - Rewrite the entire file\n4 - Exit")
    ask = int(input("I choose you: "))
    os.system("cls")
    if ask == 1:
        f = open("dream.txt","r")
        content = f.read()
        f.close()
        print(content)
    elif ask == 2:
        ask2 = input("Please enter ur message: ")
        f = open("dream.txt","a")
        f.write(f"\n{ask2}")
        f.close()
        print("\nyour message has been added :)\n")
    elif ask == 3:
        print("Warning: This will delete all the content in the file and replace it with the new content you will enter.")
        sureba = input("Are you sure you want to continue? (yes/no) ").lower()
        if sureba == "yes":
            os.system("cls")
        elif sureba == "no":
            os.system("cls")
            continue
        else:
            os.system("cls")
            print("Invalid input. yes or no answers only.")
            continue        
        ask3 = input("Please enter the new content: ")
        f = open("dream.txt","w")
        f.write(ask3)
        f.close()
        print("\nyour file has been rewritten :)n")
    elif ask == 4:
        os.system("cls")
        print("thank u, next (yuh)\n-- ariana grande")
        break