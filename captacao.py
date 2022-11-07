import pandas as pd

arquivo = open('Alunos.txt','r')
linhas = arquivo.readlines()

#deletar dados desnecessários
del linhas[:4]

#criar indicadores
qtde_anuncio = 0
qtde_org = 0
qtde_yt_org = 0
qtde_igfb_org = 0
qtde_site_org = 0

#percorrer o arquivo
for linha in linhas:
    email, origem = linha.split(',')
    if 'org' in origem:
        qtde_org += 1
        if 'yt' in origem:
            qtde_yt_org += 1
        if 'ig' in origem:
            qtde_igfb_org += 1
        if 'site' in origem:
            qtde_site_org += 1
    else:
        qtde_anuncio += 1 



print('Quantidade Anuncio: {}'.format(qtde_anuncio))
print('Quantidade Orgânico: {}'.format(qtde_org))
print('Quantidade Instagram: {}'.format(qtde_igfb_org))
print('Quantidade Youtube: {}'.format(qtde_yt_org))
print('Quantidade Site: {}'.format(qtde_site_org))

#fechar arquivo
arquivo.close()