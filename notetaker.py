print("""
--- NOTETAKER Class Project v1 ---
    By Software Engineering Class

    Create beautiful notes with Python

    1. Create Note
    2. Update Note
    3. Delete Note
""")

option = input("Enter an option from the menu items: ")



if len(option.strip()) != 0: 
    ## start the loop
    while True: 
    
        if option == "1": 
            note_title = input("Enter your note title: ")

            if len(note_title.strip()) == 0: 
                print("You did not enter a title!")
            else: 
                note_content = input("Enter Note Content: ")

                if len(note_content.strip()) == 0: 
                    print("You did not enter any content ...")
                else: 
                    ## create note with title and content 
                    ## create a file using the title name
                    title_object = open(note_title, "w")

                    title_object.write(note_content)
                    title_object.close()

                    print("Note saved successfully!")

        elif option == "2": 
            ## updating note 
            updated_filename = input("Enter filename to be updated: ")

            if len(updated_filename.strip()) != 0: 
                fobject = open(updated_filename, "a")

                new_content = input("Enter new content: ")
                if len(new_content.strip()) != 0:
                    fobject.write("\n")
                    fobject.write(new_content)

                fobject.close()


        elif option == "3": 
            ## deleting note
            pass

else: 
    print("No option was entered.. exiting ..")