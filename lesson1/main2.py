# age = 80

# if age >= 18 or age < 60:
#     print("register")
# elif age >= 60:
#     print("вам уже позно")
# else:
#     print("вам ещё рано")


numder = float(input('число '))
# print(5 % 2)
# print(f"{numder % 2} --- {numder % 2 == 0} ---") 

if numder % 2 == 0:
    # %  деление с остатком 
    # == сравнение
    # print('число', numder, 'четное')
    # print('число ' + str(numder) + ' четное')
    # print(f'число {numder} четное')
    # f-формат
    print('число {} четное'.format(numder))
else:
    print('не четное')

# число 8 чётное
