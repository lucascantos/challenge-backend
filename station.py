'''
Funçoes de consulta de estações
'''
import os
dire = 'stations/stations'
x = os.walk(dire, False)
for i in x:
    
        print('{}: {}'.format(i[0], i[2][-1]))
    except:
        pass