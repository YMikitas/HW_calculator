from constants import data
import colorama
from colorama import Fore, Back, Style
colorama.init()

def print_result_comp(data):
    '''
    вывод аргументов и результата действия с комплексными числами
    желтым цветом
    Аргумент списк data из файла constants
    data[0]=a_1         data[3]=a_2
    data[1]=b_1         data[4]=b_2
    data[2]=action      data[5]=a_result
                        data[6]=b_result
    '''
    print (Fore.YELLOW+'({} + {}*i) {} ({}+ {}*i)= ({} + {}*i) \n'.format(data[0], data[1], data[2], data[3],data[4],data[5],data[6]))
    print(Style.RESET_ALL)

def print_result_rational(data):
    '''
    вывод аргументов и результата действия с рациональными числами
    желтым цветом
    Аргумент списк data из файла constants
    data[0]=a_1                         data[3]=a_2
    data[1]=b_1 не используется         data[4]=b_2 не используется
    data[2]=action                      data[5]=a_result
                                        data[6]=b_result не используется
    '''
    print (Fore.YELLOW+'{} {} {} = {} \n'.format(data[0], data[2], data[3], data[5]))
    print(Style.RESET_ALL)

print()
print_result_comp(data) 
print_result_rational(data)   