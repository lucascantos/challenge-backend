'''
Banco De Dados
O **Banco De Dados**, na verdade são arquivos disponibilizados, dependendo da sua arquitetura ele pode ser uma pasta
física da API ou outro bucket do S3, que a API possui acesso para consultar e criar os processos de descompactação dos
arquivos.
'''

from apiclient.discovery import build
from httplib2 import Http
from oauth2client import client, tools
from oauth2client.file import Storage
from pprint import pprint
import uuid

from io import BytesIO
import pandas as pd

class google_drive_stations(object):
    def __init__(self, file_name):
        self.file_name = file_name

        pass

    def authorization (self):

        scopes = [
            'https://www.googleapis.com/auth/drive.readonly',
            'https://www.googleapis.com/auth/spreadsheets.readonly'
            ]
        # esse Storage é criado, se não existir, pra não ter que ficar toda hora pedindo permissão
        store = Storage('credentials/storage.json')
        client_secret_file = 'credentials/client_secret.json'
        self.credz = store.get()
        if not self.credz or self.credz.invalid:
            flow = client.flow_from_clientsecrets(client_secret_file, scopes)
            self.credz = tools.run_flow(flow, store)

        # Cria os serviços de Drive e Slides        
        self.drive_services = build('drive', 'v3', http=self.credz.authorize(Http()))
        #self.sheets_services = build('spreadsheets', 'v4', http=self.credz.authorize(Http()))

    def file_find(self):
        file_id = self.drive_services.files().list(q = "name='{}'".format(self.file_name)).execute()['files'][0]
        # return self.drive_services.files().get_media(fileId=file_id['id']).execute()
        file_uri = self.drive_services.files().get_media(fileId=file_id['id']).uri
        credz_token = self.credz.access_token
        return ('{}&access_token={}'.format(file_uri, credz_token))


def teste():
    my_file = google_drive_stations("2016-12-31.txt.zip")
    my_file.authorization()
    x = my_file.file_find()

    df = pd.read_csv(x,header=None, delim_whitespace=True, compression='zip')

    print(df)

teste()