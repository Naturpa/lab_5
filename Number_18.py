def check_password(correct_password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            password = input("Введите пароль: ")
            if password != correct_password:
                print("В доступе отказано")
                return None
            return func(*args, **kwargs)

        return wrapper

    return decorator


@check_password('password')
def make_burger(typeOfMeat, withOnion=False, withTomato=True):
    print(f"Бургер с мясом {typeOfMeat}, с луком: {withOnion}, с помидорами: {withTomato}")


# Пример вызова
make_burger('говядина')
