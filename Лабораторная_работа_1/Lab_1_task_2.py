list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
middle_of_list = len(list_players) // 2
team1 = list_players[:middle_of_list]
team2 = list_players[middle_of_list:]
print(team1)
print(team2)