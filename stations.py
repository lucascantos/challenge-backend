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

def station_name():
    # Coluna 1 = Nome das estacoes = Pega o nome da cada pasta
    stations_list = os.listdir('stations/stations')
    return stations_list

def station_date(station):
    # Coluna2 = Data recente
    # abre pasta com o maior ano
    path = 'stations/stations/{}'.format(station)
    years = os.listdir(path)
    years = map(int,years)
    biggus = -1
    for year in years:
        biggus = year if year > biggus else biggus

    # Pegar uma lista de nome dos arquivos
    # remove o .txt.zip
    path = '{}/{}'.format(path, str(biggus))
    dates = os.listdir(path)
    latest = datetime(1800,1,1)
    for date in dates:
        try:
            # converte o restante pra pd_datetime ou date(YYYY,MM,DD)
            date = datetime.strptime(date[:-8], '%Y-%m-%d')
            latest = date if date > latest else latest
        except:
            # por hora, vou ignorar datas bugadas (IE: 30/02/20XX)
            pass
    # pega o arquivo mais velho
    return biggus, latest

def unpack_data(station,year, date):
    # Coluna3 = Hora recente
    # Abre o arquvio com a data mais recente
    file_path = 'stations/stations/{}/{}/{}.txt.zip'.format(station, year, date)
    header = ['ESTACAO', 'LATITUDE', 'LONGITUDE', 'ALTITUDE', 'ANO', 'MES', 'DIA', 'HORA', 'TEMP', 'TMAX', 'TMIN',
     'UR','URMAX' , 'URMIN' , 'TD' , 'TDMAX' , 'TDMIN' , 'PRESSAONNM' , 'PRESSAONNM_MAX' , 'PRESSAONNM_MIN',
     'VELVENTO', 'DIRVENTO', 'VELVENTO_RAJADA', 'RADIACAO', 'PRECIPATACAO']

    station_df = pd.read_csv(file_path, header=None, delim_whitespace=True)
    station_df.columns = header
    latest_time = station_df['HORA'][-1]
    print(latest_time)
    # converte a coluna ['HORA'] pra pd.to_datetime ou algo do tipo
    # pega o valor mais recente OU pega ultima linha


for station in station_name():
    try:    
        year, lastdate = station_date(station)
        lastdate = datetime.strftime(lastdate, '%Y-%m-%d')
        unpack_data('A003',year,lastdate)
        # TODO: Esse é um caso real onde pastas são criadas, mas não tem arquivo dentro?
        # Devo procurar o ultimo arquivo com dados ou posso confiar nas pastas e que os arquivos tem conteudo?
    except:
        pass
