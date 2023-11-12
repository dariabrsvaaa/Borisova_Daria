def find_common_participants(first_group, second_group, argument=","):
    first_group = first_group.split(argument)
    second_group = second_group.split(argument)
    result = list(set(first_group) & set(second_group))
    return sorted(result)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, "|")
print(result)
