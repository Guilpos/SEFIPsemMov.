from tkinter import *
import pyautogui as auto
import pyperclip as pyper
from time import sleep
from selenium import webdriver
from random import randint

janela1 = Tk()
janela1.geometry('500x300')

sleep(5)
print(auto.position())


#numero da pasta
npastatxt = Label(janela1, text='Número')
npastatxt.place(x=0, y=0)

npasta = Entry(janela1, width=5)
npasta.place(x=80, y=0)

#nome da pasta
pastatxt = Label(janela1, text='Pasta')
pastatxt.place(x=120, y=0)

pasta = Entry(janela1, width=30)
pasta.place(x=160, y=0)

#CNPJ
cnpjtxt = Label(janela1, text='CNPJ')
cnpjtxt.place(x=0, y=25)

cnpj = Entry(janela1, width=20)
cnpj.place(x=80, y=25)

#Razao Social
razaotxt = Label(janela1, text='Razão Social')
razaotxt.place(x=0, y=50)


razao = Entry(janela1, width=38)
razao.place(x=80, y=50)

#Logradouro
logtxt = Label(janela1, text='Logradouro')
logtxt.place(x=0, y=80)

log = Entry(janela1, width=45)
log.place(x=80, y=80)

#Bairro
bairrotxt = Label(janela1, text='Bairro')
bairrotxt.place(x=0, y=105)

bairro = Entry(janela1, width=25)
bairro.place(x=80, y=105)

#cep
ceptxt = Label(janela1, text='CEP')
ceptxt.place(x=235, y=105)

cep = Entry(janela1, width=15)
cep.place(x=260, y=105)

#cidade
cidadetxt = Label(janela1, text='Cidade')
cidadetxt.place(x=0, y=130)

cidade = Entry(janela1, width=25)
cidade.place(x=80, y=130)

#UF
uftxt = Label(janela1, text='UF')
uftxt.place(x=235, y=130)

uf = Entry(janela1, width=15)
uf.place(x=260, y=130)

#DDD
dddtxt = Label(janela1, text='DDD')
dddtxt.place(x=0, y=155)

ddd = Entry(janela1, width=3)
ddd.place(x=80, y=155)

#Telefone
teltxt = Label(janela1, text='Telefone')
teltxt.place(x=110, y=155)

tel = Entry(janela1, width=20)
tel.place(x=160, y=155)

#CNAE
cnaetxt = Label(janela1, text='CNAE')
cnaetxt.place(x=0, y=180)

cnae= Entry(janela1, width=7)
cnae.place(x=80, y=180)

#Botão de coleta de dados
def myClick():
    pastanum = npasta.get()
    pastaname = pasta.get()
    cnpjdata = cnpj.get()
    global razaodata
    razaodata = razao.get()
    logdata = log.get()
    bairrodata = bairro.get()
    cepdata = cep.get()
    global cidadedata
    cidadedata = cidade.get()
    ufdata = uf.get()
    ddddata = ddd.get()
    teldata = tel.get()
    cnaedata = cnae.get()

    auto.PAUSE = 3
    pyper.copy(f'{pastanum} - {pastaname}')

    sleep(1)
    #clica no explorador de pastas
    auto.click(x=422, y=747)
    #clica no Disco local
    auto.click(x=78, y=530)
    #clica na pasta usuários
    auto.click(x=206, y=348, clicks=2)
    #clica em público
    auto.click(x=237, y=242, clicks=2)
    #clica em documentos públicos
    auto.click(x=201, y=244, clicks=2)
    #clica em empresas com competencia para o mês de setembro
    auto.click(x=166, y=351, clicks=2)
    #cria nova pasta
    auto.click(x=503, y=79)

    auto.hotkey('ctrl', 'v')

    auto.press('enter')
    #abrir a barra de pesquisa
    auto.press('win')
    #clica no sefip
    auto.click(x=474, y=290)
    #maximiza o sefip
    auto.click(x=973, y=132)
    #clica no lsc
    auto.click(x=110, y=107)
    #clica em nova empresa
    auto.click(x=1213, y=689)
    #celeciona cnpj-1
    auto.press('1')
    #barra do cnpj
    auto.press('tab')
    #escreve o cnpj
    auto.write(cnpjdata)
    #linha da razao social
    auto.press('tab')
    #escreve a razao social
    auto.write(razaodata)
    #linha do logradouro
    auto.press('tab')
    #escreve o logradouro
    auto.write(logdata)
    #linha do bairro
    auto.press('tab')
    #escreve o bairro
    auto.write(bairrodata)
    #vai para a linha do cep
    if len(bairrodata) < 20:
        auto.press('tab')
    #escreve o cep
    auto.write(cepdata)
    #escreve cidade
    auto.write(cidadedata)
    #linha da uf
    auto.press('tab')
    #escreve a uf
    auto.write(ufdata)
    #linha do ddd
    auto.click(x=316, y=284, clicks=3)
    #escreve ddd
    auto.write(ddddata)
    #linha do telefone
    auto.press('tab')
    #telefone
    auto.write(teldata)
    #escreve cnae
    auto.write(cnaedata)
    #clica no cnae
    auto.click(x=316, y=350)
    #linha do cnae preponderante
    auto.press('tab')
    #escreve cnae preponderante
    auto.write(cnaedata)
    #clica no cnae preponderante
    auto.click(x=542, y=349)
    #linha do fpas
    auto.press('tab')
    #escreve fpas
    auto.write('515')
    #clica em salvar
    auto.click(x=1224, y=690, clicks=3)
    #confirma dados
    auto.click(x=641, y=418)

    # atualiza
    auto.press('f5')
    auto.PAUSE = 2
    sleep(1)
    # clica em movimento
    auto.click(x=181, y=84)
    # clica em novo
    auto.click(x=1027, y=688)
    # escreve a competencia
    auto.write('082021')
    # vai para codigo de recolhimento
    auto.press('tab')
    # escreve o codigo de recolhimento
    auto.write('1')
    #clica no codigo de recolhimento
    auto.click(x=559, y=172)
    #clica em sem movimento
    auto.click(x=240, y=203)
    # clica em salvar
    auto.click(x=1227, y=689)
    # clica em confirma
    auto.click(x=641, y=418)
    auto.click(x=680, y=423)
    # clicla no binoculos
    auto.click(x=198, y=60)
    # escreve a empresa que quer achar
    auto.write(razaodata)
    # clica em localizar
    auto.click(x=946, y=239)
    # clica na empresa que foi incluída
    auto.click(x=534, y=380, clicks=2)
    # clica em fechar
    auto.click(x=957, y=272)
    #clica em marcar
    auto.click(x=91, y=58)
    #clica em dados do movimento
    auto.click(x=1154, y=692)
    #aperta 2
    auto.press('2')
    #clica na segunda opção
    auto.click(x=664, y=232)
    #vai para a linha de baixo
    auto.press('tab')
    #escreve 1
    auto.write('1')
    #clica em salvar
    auto.click(x=1229, y=689)
    #clica em sim
    auto.click(x=641, y=421)
    #clica na lista
    auto.click(x=13, y=391)
    #aperta para subir
    auto.scroll(1000000)
    #clica no primeiro
    auto.click(x=119, y=106)
    auto.PAUSE = 3
    sleep(1)
    #clica em executar
    auto.click(x=1115, y=688)
    sleep(10)
    #clica em ok
    auto.click(x=834, y=439)
    #clica em ok novamente
    auto.click(x=682, y=426)
    #clica nos diretórios
    auto.click(x=851, y=257)
    #minimiza a pasta
    auto.click(x=588, y=307)
    #clica em usuarios
    auto.click(x=586, y=448)
    #clica em publico
    auto.click(x=605, y=466)
    #clica em documentos publicos
    auto.click(x=626, y=413)
    #clica em empresas com competencia do mes de setembro
    auto.click(x=646, y=464)
    #clica na pasta de destino
    auto.click(x=703, y=322)
    #clica em ok
    auto.click(x=707, y=528)
    #clica em salvar
    auto.click(x=820, y=404)
    #clica em ok
    auto.click(x=692, y=392)
    #novamente
    auto.click(x=684, y=397)
    #e de novo
    auto.click(x=681, y=431)
    #clica em relação de trabalhadores
    auto.click(x=427, y=149)
    #clica em gerar pdf
    auto.click(x=813, y=536)
    #clica em documents
    auto.click(x=596, y=346)
    #clica para baixar
    auto.click(x=812, y=436)
    #clica em empresas compt. setembro
    auto.click(x=651, y=425)
    #clica na pasta de destino
    auto.click(x=623, y=377)
    #clica em ok
    auto.click(x=682, y=512)
    # clica em processo finalizado com sucesso
    auto.click(x=682, y=420)
    #clica em fechar
    auto.click(x=895, y=538)
    #clica em comprovante de pagamento da previdencia
    auto.click(x=452, y=224)
    #clica em gerar pdf
    auto.click(x=868, y=505)
    #clica em ok
    auto.click(x=683, y=507)
    #clica em processo finalizado com sucesso
    auto.click(x=682, y=420)
    #clica em fechar
    auto.click(x=941, y=508)



#botoes da janela1
Botao = Button(janela1, text='Coleta', command=myClick)
Botao.place(x=200, y=270)

janela1.mainloop()
