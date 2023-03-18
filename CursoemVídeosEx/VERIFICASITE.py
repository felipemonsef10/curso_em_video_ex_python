import urllib.request
import webbrowser as wb
from time import sleep

try:
    site = urllib.request.urlopen('https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enem')
except:
    print('\033[1;31mO site pudim está inacessível.\033[m')
else:
    print('\033[1;32mO site está acessível.\033[m')
    print('Abrindo o site na sua tela em ')
    for c in range(3, 0, -1):
        print(c, end=' ')
        sleep(1)
    wb.open('http://pudim.com.br')
