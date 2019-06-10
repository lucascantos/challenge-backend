from datetime import timedelta, date
import pandas as pd

import os.path
from zipfile import ZipFile

def error_handler(function):
    '''
    Função de tratamento dos erros da função:
    TODO: Aprender dar um argumento de entrada no decorador pra customizar os erros por função
    TODO: Depois disso, fazer o log com os erros
    '''
    def wrapper(*args, **kargs):
        try:
            return function(*args, **kargs)
        except Exception as e:
            print(e)
            pass
    return wrapper

class core_table(object):
    def __init__(self,stations, start_date, end_date):
        self.stations = stations
        self.start_date = start_date
        self.end_date = end_date

        self.header = ['ESTACAO', 'LATITUDE', 'LONGITUDE', 'ALTITUDE', 'ANO', 'MES', 'DIA', 'HORA', 'TEMP', 'TMAX', 'TMIN',
        'UR','URMAX' , 'URMIN' , 'TD' , 'TDMAX' , 'TDMIN' , 'PRESSAONNM' , 'PRESSAONNM_MAX' , 'PRESSAONNM_MIN',
        'VELVENTO', 'DIRVENTO', 'VELVENTO_RAJADA', 'RADIACAO', 'PRECIPATACAO']

    def datarange(self):
        '''
        Faz loop entre duas datas, diariamente.
        yield: uma data dentro do periodo
        '''
        for one_day in range(int ((self.end_date - self.start_date).days)+1):
            yield self.start_date + timedelta(one_day)


    @error_handler
    def make_file_path (self, *, db_folder='stations/stations'):
        '''
        Cria o caminho do arquivo a ser aberto.
        '''
        for single_station in self.stations:
            for single_date in self.datarange():
                self.file_path = '{db_folder}/{station}/{year}/{year}-{month}-{day}.txt.zip'.format(
                db_folder=db_folder,
                station=single_station,
                year=single_date.strftime('%Y'),
                month=single_date.strftime('%m'),
                day=single_date.strftime('%d'))
                yield self.file_path

    @error_handler
    def unpack_data(self):
        '''
        Descompacta o arquivo e prepara um DataFrame
        '''
        for file_path in self.make_file_path():
            station_df = pd.read_csv(file_path,header=None, delim_whitespace=True)
            station_df.columns = self.header
            yield station_df


stations = ['A003']
start_date = date(2015, 12, 31)
end_date = date(2014, 10, 23)
x = core_table(['A002'], start_date, start_date)
for i in x.unpack_data():
    # Ve se o objeto encontrado é um dataframe
    if isinstance(i, pd.DataFrame):
        print(i['HORA'])
