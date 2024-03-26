"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar.
-Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
from datetime import date
import emoji

print(emoji.emojize('\033[0;33m| :Brazil: |\033[m\033[0;32mSeja bem vindo(a) ao alistamento militar obrigatório !\033[0;33m| :Brazil: | \033[m'))
print('''\033[0;34mQual o seu gênero:
[ 1 ] Masculino
[ 2 ] Feminino \033[m''')
gen = int(input('\033[1;33mSua opção: \033[m'))
if gen == 2:
    print('\033[0;36mDesculpe, o alistamento militar é obrigatório apenas para homens no brasil.\033[m')
    print(emoji.emojize('\033[1;33m| :Brazil: | \033[m\033[0;32mObrigado por usar nosso sistema. \033[m\033[1;33m| :Brazil: | \033[m'))
    exit()
else:
    print('\033[1;32mSua inscrição é obrigatória!!!\033[m')
    nascimento = int(input('\033[1;33mQual seu ano de nascimento? \033[m'))
    atual = date.today().year
    idade = atual - nascimento

print('\033[0;36mVocê nascido no ano de {} tem {} anos e\033[m'.format(nascimento, idade))
if idade == 18:
    print('\033[0;36mprecisa se alistar imediatamente!\033[m')
elif idade > 18:
    saldo = idade - 18
    print('\033[0;36mjá deveria ter se alistado a {} anos.\033[m'.format(saldo))
elif idade < 18:
    saldo = 18 - idade
    mes = saldo * 12
    print('\033[0;36mAinda faltam {} meses para o seu alistamento.\033[m'.format(mes))

print(emoji.emojize('\033[0;33m| :Brazil: |\033[m\033[0;32mPrepare-se para o serviço militar com determinação e foco\033[m\033[0;33m| :Brazil: |\033[m'))
