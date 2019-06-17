from flask import Flask
from core import core_table
from stations import stations_available


stratus_app = Flask(__name__)

@stratus_app.route('/stations')
def stations():
    '''
    Consultar quais as estações disponíveis para consulta. 
    É um diferencial realizar consultas utilizando filtros como: 
    código da estação, data/hora - além de possuir parâmetros nesses campos.
    '''
    count = 0
    station_list = []
    check_stations = stations_available()
    for station in check_stations.station_latest():
        station_list.append(station)
        count+=1
    output = dict(count=count, stations=station_list)
    return output

@stratus_app.route('/postback')
def postback():
    stations=[]
    for stations in station:
        query_dataframe = core_table(station, start_date, end_date)
        

    '''
    Solicitar o processamento de um arquivo,
    isto é, realizar o fluxo de trabalho completo da aplicação.
    '''

@stratus_app.route('/queue')
def queue():
    pass
    ''' 
    Consultar quantos/quais trabalhos estão na queue no momento.
    '''