'''
Teste controlado das coisas
'''
import os
from time import time
import pandas as pd
dire = 'stations/stations'

def timer(function):
    def wrapper(*args, **kwargs):
        before = time()
        function(*args, **kwargs)
        after = time()
        print('Elapsed: {}s'. format(after-before))
    return wrapper

@timer
def teste ():    
    x = os.walk(dire)
    for i in x:
        station = i[0][-9:-5]
        lastest_station = ''

        if i[2]:
            for j in i[2]:

                grabfile(i[0], j)


@timer
def teste2 ():
    station_list = os.listdir(dire)
    for i in x:
        path = '{}/{}'.format(dire, i)
        y = os.listdir(path)

        latest = y.max()
        for j in y:    
            path = '{}/{}'.format(path, j)
            try:
                z = os.listdir(path)
                for k in z:
                    grabfile(path, k)
            except:
                pass


def grabfile (path, file):
    path = '{}/{}'.format(path, file)
    if os.path.getsize(path) > 198:
        pd.read_csv(path, header=None, delim_whitespace=True)    

teste()
teste2()