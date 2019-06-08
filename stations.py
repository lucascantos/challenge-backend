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
    TODO 2: Adicionar um novo wrapper pra adiconar argumento
    '''
    def wrapper(*args, **kargs):
        try:
            return function(*args, **kargs)
        except Exception as e:
            #print(e)
            return
    return wrapper


class stations_available(object):
    def __init__(self, station=None, date=None, hour=None):
        self.station_filter = station
        self.date_filter = date
        self.hour_filter = hour


        self.dir = 'stations/stations'

        self.header = ['ESTACAO', 'LATITUDE', 'LONGITUDE', 'ALTITUDE', 'ANO', 'MES', 'DIA', 'HORA', 'TEMP', 'TMAX', 'TMIN',
        'UR','URMAX' , 'URMIN' , 'TD' , 'TDMAX' , 'TDMIN' , 'PRESSAONNM' , 'PRESSAONNM_MAX' , 'PRESSAONNM_MIN',
        'VELVENTO', 'DIRVENTO', 'VELVENTO_RAJADA', 'RADIACAO', 'PRECIPATACAO']
    @error_handler
    def station_date(self, file):
        self.station_hour('{}/{}'.format(self.path, file))
        # converte o restante pra pd_datetime ou date(YYYY,MM,DD)
        date = datetime.strptime(file[:-8], '%Y-%m-%d')
        if self.date_filter == None:
            if date > self.latest_date:
                self.latest_date = date
        elif date == self.date_filter:
            self.latest_date = date        
        self.latest_date  = self.latest_date.replace(hour=self.latest_hour)

            # O error cheka se a data existe

    def station_hour(self, file):
        '''
        Abre um dataframe do banco de dados e tira a ultima hora de registro
        '''
        df = self.unpack_data(file)
        if self.hour_filter == None:
            self.latest_hour = df['HORA'].max()
        else:
            self.latest_hour = df['HORA'][df['HORA'] == self.hour_filter].iloc[0]

        #print(self.latest_date)
        
        # O error cheka se exisem dados nesse arquivo
    @error_handler
    def station_latest(self):
        '''
        Resultado final na forma de Dictionary
        '''

        working_list = os.walk(self.dir, False)
        for folder in working_list:
            if folder[2]:
                # Admitindo que a estrutura de pastas será sempre assim
                # Admitindo que o walk sempre vai fazer de forma ordenada
              
                self.station = folder[0][-9:-5]            
                self.path = folder[0]
                self.latest_date = datetime(1800,1,1)

                for file in folder[2]:
                    self.station_date(file)

                if self.latest_date != datetime(1800,1,1):
                    self.latest_data = {
                        'station': self.station,
                        'date': self.latest_date
                    }

                    yield self.latest_data

    def unpack_data(self,file):
        # Coluna3 = Hora recente
        # Abre o arquvio com a data mais recente

        station_df = pd.read_csv(file, header=None, delim_whitespace=True)
        station_df.columns = self.header
        return station_df

        # converte a coluna ['HORA'] pra pd.to_datetime ou algo do tipo
        # pega o valor mais recente OU pega ultima linha

        #O Error checa se o arquivo existe ou não

@timer
def teste():
    disp = stations_available(date='2019-10-01')
    for i in disp.station_latest():
        print(i)


teste()



# for station in station_name():
#     try:    
#         year, lastdate = station_date(station)
#         lastdate = datetime.strftime(lastdate, '%Y-%m-%d')
#         unpack_data(station,year,lastdate)
#         # TODO: Esse é um caso real onde pastas são criadas, mas não tem arquivo dentro?
#         # Devo procurar o ultimo arquivo com dados ou posso confiar nas pastas e que os arquivos tem conteudo?
#     except:
#         pass
