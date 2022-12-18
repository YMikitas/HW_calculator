from datetime import datetime as dt
from time import time
from constants import data
import csv

def action_logger_head():
    '''
    создание файла журнала операций, если он еще не создан.
    формирование шапки журнала
    вызывается только при первом обращении к журналу
    '''
    my_file = open("calc_log_1.log", "w")
    #time=dt.now().strftime('%d.%m %H:%M') 
    with open('calc_log_1.log','a') as file:
        file.write(' data  time \t a1 \t+ \t b1*i \t action \t a2 \t+ \t b2 \t = \t a_result \t+ \t b_result\n')
        #                time a1+b1*i действие a2+b2*i= a_result+b_result*i
    my_file.close()

def action_logger(data):
    '''
    фиксирование данныx в журнал операций
    Аргумент списк data из файла constants
    data[0]=a_1         data[3]=a_2
    data[1]=b_1         data[4]=b_2
    data[2]=action      data[5]=a_result
                        data[6]=b_result
    '''
    time=dt.now().strftime('%d.%m %H:%M') 
    with open('calc_log_1.log','a+') as file:
        file.write('{} \t {} \t\t\t +{}i \t    {} \t\t {} \t\t\t{}i \t =\t\t {} \t\t +{}i \n'.format(time, data[0], data[1], data[2], data[3],data[4],data[5],data[6]))

#action_logger_head()
action_logger(data)