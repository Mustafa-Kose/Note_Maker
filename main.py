import os

def note_writer():
    while True:
        print("""
            Note book
            1-create  
            2-write
            3-Read
            4-Add
            5-Exit
            """)
        whattodo=input("Choose a number from 1 to 5:")


        if whattodo == "1":
            try:    
                with open("New_TXT.txt","x+", encoding="utf-8") as file_New:
                    newtext=input("""What would you like to write to your note?
                                    """)
                    file_New.write(newtext)
                    print(file_New.read())
            except FileExistsError:
            
                print("The note has already been created.")
        elif whattodo == "2":
            with open("New_TXT.txt","w+",encoding="utf-8") as writy:
                whattowrite=input("""What would you like to write?
                                  """)
                writy.write(whattowrite)
                print(writy.read)
        elif whattodo == "3":
            with open("New_TXT.txt","r",encoding="utf-8") as notenew:
                if os.path.exists("New_TXT.txt"):
                    print(notenew.read())
                else:
                    print("Note doesn't exist. Would you like to create one?")
                
        elif whattodo == "4":
            with open("New_TXT.txt","a",encoding="utf-8") as noteadd:
                if os.path.exists("New_TXT.txt"):
                    addtonote=input("""Write the note that you would like to add                               
                                """)
                    noteadd.write(addtonote)
                    print(noteadd.read)
                else:
                    print("Note doesn't exist. Would you like to create one?")

                
        elif whattodo == "5":
            print("Byeee")
            break
        else:
            print("The number you have given isn't on the list.")

note_writer()