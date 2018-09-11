# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

player_name = "Jack"
enemy_name = "Mob"
# player_name = input("Назовите героя:")
# enemy_name = input("Назовите врага:")
player = {"name": player_name, "health": 100, "damage": 7}
enemy = {"name": enemy_name, "health": 100, "damage": 6}


def health(char1, char2):
    print("Здоровье", char1["name"].upper(), "-", str(char1["health"]) + ".")
    print("Здоровье", char2["name"].upper(), "-", str(char2["health"]) + ".\n")


health(player, enemy)


def attack(char1, char2):
    char2["health"] = char2["health"] - char1["damage"]
    print(char1["name"].upper(), "нанес", char1["damage"], "урона", char2["name"].upper() + "!\n")


attack(player, enemy)
health(player, enemy)

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

player_name = "Jack"
enemy_name = "Mob"
# player_name = input("Назовите героя:")
# enemy_name = input("Назовите врага:")
player = {"name": player_name, "health": 100, "damage": 43, "armor": 1.1}
enemy = {"name": enemy_name, "health": 100, "damage": 40, "armor": 1.3}
with open(str(player['name']) + ".txt", "w") as player_file:
    for attr in list(player.keys()):
        attr = attr + " - " + str(player.get(attr)) + "\n"
        player_file.write(attr)
with open(str(enemy['name']) + ".txt", "w") as enemy_file:
    for attr in list(enemy.keys()):
        attr = attr + " - " + str(enemy.get(attr)) + "\n"
        enemy_file.write(attr)


def read_files(start):
    with open(str(player['name']) + ".txt", "r") as player_file:
        for line in player_file:
            player["name"] = line.split(" ")[2]
            player["health"] = line.split(" ")[2]
            player["damage"] = line.split(" ")[2]
            player["armor"] = line.split(" ")[2]
    with open(str(enemy['name']) + ".txt", "r") as enemy_file:
        for line in enemy_file:
            enemy["name"] = line.split(" ")[2]
            enemy["health"] = line.split(" ")[2]
            enemy["damage"] = line.split(" ")[2]
            enemy["armor"] = line.split(" ")[2]


def health(char1, char2):
    print("Здоровье", char1["name"].upper(), "-", str(round(char1["health"], 2)) + ".")
    print("Здоровье", char2["name"].upper(), "-", str(round(char2["health"], 2)) + ".\n")


def attack(char1, char2):
    print(char1["name"].upper(), "наносит", char2["name"].upper(), "удар на", str(char1["damage"]) + "!")


def armor(char1, char2):
    damage = char1["damage"] / char2["armor"]
    char2["health"] = char2["health"] - round(damage, 2)
    print(char2["name"].upper(), "получает урон -", str(round(damage, 2)) + "!\n")


print("Начало игры!")
print(player["name"], "VS", enemy["name"])
i = 1
while True:
    if i == 1:
        attack(player, enemy)
        armor(player, enemy)
        health(player, enemy)
        if enemy["health"] < 0:
            print("Победа!", player["name"], "одолел злобного", enemy["name"], "\nОсталось", round(player["health"], 2),
                  "здоровья.")
            break
        else:
            pass
        i -= 1
    if i == 0:
        attack(enemy, player)
        armor(enemy, player)
        health(player, enemy)
        if player["health"] < 0:
            print("Победа!", enemy["name"], "одолел злобного", player["name"], "\nОсталось", round(enemy["health"], 2),
                  "здоровья.")
            break
        else:
            pass
        i += 1
