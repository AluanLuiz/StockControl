import tkinter as tk
from tkinter import messagebox
from tkinter import font

#------------------------------------------
#Banco de Dados
import sqlite3 as sql
import os
import database

db_path = "env/db/control.db"
def init_config():
    dir_atual = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(dir_atual, "db", "control.db")

    database.create_DB(db_path)

#------------------------------------------
#Modulos _py
import log
import main
#from log import Id_user