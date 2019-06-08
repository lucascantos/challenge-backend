'''
Funçoes de consulta de estações
'''
import os
dire = 'stations/sample'
x = os.walk(dire, False)
for i in x:
    try:
        print('{}: {}'.format(i[0][-9:-5], i[2][-1]))
        
    except:
        pass