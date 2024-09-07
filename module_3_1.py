calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls()
    return (len(string), string.lower(), string.upper())


def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]


print(string_info('Capybara'))  # Длина Регистры
print(string_info('Armageddon'))  # Длина Регистры
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Совпадения
print(is_contains('cycle', ['recycling', 'cyclic']))  # Совпадения
print(calls)  # Количество вызовов
