def showMenu(show_menu_title = True):

    menu_title = ""

    if show_menu_title == True:
        menu_title = """--- NOTETAKER Class Project v1 ---
    By Software Engineering Class"""
    else: 
        menu_title = ""

    print(f"""
            {menu_title}
    Create beautiful notes with Python

    1. Create Note
    2. Update Note
    3. Delete Note
    4. Transfer Note
    5. Exit
""")