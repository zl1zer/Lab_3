import string  
password = input()

errors = False # Флаг

# Длинна
if len(password) != 8:
    print("Длина пароля не равна 8;")
    errors = True

# Заглавные
if password == password.lower():
    print("В пароле отсутствуют заглавные буквы;")
    errors = True

# Строчные
if password == password.upper():
    print("В пароле отсутствуют срочные буквы")
    errors = True

# Цифры
if not any(symbol.isdigit() for symbol in password):
    print("В пароле отсутствуют цифры;")
    errors = True

# Спец. Символы
specials = "*-#"
if not any(symbol in specials for symbol in password):
    print("В пароле отсутствуют специальные символы;")
    errors = True

# Неизвестные символы
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + specials
if not all(symbol in allowed for symbol in password):
    print("В пароле используются непредусмотренные символы.")
    errors = True

if not errors:
    print("Надежный пароль")
