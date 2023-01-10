import configparser
import os
import re

from .database import Database

parser = configparser.ConfigParser()
parser.read('./data/config.cfg')

TOKEN = os.environ[parser.get('MAIN', 'token')]
ADMINS = list(map(int, re.findall(r'\d{5,}', parser.get('MAIN', 'admins'))))

DB_FILE = parser.get("DATABASE", 'filename')
database = Database(DB_FILE)

