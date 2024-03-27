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
image_path = "env/image"
default_images = {
    "user_icon": os.path.join(image_path, "user_icon1.png"),
    "add_icon": os.path.join(image_path, "plus_icon.png"),
    "minus_icon": os.path.join(image_path, "minus_icon.png"),
    "eye_look_icon" : os.path.join(image_path, "eye_look_icon.png"),
    "eye_view_icon" : os.path.join(image_path, "eye_view_icon.png")
}
# Icones nao usados, ainda...
# "product_icon": os.path.join(image_path, "product_icon.png"),
# "menu_icon": os.path.join(image_path, "menu_icon1.png"),
# "warehouse_icon": os.path.join(image_path, "warehouse_icon1.png"),
#------------------------------------------
#Modulos _py
import log #login
import main #Principal
import register_prod as rp #Registrar produto
import register_user as ru #Registrar usuário
import order #Ordem de Requisiçao/Devolção
import write_off_prod as wp #Dar Baixa estoque/produto
import forms_fornec as ff #Registro de novo fornecedor
