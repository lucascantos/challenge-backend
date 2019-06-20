from flask import Flask, request
from core import core_table
from stations import stations_available
import pandas as pd


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
    stations = request.args.get('station')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # TODO: Checkar arquivo antes de rodar


    stations_data = []
    for station_name in stations:
        query_dataframe = core_table(station_name, start_date, end_date)
        station_data = pd.DataFrame()
        for date in query_dataframe.unpack_data():
            station_data.append(date, ignore_index=True)
        station_dict = dict(station=station_name, data=station_data)
        stations_data.append(station_dict)
    return stations_data
        

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