def check_password(func):
    def wrapper(*args, **kwargs):
        password = input("Введите пароль: ")
        if password != "ваш_пароль":  # замените на нужный пароль
            print("В доступе отказано")
            return None
        return func(*args, **kwargs)
    return wrapper

@check_password
def protected_function():
    print("Доступ к функции получен.")

# Пример вызова
protected_function()