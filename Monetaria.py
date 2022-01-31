# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 19:51:56 2022

@author: lucas
"""

'-------------------------------------------------------------------------------'

'Ativos totais = ativo circulante (liquidáveis no curto prazo) + ativo não circulante (liquidáveis no longo prazo) + ativo permanente (patrimônio imobilizado);'

'Passivos totais = passivo circulante (exigíveis no curto prazo) + passivo não circulante (exigíveis no longo prazo);'

'Vale notar que o patrimônio líquido é sempre a diferença entre ativos e passivos totais. Assim, o grau de endividamento corresponde à proporção percentual dos ativos sobre os passivos, segundo a fórmula:'

'-------------------------------------------------------------------------------'

'Grau de endividamento = (passivos totais / ativos totais) x 100'

'-------------------------------------------------------------------------------'

# Endividamento geral
# O índice de endividamento geral apresenta em percentual quanto dos ativos totais estão comprometidos por crédito. Obtém-se o valor a partir da fórmula:

# Endividamento geral = (capital de terceiros / ativos totais) x 100

# Composição do endividamento
# Esse indicador permite saber quanto dos passivos totais as despesas de curto prazo representam. O percentual é dado pela fórmula:

# Composição do endividamento = (passivo circulante / passivos totais) x 100

# Liquidez corrente
# O cálculo de liquidez corrente gera um valor que representa a capacidade da empresa em manter suas operações no período. A fórmula do indicador é a seguinte:

# Liquidez corrente = ativo circulante / passivo circulante

'-------------------------------------------------------------------------------'

# from openpyxl import Workbook

# data = Workbook()
# sheet = data.active
# sheet.title = "Gasto"

def vec(x):
    a = []
    for i in range(x):
        a = a + [[]]
    return a

def rest(x,y):
    s = x
    if y<=x:
        k = 1
        while k*y<x+1:
            k = k+1
        s = x-(k-1)*y
    return s

def binar(x,y):
    c = 0
    while y**c<=x:
        c = c+1
    c = c-1
    # print(c)
    # print(y**c)
    vect = vec(c+1)
    if x == 0: 
        vect = [0]
    else: 
        for i in range(c+1):
            vect[i] = int(x/(y**(c-i)))
            x = x-(vect[i])*(y**(c-i))
    return vect


def search(k,x):
    vr = [[0]]
    l = len(x)
    for i in range(len(k)):
        if k[i:i+l] == x:
            vr[len(vr)-1] = vr[len(vr)-1] + [i-1]
            vr = vr + [[i+l+1]]
    return vr

'MONTANDO A TABELA EM TXT'

print('Ler Planilha: ')
k = open(r'ipo_geral.csv').read()

lines = 0
cell = 0
print('type(k)')
print(type(k))

sep = 0
while k[sep]!= ';':
    sep = sep + 1
for i in range(len(k)):
    if k[i] == ';':
        cell = cell + 1
    if k[i:i+1] == '\n':
        lines = lines + 1
print(lines)
print(cell)
print(cell/lines)

col = int(cell/lines)

# for i in range(col):
#     for j in range(lines):
    
n = 0    
def celu(k,x):
    if k[x] == ';':
        if k[x+1] == ';':
            print('nenhum')
        else:
            i = 1
            while k[x+i] != ';' and k[x+i:x+i+1] != '\n':
                i = i+1
            print(k[x+1:x+i])

# def montar():
look_1 = search(k,'\n')
# global data
# data = vec(lines)
# for i in range(len(data)):
#     data[i] = vec(col)
data = []
for i in range(len(look_1)-2):
    data = data + [k[look_1[i][1]+2:look_1[i+1][1]+1]]
data = [k[look_1[0][0]:look_1[0][1]+1]] + data
# montar()
    
c = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == ';' or data[i][j] == '\n':
            c = c + [[i,j]]
            
# supdata = vec(lines)
# for i in range(len(supdata)):
#     supdata[i] = vec(col-1)
# for i in range(len(data)):
#     for j in range(col-1):
#         supdata[i][j] = data[c[i][0]][c[j][1]+1:c[j+1][1]]

supdata = vec(len(c))
for i in range(len(c)-1):
    supdata[i] = data[c[i][0]][c[i][1]+1:c[i+1][1]]


dados = vec(lines)
for i in range(len(dados)):
    dados[i] = vec(col)
for i in range(len(supdata)):
    linha = int(i/(col)) 
    coluna = rest(i,col)
    dados[linha][coluna] = supdata[i]

# Você pode encontrar no site de RI da empresa, geralmente fica na aba “divulgação de resultado”, ou no site da B3: http://www.b3.com.br/pt_br/

# No site da B3 você procura a empresa desejada pelo nome ou ticker, depois clique em “saiba mais”, e por ultimo em “relatórios estruturados” e você terá as informações trimestrais – ITR -, e o balanço de todo o ano através da demonstrações financeiras padronizadas – DFP.

 

# Espero ter ajudado. Sucesso nos investimentos!
'------------------------------------------------------------------------------'

#dados[2] - Nome da informação

'0 NOME DE PREGÃO'
'1 LISTAGEM NA OFERTA'
'2 CLASSIFICAÇÃO SETORIAL (SEGMENTO)'
'3 COORDENADOR LÍDER'
'4 CLASSIFICAÇÃO'
'5 TIPO'
'6 FIXAÇÃO DE PREÇO'
'7 PREÇO POR AÇÃO / UNIT / BDR (LÇTO.)4'
'8 INÍCIO DE NEGOCIAÇÃO'
'9 Nº DE PESSOAS FÍSICAS'
'10 Nº TOTAL DE INVESTIDORES '
'11 VOLUME PRIMÁRIA (R$) '
'12 VOLUME SECUNDÁRIA (R$) '
'13 VOLUME TOTAL (R$)'
'14 VAREJO'
'15 INSTITUCIONAL'
'16 ESTRANGEIROS'
'17 OUTROS'


'19 ANO'
'20 IPO'
'21 FOLLOW-ON'

'------------------------------------------------------------------------------'
'Funcoes de pesquisa'

def nome():
    k = []
    for i in range(len(dados)-2):
        j = i+2
        k = k + [dados[j][0]]
    return k
def listagem():
    k = []
    for i in range(len(dados)-2):
        j = i+2
        k = k + [dados[j][1]]
    return k
def classificacao():
    k = []
    for i in range(len(dados)-2):
        j = i+2
        k = k + [dados[j][2]]
    return k
def coordenador():
    k = []
    for i in range(len(dados)-2):
        j = i+2
        k = k + [dados[j][3]]
    return k
def classific():
    k = []
    for i in range(len(dados)-2):
        j = i+2
        k = k + [dados[j][4]]
    return k
def tipo():
    k = []
    for i in range(len(dados)-2):
        j = i+2
        k = k + [dados[j][5]]
    return k
def preco_fixo():
    k = []
    for i in range(len(dados)-2):
        j = i+2
        k = k + [dados[j][6]]
    return k
def preco_un():
    k = []
    for i in range(len(dados)-2):
        j = i+2
        k = k + [dados[j][7]]
    return k
def data_inicio():
    k = []
    for i in range(len(dados)-2):
        j = i+2
        k = k + [dados[j][8]]
    return k
def num_pf():
    k = []
    for i in range(len(dados)-2):
        j = i+2
        k = k + [dados[j][9]]
    return k
def num_invest():
    k = []
    for i in range(len(dados)-2):
        j = i+2
        k = k + [dados[j][10]]
    return k
def vol_prim():
    k = []
    for i in range(len(dados)-2):
        j = i+2
        k = k + [dados[j][11]]
    return k
def vol_sec():
    k = []
    for i in range(len(dados)-2):
        j = i+2
        k = k + [dados[j][12]]
    return k
def vol_total():
    k = []
    for i in range(len(dados)-2):
        j = i+2
        k = k + [dados[j][13]]
    return k
def varejo():
    k = []
    for i in range(len(dados)-2):
        j = i+2
        k = k + [dados[j][14]]
    return k
def instit():
    k = []
    for i in range(len(dados)-2):
        j = i+2
        k = k + [dados[j][15]]
    return k
def estrang():
    k = []
    for i in range(len(dados)-2):
        j = i+2
        k = k + [dados[j][16]]
    return k
def outros():
    k = []
    for i in range(len(dados)-2):
        j = i+2
        k = k + [dados[j][17]]
    return k
    k = []
    for i in range(len(dados)-2):
        j = i+2
        k = k + dados[j][17]
    return k

# m = ['nome',  'listagem',  'classificacao',  'coordenador',  'classific',  'tipo',  'preco_fixo',  'preco_un',  'data_inicio',  'num_pf',  'num_invest',  'vol_prim',  'vol_sec',  'vol_total',  'varejo',  'instit',  'estrang',  'outros']
'------------------------------------------------------------------------------'

m = []
for i in range(len(nome())):
    if classific()[i] == "'IPO'":
        m = m + [[nome()[i],data_inicio()[i]]]


quote = [['NATURA', '26/05/04'],  2,  ['GOL', '24/06/04'],  2,  ['ALL AMER LAT', '25/06/04'],  2,  ['CPFL ENERGIA', '29/09/04'],  2,  ['GRENDENE', '29/10/04'],  1,  ['DASA', '19/11/04'],  3,  ['PORTO SEGURO', '22/11/04'],  2,  ['RENAR', '28/02/05'],  1,  ['SUBMARINO', '30/03/05'],  2,  ['LOCALIZA', '23/05/05'],  3,  ['TAM S/A', '14/06/05'],  2,  ['ENERGIAS BR', '13/07/05'],  3,  ['OHL BRASIL', '15/07/05'],  1,  ['NOSSA CAIXA', '28/10/05'],  1,  ['COSAN', '18/11/05'],  1,  ['UOL', '16/12/05'],  1,  ['COPASA', '08/02/06'],  2,  ['VIVAX', '08/02/06'],  1,  ['GAFISA', '17/02/06'],  2,  ['COMPANY', '02/03/06'],  1,  ['TOTVS', '09/03/06'],  3,  ['EQUATORIAL', '03/04/06'],  2,  ['ABNOTE', '27/04/06'],  1,  ['CSU CARDSYST', '02/05/06'],  1,  ['BRASILAGRO', '02/05/06'],  2,  ['LUPATECH', '15/05/06'],  1,  ['GP INVEST ¹', '01/06/06'],  2,  ['DATASUL', '02/06/06'],  1,  ['MMX MINER', '24/07/06'],  1,  ['ABYARA', '27/07/06'],  1,  ['MEDIAL SAUDE', '22/09/06'],  1,  ['KLABINSEGALL', '09/10/06'],  1,  ['SANTOS BRAS', '13/10/06'],  1,  ['MDIASBRANCO', '18/10/06'],  1,  ['BRASCAN RES', '23/10/06'],  1,  ['PROFARMA', '26/10/06'],  1,  ['TERNA PART', '27/10/06'],  1,  ['ECODIESEL', '22/11/06'],  1,  ['ODONTOPREV', '01/12/06'],  1,  ['POSITIVO INF', '11/12/06'],  1,  ['LOPES BRASIL', '18/12/06'],  3,  ['DUFRYBRAS', '20/12/06'],  1,  ['PDG REALT', '26/01/07'],  4,  ['RODOBENSIMOB', '31/01/07'],  1,  ['CC DES IMOB', '31/01/07'],  1,  ['TECNISA', '01/02/07'],  2,  ['IGUATEMI', '07/02/07'],  3,  ['SAO MARTINHO', '12/02/07'],  1,  ['GVT HOLDING', '16/02/07'],  1,  ['ANHANGUERA', '12/03/07'],  4,  ['JBS', '29/03/07'],  2,  ['PINE', '02/04/07'],  1,  ['EVEN', '02/04/07'],  2,  ['BR MALLS PAR', '05/04/07'],  4,  ['FER HERINGER', '12/04/07'],  1,  ['JHSF PART', '12/04/07'],  3,  ['METALFRIO', '13/04/07'],  1,  ['BEMATECH', '19/04/07'],  1,  ['CR2', '23/04/07'],  1,  ['AGRA INCORP', '26/04/07'],  1,  ['CREMER', '30/04/07'],  1,  ['WILSON SONS', '30/04/07'],  1,  ['SOFISA', '02/05/07'],  1,  ['TARPON', '31/05/07'],  1,  ['INPAR S/A', '06/06/07'],  2,  ['PARANA', '14/06/07'],  1,  ['SLC AGRICOLA', '15/06/07'],  2,  ['LOG-IN', '21/06/07'],  2,  ['EZTEC', '22/06/07'],  2,  ['CRUZEIRO SUL', '26/06/07'],  2,  ['DAYCOVAL', '29/06/07'],  1,  ['MARFRIG', '29/06/07'],  4,  ['TEGMA', '03/07/07'],  1,  ['INDUSVAL', '12/07/07'],  1,  ['REDECARD', '13/07/07'],  3,  ['INVEST TUR', '16/07/07'],  1,  ['MINERVA', '20/07/07'],  3,  ['PATAGONIA ¹', '20/07/07'],  1,  ['MRV', '23/07/07'],  2,  ['KROTON', '23/07/07'],  2,  ['GUARANI', '23/07/07'],  1,  ['TRIUNFO PART', '23/07/07'],  1,  ['ABC BRASIL', '25/07/07'],  1,  ['SPRINGS', '27/07/07'],  1,  ['PROVIDENCIA', '27/07/07'],  1,  ['MULTIPLAN', '27/07/07'],  3,  ['GENERALSHOPP', '30/07/07'],  2,  ['ESTACIO PART', '30/07/07'],  3,  ['COSAN LTD ¹', '17/08/07'],  1,  ['SATIPEL', '21/09/07'],  1,  ['SUL AMERICA', '05/10/07'],  1,  ['BICBANCO', '15/10/07'],  1,  ['TRISUL', '15/10/07'],  2,  ['TENDA', '15/10/07'],  1,  ['SEB', '18/10/07'],  1,  ['MARISA', '22/10/07'],  1,  ['AGRENCO', '25/10/07'],  1,  ['BOVESPA HLD', '26/10/07'],  1,  ['BR BROKERS', '29/10/07'],  1,  ['AMIL', '29/10/07'],  1,  ['HELBOR', '29/10/07'],  2,  ['LAEP', '31/10/07'],  1,  ['PANAMERICANO', '19/11/07'],  1,  ['BMF', '30/11/07'],  1,  ['MPX ENERGIA', '14/12/07'],  1,  ['TEMPO PART', '19/12/07'],  1,  ['NUTRIPLANT', '13/02/08'],  1,  ['HYPERMARCAS', '18/04/08'],  3,  ['LE LIS BLANC', '29/04/08'],  3,  ['OGX PETROLEO', '13/06/08'],  1,  ['VISANET', '29/06/09'],  1,  ['TIVIT', '28/09/09'],  1,  ['SANTANDER BR ¹', '07/10/09'],  2,  ['CETIP', '28/10/09'],  1,  ['DIRECIONAL', '19/11/09'],  2,  ['FLEURY', '17/12/09'],  1,  ['ALIANSCE', '29/01/10'],  2,  ['MULTIPLUS', '05/02/10'],  1,  ['BR PROPERT', '08/03/10'],  3,  ['OSX BRASIL ', '22/03/10'],  1,  ['ECORODOVIAS', '01/04/10'],  2,  ['MILLS', '16/04/10'],  1,  ['JULIO SIMOES', '22/04/10'],  1,  ['RENOVA', '13/07/10'],  1,  ['HRT PETROLEO', '25/10/10'],  1,  ['BR INSURANCE', '01/11/10'],  1,  ['RAIA', '20/12/10'],  1,  ['AREZZO CO ', '02/02/11'],  1,  ['SIERRABRASIL ', '03/02/11'],  1,  ['AUTOMETAL ', '07/02/11'],  1,  ['QGEP PART ', '09/02/11'],  1,  ['IMC HOLDINGS', '09/03/11'],  1,  ['TIME FOR FUN', '13/04/11'],  1,  ['MAGAZ LUIZA', '02/05/11'],  4,  ['BR PHARMA', '27/06/11'],  3,  ['QUALICORP', '29/06/11'],  2,  ['TECHNOS', '01/07/11'],  1,  ['ABRIL EDUCA', '26/07/11'],  2,  ['LOCAMERICA', '23/04/12'],  3,  ['BTG PACTUAL', '26/04/12'],  1,  ['UNICASA', '27/04/12'],  1,  ['LINX', '08/02/13'],  2,  ['SENIOR SOL', '08/03/13'],  1,  ['BIOSEV', '19/04/13'],  1,  ['ALUPAR', '24/04/13'],  3,  ['BB SEGURIDADE', '29/04/13'],  1,  ['SMILES', '29/04/13'],  1,  ['CPFL RENOVAV', '19/07/13'],  1,  ['ANIMA', '28/10/13'],  3,  ['SER EDUCA', '29/10/13'],  1,  ['CVC BRASIL', '09/12/13'],  2,  ['OUROFINO S/A', '21/10/14'],  1,  ['PARCORRETORA', '05/06/15'],  1,  ['ALLIAR', '28/10/16'],  1,  ['MOVIDA', '08/02/17'],  2,  ['IHPARDINI', '14/02/17'],  1,  ['AZUL¹', '11/04/17'],  1,  ['CARREFOUR BR', '20/07/17'],  1,  ['BIOTOSCANA', '25/07/17'],  1,  ['IRBBRASIL RE', '31/07/17'],  3,  ['OMEGA GER', '31/07/17'],  4,  ['CAMIL', '28/09/17'],  1,  ['BK BRASIL', '18/12/17'],  3,  ['PETROBRAS BR', '15/12/17'],  3,  ['INTERMEDICA', '23/04/18'],  5,  ['HAPVIDA', '25/04/18'],  3,  ['INTER BANCO', '30/04/18'],  1,  ['CENTAURO', '17/04/19'],  2,  ['NEOENERGIA', '28/06/19'],  1,  ['VIVARA SA', '10/10/19'],  1,  ['BANCO BMG', '28/10/19'],  1,  ['CEA MODAS', '28/10/19'],  1,  ['MITRE REALTY', '05/02/20'],  1,  ['LOCAWEB', '06/02/20'],  2,  ['MOURA DUBEUX', '13/02/20'],  1,  ['PRINER', '17/02/20'],  1,  ['ESTAPAR', '15/05/20'],  1,  ['AURA 360', '06/07/20'],  2,  ['AMBIPAR', '13/07/20'],  1,  ['GRUPO SOMA', '31/07/20'],  2,  ['D1000VFARMA', '10/08/20'],  1,  ['QUERO-QUERO', '10/08/20'],  1,  ['LAVVI', '02/09/20'],  1,  ['PAGUE MENOS', '02/09/20'],  1,  ['PETZ', '11/09/20'],  2,  ['PLANOEPLANO', '17/09/20'],  1,  ['MELNICK', '28/09/20'],  1,  ['HIDROVIAS', '25/09/20'],  1,  ['CURY S/A', '21/09/20'],  1,  ['BOA VISTA', '30/09/20'],  1,  ['SEQUOIA LOG', '07/10/20'],  2,  ['GRUPO MATEUS', '13/10/20'],  1,  ['TRACK FIELD', '26/10/20'],  1,  ['MELIUZ', '04/11/20'],  2,  ['ENJOEI', '06/11/20'],  1,  ['AERIS', '10/11/20'],  1,  ['3R PETROLEUM', '10/11/20'],  3,  ['ALPHAVILLE', '07/12/20'],  1,  ['REDE D OR', '10/12/20'],  2,  ['NEOGRID', '18/12/20'],  1,  ['HBRREALTY', '21/01/21'],  1,  ['VAMOS', '29/01/21'],  2,  ['ESPACOLASER', '01/02/21'],  1,  ['INTELBRAS', '04/02/21'],  1,  ['MOSAICO', '05/02/21'],  1,  ['MOBLY', '05/02/21'],  1,  ['JALLESMACHADO', '08/02/21'],  1,  ['FOCUS ON', '08/02/21'],  1,  ['CRUZEIRO SUL', '11/02/21'],  2,  ['OCEANPACT', '12/02/21'],  1,  ['ORIZON', '17/02/21'],  1,  ['ELETROMIDIA', '17/02/21'],  1,  ['BEMOBI TECH', '10/02/21'],  1,  ['CSNMINERACAO', '18/02/21'],  1,  ['WESTWING', '10/02/21'],  1,  ['ALLIED', '12/04/21'],  1,  ['MATER DEI', '16/04/21'],  1,  ['BLAU', '19/04/21'],  1,  ['GPS', '26/04/21'],  1,  ['BOA SAFRA', '29/04/21'],  1,  ['CAIXA SEGURI²', '29/04/21'],  1,  ['MODALMAIS', '30/04/21'],  1,  ['INFRACOMM', '04/05/21'],  1,  ['PETRORECSA', '05/05/21'],  1,  ['GETNINJAS', '13/05/21'],  1,  ['G2D INVEST', '14/05/21'],  1,  ['DOTZ', '31/05/21'],  1,  ['BR PARTNERS', '21/06/21'],  1,  ['3TENTOS', '12/07/21'],  1,  ['WDC NETWORKS', '26/07/21'],  1,  ['SMART FIT', '14/07/21'],  1,  ['MULTILASER', '22/07/21'],  1,  ['DESKTOP', '21/07/21'],  1,  ['CBA', '15/07/21'],  1,  ['AGROGALAXY', '26/07/21'],  1,  ['UNIFIQUE', '27/07/21'],  1,  ['ARMAC', '28/07/21'],  1,  ['TC', '28/07/21'],  1,  ['BRISANET', '29/07/21'],  1,  ['CLEARSALE', '30/07/21'],  1,  ['VIVEO', '09/08/21'],  1,  ['RAIZEN', '04/08/21'],  1,  ['ONCOCLINICAS', '10/08/21'],  1,  ['KORA SAUDE', '13/08/21'],  1,  ['VITTIA', '02/09/21'],  1,  ['NU-NUBANK*', '09/12/21'],  1]

#pesquisa ano
def pesq_ano(x):
    k = []
    for i in range(int(len(quote)/2)):
        if quote[2*i][1][len(quote[2*i][1])-2:len(quote[2*i][1])] == str(x):
            # print(quote[2*i])
            k = k + [quote[2*i]]
    return k

from numpy import corrcoef

'------------------------------------------------------------------------------'

# acoes = open(r'ipo_emp.csv').read()
# l_aco = 0
# c_aco = 0

# for i in range(len(acoes)):
#     if acoes[i] == ';':
#         c_aco = c_aco + 1
#     if acoes[i:i+1] == '\n':
#         l_aco = l_aco + 1
# print(l_aco)
# print(c_aco)
# print(c_aco/l_aco)

# '-------------------------------------------------------------------------------'

# anual = open(r'ipo_ano.csv').read()
# l_ano = 0
# c_ano = 0

# for i in range(len(anual)):
#     if anual[i] == ';':
#         c_ano = c_ano + 1
#     if anual[i:i+1] == '\n':
#         l_ano = l_ano + 1
# print(l_ano)
# print(c_ano)
# print(c_ano/l_ano)

# '-------------------------------------------------------------------------------'

