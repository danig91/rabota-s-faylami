# Открывает файл data.txt и выводит содержимое на экран.
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# Дополняет файл новыми строками с помощью режима добавления 'a'.
with open("data.txt", "a", encoding="utf-8") as file:
    file.write(
        """Дополните файл новыми строками с помощью режима добавления 'a'.
Реализуйте чтение содержимого файла построчно и выведите его на экран.
Скопируйте файл в бинарном режиме, создав его копию с другим именем."""
    )

# Чтение содержимого файла построчно и вывод на экран.
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Чтение файла в бинарном режиме.
with open("data.txt", "rb") as file:
    content = file.read()

# Создание копии с другим именем.
with open("new_name.txt", 'wb') as file:
    file.write(content)
