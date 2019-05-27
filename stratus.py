from flask import Flask


stratus_app = Flask(__name__)

@stratus_app.route("/stations")
def hello():
    '''
    Consultar quais as estações disponíveis para consulta. 
    É um diferencial realizar consultas utilizando filtros como: 
    código da estação, data/hora - além de possuir parâmetros nesses campos.
    '''
    pass




'''
Solicitar o processamento de um arquivo,
 isto é, realizar o fluxo de trabalho completo da aplicação.
'''

''' 
Consultar quantos/quais trabalhos estão na queue no momento.
'''