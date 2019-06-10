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
    TODO 1 : Aprender dar um argumento de entrada no decorador pra customizar os erros por função
    TODO: Depois disso, fazer o log com os erros
    TODO 1: Adicionar um novo wrapper pra adiconar argumento
    '''
    def wrapper(*args, **kargs):
        try:
            return function(*args, **kargs)
        except Exception as e:
            # print(e)
            return
    return wrapper


class stations_available(object):
    def __init__(self, station=None, date=None, hour=None):
        '''
        Cria uma lista de estações disponiveis.
        station: filtra os dados apenas para a estação desejada
        date: filtro para a data desejada
        hour: filtro para a hora desejada

        return: Um gerador entendo a estação, data do arquivo e valor da ultima hora registrada. 
        '''
        self.station_filter = station
        self.date_filter = date
        self.hour_filter = hour

        
        # self.output = pd.DataFrame(columns=['stations', 'date'])
        # Diretorio base dos arquivos. Header dos dados de cada arquivo de acordo com o INMET
        self.dir = 'stations/stations'
        self.header = ['ESTACAO', 'LATITUDE', 'LONGITUDE', 'ALTITUDE', 'ANO', 'MES', 'DIA', 'HORA', 'TEMP', 'TMAX', 'TMIN',
        'UR','URMAX' , 'URMIN' , 'TD' , 'TDMAX' , 'TDMIN' , 'PRESSAONNM' , 'PRESSAONNM_MAX' , 'PRESSAONNM_MIN',
        'VELVENTO', 'DIRVENTO', 'VELVENTO_RAJADA', 'RADIACAO', 'PRECIPATACAO']

    def check_date(self):
        '''
        Converte uma data de String para datetime do Python.
        essa passagem do Pandas é por ele ja trata parte do regex
        '''
        if not isinstance(self.date_filter, datetime):
            self.date_filter = pd.to_datetime(self.date_filter, dayfirst=True)
            self.date_filter = self.date_filter.to_pydatetime()
   
    def station_name(self,folder):
        '''
        Devolve o nome da estação. Filtra os dados por estação.
        folder: string contendo o caminho {BaseDir}/{Station}/{year}
        '''
        station_name = folder[0][-9:-5]
        if self.station_filter == None:
            return station_name
        elif station_name == self.station_filter:
            return station_name

    @error_handler
    def station_date(self, file):
        '''
        Converte a data do arquivo pra datetime. Filtra os dados por data
        file: String contendo {nome_do_arquivo}.txt.zip
        '''
        # TODO: Error handler pra datas zuadas tipo 31/02/20XX
        
        date = datetime.strptime(file[:-8], '%Y-%m-%d')
        if self.date_filter == None:
            # Ele puxa a hora se o arquivo existe e ja adiciona na data
            latest_hour = self.station_hour('{}/{}'.format(self.path, file))
            date = date.replace(hour=latest_hour)
            return date
        elif date == self.date_filter:
            latest_hour = self.station_hour('{}/{}'.format(self.path, file))
            date = date.replace(hour=latest_hour)
            return date


    def station_hour(self, file):
        '''
        Abre arquivo desejado e puxa o horario desejado. ultimo horario caso não haja filtro
        '''
        df = self.unpack_data(file)
        if self.hour_filter == None:
            latest_hour = df['HORA'].max()
            return latest_hour
        # toda essa patifaria pra checar se a hora realmente existe dentro do arquivo. Ja garante perda de dados.
        elif self.hour_filter == int(df['HORA'][df['HORA'] == latest_hour].iloc[0]):
            return self.hour_filter            

    @error_handler
    def station_latest(self):
        '''
        Lê no banco de dados e retorna todos os arquivos que contem os dados requisitados
        '''
        # Arruma a data do filtro
        if self.date_filter != None:
            self.check_date()

        # Abre todas as subpastas do diretorio base
        working_list = os.walk(self.dir)
        for folder in working_list:
            # Filtro de pastas vazias/sem arquivos. Checa se pasta possui arquivos dentro.
            if folder[2]:

                # Puxa o nome da estação. Cria o caminho pra ele    
                self.station = self.station_name(folder)            
                self.path = folder[0]
                
                # Filtro de estação.
                if self.station != None:
                    
                    # Limpa e filtra data e hora
                    self.latest_date = None
                    for file in folder[2]:
                        self.latest_date = self.station_date(file)
                        if self.latest_date != None:

                            self.latest_data = {
                                'station': self.station,
                                'date': self.latest_date
                            }
                            yield self.latest_data



    def unpack_data(self,file):
        '''
        Abre um arquivo desejado

        return: DataFrame, caso exista.
        '''
        # TODO: so de abrir um pandas, o demora 11x mais. Tentar evitar essa etapa de checagem de arquivo
        #       Em teste rudimentar, usando o getsize > 198, demora 4x mais. Meio bruto
        # TODO: depois que mexer no error handle, tirar esse IF e chamar a função no error_handler

        if self.check_file(file):
            station_df = pd.read_csv(file, header=None, delim_whitespace=True)
            station_df.columns = self.header
            return station_df

        # converte a coluna ['HORA'] pra pd.to_datetime ou algo do tipo
        # pega o valor mais recente OU pega ultima linha

        #O Error checa se o arquivo existe ou não
    
    def check_file(self,file):
        non_empty_file = True if os.path.getsize(file)>198 else False
        return non_empty_file
        

@timer
def teste():
    count = 0
    disp = stations_available(station='A003')
    for i in disp.station_latest():  
        print(i)      
        count +=1
    print(count)


teste()