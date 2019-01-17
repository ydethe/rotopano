import os
import logging

from logging.handlers import RotatingFileHandler


# DBG_LVL = logging.DEBUG
DBG_LVL = logging.INFO

# création de l'objet logger qui va nous servir à écrire dans les logs
logger = logging.getLogger()
# on met le niveau du logger à DEBUG, comme ça il écrit tout
logger.setLevel(DBG_LVL)
 
# création d'un formateur qui va ajouter le temps, le niveau
# de chaque message quand on écrira un message dans le log
formatter = logging.Formatter('%(asctime)s[%(levelname)s]%(message)s')
# création d'un handler qui va rediriger une écriture du log vers
# un fichier en mode 'append', avec 1 backup et une taille max de 1Mo
file_handler = RotatingFileHandler(os.path.join(os.path.dirname(__file__), "debug.log"), 'a', 1000000, 1)
# on lui met le niveau sur DEBUG, on lui dit qu'il doit utiliser le formateur
# créé précédement et on ajoute ce handler au logger
file_handler.setLevel(DBG_LVL)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
 
# création d'un second handler qui va rediriger chaque écriture de log
# sur la console
formatter = logging.Formatter('[%(levelname)s]%(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setLevel(DBG_LVL)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


