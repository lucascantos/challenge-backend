from datetime import timedelta, date
import pandas as pd

import os.path
from zipfile import ZipFile

def error_handler(function):
    '''
    Função de tratamento dos erros da função:
    TODO: Aprender dar um argumento de entrada no decorador pra customizar os erros por função
    TODO: Depois disso, logar os erros
    '''
    def wrapper(*args, **kargs):
        try:
            return function(*args, **kargs)
        except Exception as e:
            print(e)
            pass
    return wrapper


def datarange(start_date, end_date):
    '''
    Faz loop entre duas datas, diariamente
    '''
    for n in range(int ((end_date - start_date).days)+1):
        yield start_date + timedelta(n)


@error_handler
def database (stations, start_date, end_date, *, db_folder='stations/stations'):
    '''
    Acessa arquivos do banco de dados.
    '''
    for single_station in stations:
        for single_date in datarange(start_date, end_date):
            file_path = '{db_folder}/{station}/{year}/{year}-{month}-{day}.txt.zip'.format(
             db_folder=db_folder,
             station=single_station,
             year=single_date.strftime('%Y'),
             month=single_date.strftime('%m'),
             day=single_date.strftime('%d'))
            yield(unpack_data(file_path))

@error_handler
def unpack_data(file_path):
    '''
    Descompacta o arquivo e prepara um DataFrame
    '''
    header = ['ESTACAO', 'LATITUDE', 'LONGITUDE', 'ALTITUDE', 'ANO', 'MES', 'DIA', 'HORA', 'TEMP', 'TMAX', 'TMIN',
     'UR','URMAX' , 'URMIN' , 'TD' , 'TDMAX' , 'TDMIN' , 'PRESSAONNM' , 'PRESSAONNM_MAX' , 'PRESSAONNM_MIN',
     'VELVENTO', 'DIRVENTO', 'VELVENTO_RAJADA', 'RADIACAO', 'PRECIPATACAO']

    station_df = pd.read_csv(file_path,header=None, delim_whitespace=True)
    station_df.columns = header
    return station_df


stations = ['A003', 'A014', 'A015', 'A011', 'A009']
start_date = date(2014, 10, 20)
end_date = date(2014, 10, 23)
for i in database(['A003'], start_date, end_date):
    if isinstance(i, pd.DataFrame):
        print(i.head())
