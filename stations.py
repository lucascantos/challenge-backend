'''
Consultar quais as estações disponíveis para consulta. 
É um diferencial realizar consultas utilizando filtros como: 
código da estação, data/hora - além de possuir parâmetros nesses campos.
'''

import os
from time import time
from datetime import datetime
import pandas as pd

def timer(function):
    def wrapper(*args, **kwargs):
        before = time()
        function(*args, **kwargs)
        after = time()
        print('Elapsed: {}s'. format(after-before))
    return wrapper

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
            # print(e)
            pass
    return wrapper


class stations_available(object):
    def __init__(self):
        self.dir = 'stations/stations'

        self.header = ['ESTACAO', 'LATITUDE', 'LONGITUDE', 'ALTITUDE', 'ANO', 'MES', 'DIA', 'HORA', 'TEMP', 'TMAX', 'TMIN',
        'UR','URMAX' , 'URMIN' , 'TD' , 'TDMAX' , 'TDMIN' , 'PRESSAONNM' , 'PRESSAONNM_MAX' , 'PRESSAONNM_MIN',
        'VELVENTO', 'DIRVENTO', 'VELVENTO_RAJADA', 'RADIACAO', 'PRECIPATACAO']


    def station_names(self):
        # Coluna 1 = Nome das estacoes = Pega o nome da cada pasta
        self.stations_list = os.listdir('stations/stations')

    def station_year(self, station):
        # Coluna2 = Data recente
        # abre pasta com o maior ano
        self.station = station
        self.path = '{}/{}'.format(self.dir, self.station)
        years = os.listdir(self.path)
        years = map(int,years)
        self.lastest_year = -1
        for year in years:
            self.lastest_year = year if year > self.lastest_year else self.lastest_year

        # Pegar uma lista de nome dos arquivos
        # remove o .txt.zip
    def station_date(self):
        self.path = '{}/{}'.format(self.path, str(self.lastest_year))
        dates = os.listdir(self.path)
        self.latest_date = datetime(1800,1,1)
        for date in dates:
            try:
                # converte o restante pra pd_datetime ou date(YYYY,MM,DD)
                date = datetime.strptime(date[:-8], '%Y-%m-%d')
                self.latest_date = date if date > self.latest_date else self.latest_date
            except:
                # por hora, vou ignorar datas bugadas (IE: 30/02/20XX)
                pass
        # pega o arquivo mais velho
    
    def station_hour(self, df):
        '''
        Abre um dataframe do banco de dados e tira a ultima horade registro
        '''
        self.latest_hour = df['HORA'].iloc[-1]

    def station_latest(self):
        self.latest_data = {
            'station': self.station,
            'date': self.latest_date,
            'hour': self.latest_hour
        }

    def unpack_data(self,station,year,date):
        # Coluna3 = Hora recente
        # Abre o arquvio com a data mais recente
        file_path = '{}/{}/{}/{}.txt.zip'.format(self.dir, station, year, date)

        header = ['ESTACAO', 'LATITUDE', 'LONGITUDE', 'ALTITUDE', 'ANO', 'MES', 'DIA', 'HORA', 'TEMP', 'TMAX', 'TMIN',
        'UR','URMAX' , 'URMIN' , 'TD' , 'TDMAX' , 'TDMIN' , 'PRESSAONNM' , 'PRESSAONNM_MAX' , 'PRESSAONNM_MIN',
        'VELVENTO', 'DIRVENTO', 'VELVENTO_RAJADA', 'RADIACAO', 'PRECIPATACAO']
        station_df = pd.read_csv(file_path, header=None, delim_whitespace=True)
        station_df.columns = header
        return station_df

        # converte a coluna ['HORA'] pra pd.to_datetime ou algo do tipo
        # pega o valor mais recente OU pega ultima linha




@error_handler
def teste(disp):
    disp.station_year(i)
    disp.station_date()
    df = disp.unpack_data(i, disp.lastest_year, datetime.strftime(disp.latest_date, '%Y-%m-%d'))
    disp.station_hour(df)
    disp.station_latest()
    print(disp.latest_data)


disp = stations_available()
disp.station_names()
for i in disp.stations_list:
    teste(disp)


# for station in station_name():
#     try:    
#         year, lastdate = station_date(station)
#         lastdate = datetime.strftime(lastdate, '%Y-%m-%d')
#         unpack_data(station,year,lastdate)
#         # TODO: Esse é um caso real onde pastas são criadas, mas não tem arquivo dentro?
#         # Devo procurar o ultimo arquivo com dados ou posso confiar nas pastas e que os arquivos tem conteudo?
#     except:
#         pass
