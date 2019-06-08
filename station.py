'''
Funçoes de consulta de estações
'''
import os
from datetime import datetime
import pandas as pd

def station_hour(path,file):
    '''
    Abre um dataframe do banco de dados e tira a ultima horade registro
    '''
    df = unpack_data(path,file)
    return df['HORA'].max()


def unpack_data(path,file):
    # Coluna3 = Hora recente
    # Abre o arquvio com a data mais recente
    file_path = '{}/{}'.format(path, file)

    header = ['ESTACAO', 'LATITUDE', 'LONGITUDE', 'ALTITUDE', 'ANO', 'MES', 'DIA', 'HORA', 'TEMP', 'TMAX', 'TMIN',
    'UR','URMAX' , 'URMIN' , 'TD' , 'TDMAX' , 'TDMIN' , 'PRESSAONNM' , 'PRESSAONNM_MAX' , 'PRESSAONNM_MIN',
    'VELVENTO', 'DIRVENTO', 'VELVENTO_RAJADA', 'RADIACAO', 'PRECIPATACAO']
    station_df = pd.read_csv(file_path, header=None, delim_whitespace=True)
    station_df.columns = header
    return station_df

dire = 'stations/stations'
file_list = os.walk(dire)
for file in file_list:
    try:
        print(file[0])
    except:
        pass