from typing import Optional

def give_int(input_string: str, min_num: Optional[int] = None, max_num: Optional[int] = None) -> int:
    '''
    Takes an int number from user
    Takes: string
    Returns: int number or a message about an error
    '''
    while True:
        try:
            num = int(input(input_string))
            if min_num and num < min_num:
                print(f'Введите больше {min_num}')
                continue
            if max_num and num > max_num:
                print(f'Введите меньше {max_num}')
                continue
            return num
        except ValueError:
            print('Вы ввели не число')

def check(first_arg, second_arg, operator):
    if second_arg == '0' and operator == '/':
        print('Деление на 0 не предусмотрено')
    for i in first_arg:
        if '+' or '-' in i:
        # строка вида 'a+bi'
            a_complex = complex(first_arg)
            break
        if '+' or '-' not in i:
        # строка вида 'bi'
            a_complex = f'0+{first_arg}'
            complex(a_complex)
    # Проверка на наличие знака во втором аргументе: 
    for i in second_arg:
        if '+' or '-' in i:
            b_complex = complex(second_arg)
            break
        if '+' or '-' not in i:
            b_complex = f'0+{second_arg}'
            complex(second_arg)