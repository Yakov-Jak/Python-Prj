# Определяем время года
mn = int(input('Введите номер месяца '))
while mn > 12 or mn < 1:
    print('Неправильный месяц. Введите еще раз')
    mn = int(input('Введите номер месяца'))

# Вариант со словарём
# kalend = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
#           9: "September",
#           10: "October",
#           11: "November",
#           12: "December"
#           }
# month = kalend.get(mn)

# Вариант со списком
kalend = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
mn = mn - 1
month = kalend[mn]

if month == "January" or month == "February" or month == "December":
    print(f"{month} - это зима!")
elif month == "April" or month == "May" or month == "March":
    print(f"{month} - это весна")
elif month == "June" or month == "July" or month == "August":
    print(f"{month} - это лето")
else:
    print(f"{month} - это осень")
