# Разработать функцию replace(). Желательно в этой функции использовать ранее разработаную функцию slice()
# функция принимает 3 параметра:
# исходная строка
# что мы хотим изменить
# на что мы хотим изменить
# Пример: replace("abc", "ab", "d") ---> функция возвращает: "dc"
# Встроеный в python метод .replace() использовать нельзя.

# print("abcab".replace("ab", "!"))
def slice(row, start, end):
    answer = ""
    i = start
    while i < end:
        answer += row[i]
        i += 1
    return answer
# print(slice("abc", 0, 2)) # 0 1
# print(slice("abc", 1, 2))

def replace(row, tochange, replacement):
    answer = ""
    i = 0
    while i < len(row):
        if row[i:i + len(tochange)] == tochange:
            answer += replacement
            i += len(tochange) - 1
        else:
            answer += row[i]
        i += 1
    return answer


print(replace("abc", "ab", "d") )

# print(len("abc"))