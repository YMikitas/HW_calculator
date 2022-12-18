def sum_comp (a_1:float, b_1:float, a_2:float, b_2:float): 
    ''' 
    Суммирование 2 комплексных чисел 
    a_1, a_2 float –действительные части чисел 
    b_1, b_2 float-мнимые части чисел 
    результат - кортеж: 
    result_a - действительная часть результата 
    result_b - мнимая часть результата 
    '''
    result_a =a_1+a_2 
    result_b =b_1+b_2
    return result_a, result_b 
 
#в общем виде ответ будет в формате: 
#print (f’ str (result_a) + str (result_b)*i’) 
 
def  subtraction_comp (a_1:float, b_1:float, a_2:float, b_2:float):  
    ''' 
    Вычитание 2 комплексных чисел
    Аргументы: 
    a_1, a_2 float -действительные части чисел 
    b_1, b_2 float -мнимые части чисел 
    Результат - кортеж: 
    result_a - действительная часть результата 
    result_b - мнимая часть результата 
    ''' 
    result_a =a_1-a_2 
    result_b =b_1-b_2 
    return result_a, result_b 
 
def  multiplication_comp (a_1:float, b_1:float, a_2:float, b_2:float): 
    ''' 
    Умножение 2 комплексных чисел
    Аргументы: 
    a_1, a_2 float -действительные части чисел 
    b_1, b_2 float -мнимые части чисел 
    Результат - кортеж: 
    result_a - действительная часть результата 
    result_b - мнимая часть результата 
    ''' 
    result_a = a_1* a_2- b_1* b_2 
    result_b = a_1* b_2+ a_2* b_1  
    return result_a, result_b 
 
def  division_comp (a_1:float, b_1:float, a_2:float, b_2:float): 
    ''' 
    Деление 2 комплексных чисел
    a_1 и b_1 - делимое a_2 и b_2 -делитель
    Аргументы: 
    a_1, a_2 float -действительные части чисел 
    b_1, b_2 float -мнимые части чисел 
    Результат - кортеж: 
    result_a - действительная часть результата 
    result_b - мнимая часть результата 
    ''' 
    result_a= (a_1* a_2+ b_1* b_2)/( a_2**2+ b_2**2) 
    result_b= (a_2* b_1+ a_1* b_2)/( a_2**2+ b_2**2) 
    return result_a, result_b
