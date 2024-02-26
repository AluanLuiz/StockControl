import tkinter as tk
from tkinter import messagebox
from tkinter import font

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
#Caminho imagens
image_path = "env/image"
default_images = {
    "user_icon": os.path.join(image_path, "user_icon1.png"),
    "product_icon": os.path.join(image_path, "product_icon.png"),
    "warehouse_icon": os.path.join(image_path, "warehouse_icon1.png"),
    "menu_icon": os.path.join(image_path, "menu_icon1.png")
}

#------------------------------------------
#Modulos _py
import log #login
import main #Principal
import register_prod #Registrar produto
import register_user #Registrar usuário
import requisition_order #Ordem de Requisiçao
import write_off_prod #Dar Baixa estoque/produto

#from log import Id_user