def month_to_season(month):
    if month == 12 or month == 1 or month == 2:
        return "Зима"
    elif month == 3 or month == 4 or month == 5:
        return "Весна"
    elif month == 6 or month == 7 or month == 8:
        return "Лето"
    elif month == 9 or month == 10 or month == 11:
        return "Осень"
    else:
        return "Неверный номер месяца"


month = 11
season = month_to_season(month)


print(f"Месяц {month}: {season}")
