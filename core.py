from datetime import timedelta, date
import pandas as pd

def error_handler(function):
    '''
    Função de tratamento dos erros da função:
    TODO: Aprender dar um argumento de entrada no decorador pra customizar os erros por função
    '''
    def wrapper(*args, **kargs):
        try:
            return function(*args, **kargs)
        except Exception as e:
            print(e)
            return None
    return wrapper


def datarange(start_date, end_date)
    '''
    Faz loop entre duas datas, diariamente
    '''
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

@error_handler
def database (db_folder='stations/stations/'):
    '''
    Acessa arquivos do banco de dados.
    '''
    stations = []
    start_date = '1990-10-10'
    end_date = '1990-10-20'
    for single_station in stations:
        for single_date in datarange(start_date, end_date):
            file_path = '{station}/{year}/{year}-{month}-{day}.txt.zip'.format(station=single_station,
             year=single_date.strftime('%Y'),
             month=single_date.strftime('%m'),
             day=single_date.strftime('%d'))

def unpack_data():
