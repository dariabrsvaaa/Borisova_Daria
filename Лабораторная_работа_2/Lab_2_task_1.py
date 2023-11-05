salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

need_money = 0  # количество денег на проживание в течение 10 месяцев
need_money = spend - salary
i = 2
for k in range(i, months+1):
       spend = 1.03 * spend
       need_money = need_money + spend - salary

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(need_money,2))
