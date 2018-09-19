def create_dir():
    name = input("Пожалуйста, укажите название папки для создания:")
    import os
    if name in os.listdir():
        print("Папка с таким именем уже существует.")
        start()
    else:
        os.mkdir(name)
    print("Папка с именем \""+str(name)+"\" была создана.")


def remove_dir():
    name = input("Пожалуйста, укажите название папки для удаления:")
    import os
    import shutil
    dir = name
    if dir in os.listdir():
        shutil.rmtree(dir)
        print("Папка с именем \"" + str(dir) + "\" была удалена.")
    else:
        print("Папка с таким именем не существует.")



def in_dir():
    import os
    print("Содержимое текущей папки:")
    for i in os.listdir():
        if i != "__pycache__":
            print(i)
    start()


def open_dir():
    name = input("Пожалуйста, укажите название папки для перехода:")
    name = str(name)
    import os
    try:
        os.chdir(name)
        print("Вы перешли в папку \""+ name+"\".")
        start()
    except FileNotFoundError:
        print("Вы указали несуществующую папку.\nПопробуйте снова.")
        start()


def start():
        print("1. Перейти в папку\n"
            "2. Просмотреть содержимое текущей папки\n"
            "3. Удалить папку\n"
            "4. Создать папку")
        choice = int(input("Ваш выбор:"))
        if choice == 1:
            open_dir()
        elif choice == 2:
            in_dir()
        elif choice == 3:
            remove_dir()
        elif choice == 4:
            create_dir()
