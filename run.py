from bot import Bot
import argparse

parser = argparse.ArgumentParser(epilog='''
Downloader Movies Torrent Bot
- run the command 'python3 run.py -m MOVIE_NAME
''')
parser.add_argument('-m', help='Movie/Filme para Download')
args = parser.parse_args()

if args.m:
    Bot.init(args)
else:
    print('''Downloader Movies Torrent Bot

How to use:
-(EN-US) Run the command 'python3 run.py -m MOVIE_NAME
-(PT-BR) Rode o comando 'python3 run.py -m NOME_DO_FILME

Desenvolvido por Jocimar Lopes
    ''')
