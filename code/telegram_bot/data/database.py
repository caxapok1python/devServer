import sqlite3
import time

from aiogram import types


class Database:
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)
        self.cursor = self.conn.cursor()
