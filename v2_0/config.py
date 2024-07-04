#------------------------------------------
# Interface
import tkinter as tk
from tkinter import messagebox as msg
from tkinter import font

#------------------------------------------
#Outras bibliotecas
import re
import string
import datetime as dt

#------------------------------------------
#Banco de Dados
import sqlite3 as sql
import os
import database

db_cam = "env/db/control.db"
def init_config():
    dir_atual = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(dir_atual, "db", "control.db")

    database.create_DB(db_path)

#------------------------------------------
#Caminho imagens padrões
# def load_image_paths(db_path):
#     connection = sql.connect(db_path)
#     cursor = connection.cursor()
#     try:
#         cursor.execute("SELECT path FROM Images")
#         paths = cursor.fetchall()
#         return [path[0] for path in paths]
#     except sql.Error as e:
#         print(f"Erro ao carregar caminhos das imagens: {str(e)}")
#         return []
#     finally:
#         cursor.close()
#         connection.close()

image_path = "env/image"
default_images = {
    "user": os.path.join(image_path, "user_icon1.jpeg"),
    "add": os.path.join(image_path, "plus_icon.jpeg"),
    "minus": os.path.join(image_path, "minus_icon.jpeg"),
    "eye_look" : os.path.join(image_path, "eye_look_icon.jpeg"),
    "eye_view" : os.path.join(image_path, "eye_view_icon.jpeg")
  }

#------------------------------------------
#Modulos _py
import log #login
import main #Principal
import register_prod as rp #Registrar produto
import register_user as ru #Registrar usuário
import order #Ordem de Requisiçao/Devolção
import write_off_prod as wp #Dar Baixa estoque/produto
import forms_fornec as ff #Registro de novo fornecedor