# Backend Challenge

## Como participar
1. Crie um novo fork e branch com seu nome-sobrenome e faça um pull request quando estiver pronto, logo em seguida
marcaremos uma conversa. Não esqueça de nos fornecer uma maneira de entrar em contato.
2. Se precisar falar conosco pode entrar em contato via challenge@somar.io .

## Sobre o challenge
Para manter uma porta de entrada legal, queremos deixar esse pequeno passatempo em forma de desafio para descobrir um
pouco sobre o seu conhecimento técnico, práticas de implementação, organização do projeto, foco em performance, teste
unitários, e o mais importante de tudo: apresentar uma solução plausível para o problema.

O céu é o limite, então faça o projeto em uma arquitetura que seja suficiente para resolver o problema, lembrando que a
aplicação deve ser plenamente funcional.

## Entregáveis
O desafio consiste nos seguintes componentes:
* _Banco De Dados_
* Queue
* Consumer
* API
* S3 (Qualquer solução de "simple storage service" desde que seja da AWS :smiley:)

Qual linguagem? Python, NodeJS ou Go.

## Sugestões
Devido a nossa característica de trabalho atual seria interessante se utilizasse tecnologias disponíveis na plataforma
do Google ou Amazon, já que esse é o nosso cenário mais provável, porém se quiser utilizar o heroku pode, container
pode, afinal o importante é funcionar.


## Especificações
A ideia é dar um _overview_ de como esperamos que seja entregue cada componente, lembre-se, são somentes sugestões de
implementação, não se trata de uma restrição.


#### API (Nome artístico: Stratus)
Deve obrigatoriamente permitir as seguintes interações:
* Consultar quais as estações disponíveis para consulta. É um diferencial realizar consultas utilizando
filtros como: código da estação, data/hora - além de possuir parâmetros nesses campos.

* Solicitar o processamento de um arquivo, isto é, realizar o fluxo de trabalho completo da aplicação.

* Consultar quantos/quais trabalhos estão na queue no momento.

#### Queue
Não tem muito o que falar - tu vai utilizar a queue para agregar o serviço e realizar o trabalho, nesse caso é
obrigatório que utilize um serviço de Queue, se quiser citar as tecnologias e como faria sem esse cara aqui, fique a
vontade.

#### Consumer
O trabalho desse consumer é simples: Pegar o arquivo solicitado descompactar o conteúdo e realizar o upload para o S3.

#### S3
Armazenar o arquivo? Bem, você pode adicionar as configurações que entender como necessárias e que seriam escaláveis para
 um bucket maior.

#### Banco De Dados
O **Banco De Dados**, na verdade são arquivos disponibilizados, dependendo da sua arquitetura ele pode ser uma pasta
física da API ou outro bucket do S3, que a API possui acesso para consultar e criar os processos de descompactação dos
arquivos.
   A pasta deve conter os arquivos no seguinte modelo:
 
   * A506/2019/2019-01-01.txt.zip /{estação}/{ano}/{YYYY-MM-DD}.txt.zip
   * A506/2019/2019-01-02.txt.zip
   * A506/2019/2019-01-03.txt.zip
   * A506/2019/2019-01-04.txt.zip

O conteúdo dos arquivos está me anexo na pasta _stations_ - As colunas dos arquivos respeitam os seguintes cabeçalhos:

|  ESTAÇÃO | LATITUDE  | LONGITUDE  | ALTITUDE  | ANO  | MES  | DIA  | HORA  | TEMP(C)  | TMAX(C)  | TMIN(C)  | UR(%) |
|---|---|---|---|---|---|---|---|---|---|---|---|

- TEMP: Temperatura
- TMAX: Temperatura Máxima
- TMIN: Temperatura Minima
- UR: Umidade Relativa

| URMAX(%)  | URMIN(%)  | TD(C)  | TDMAX(C)  | TDMIN(C)  | PRESSAONNM(hPa)  | PRESSAONNM_MAX(hPa)  | PRESSAONNM_MIN(hPa)  
|---|---|---|---|---|---|---|---|

- URMAX: Umidade Relativa Máxima
- URMIN: Umidade Relativa Minima
- UR: Umidade Relativa
- TD: Temperatura Ponto de Orvalho
- TDMAX: Temperatura Ponto de Orvalho Máxima
- TDMIN: Temperatura Ponto de Orvalho Mínima
- PRESSAONNM: Pressão Nominal
- PRESSAONNM_MAX: Pressão Nominal Máxima
- PRESSAONNM_MIN: Pressão Nominal Minima

| VELVENTO(m/s)  | DIR(°) | VENTO_RAJADA(m/s) | RADIACAO(Kjm²) | PRECIPATACAO(mm)
|---|---|---|---|---|

- VELVENTO: Velocidade do Vento
- DIR: Direção do vento (De norte = 360° ou 0°, de leste=90°)
- VENTO_RAJADA: Velocidade do vento rajada

**A sequência é exatamente a exposta acima.**

#### Core
Como o processo em si deve funcionar?

Uma solicitação de arquivo será enviado para a API com os dados do arquivos e um link de postback para que quando o
processo seja finalizado haja uma notificação. Na resposta dessa solicitação deve ser informado o jobid do processo na
Queue.

No postback deve ser enviado os dados do arquivo solicitado, juntamente com o link de acesso do arquivo para o S3.


##### Diferenciais
A ideia não é levantar uma super estrutura, sendo assim, se você cobrir um endpoint para cada item da lista já poderemos
 ver em ação as ideias solicitadas.
* Documentação
* Testes unitários/funcionais.
* Monitoramento
* Diagrama da aplicação.


Por favor, inclua suas considerações do em um arquivo de texto ou markdown.

**May the Force be with you!**

w6kgdW0gdGlwbyBkZSBudXZlbSBxdWUgY29icmUgdW1hIGFyZWEgZ3JhbmRlIGlndWFsIGVzc2UgcHJvamV0bwo