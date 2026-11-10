
#dsfsdfsdfdsfsd


def find_unpaired(list_numbres):
    print('наша програма перевіряє парність елемента списку')
    
    for number in list_numbres:
        flag = False
        
        for other in list_numbres:
            if number == -other:
                flag = True
                print(f'ці елементи мають пару: {number} : {-other}')
                break
        if not flag:
            print(f'цей елемент не має пари: {number} ')



# find_unpaired([1, -1, 2, -2, 3])           
# find_unpaired([-3, 1, 2, 3, -1, -4, -2])  
# find_unpaired([1, -1, 2, -2, 3, 3])   


def find_unpaired_2(list_numbers):
    print('наша програма перевіряє парність елемента списку')

    unique = set()

    for number in list_numbers:
        if -number in unique:
            unique.discard(-number)
        else:
            unique.add(number)

    print(f'непарне значання: {unique.pop()}')
    
find_unpaired_2([1, -1, 2, -2, 3, 3])
#list_numbers = list(map(int,input('ведіть число:  ').split()))


numbers = input('ведіть число: ').split() 
list_numbers = [int(number) for number in numbers]

find_unpaired_2(list_numbers)
    