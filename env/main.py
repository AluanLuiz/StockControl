import config as cg

#------------------------------------------

class StockControl:
    def __init__(self, master):
        self.master = master
        self.master.title("Controle de Estoque")
        self.conect = cg.sql.connect(cg.db_path)
        self.start_config()
        
        self.font_1 = cg.font.Font(family="Arial", size=18)
        self.font_2 = cg.font.Font(family="Arial", size=16)
        self.font_3 = cg.font.Font(family="Arial", size=12)
        
        self.title = cg.tk.Label(self.master, text="Controle de Estoque", font=self.font_1)
        self.title.pack(anchor="w", padx=15, pady=5)
        # Adicione aqui a inicialização de outros componentes da tela principal
        self.bt_cadProdut = cg.tk.Button(self.master, text="Cadastrar Produto", font=self.font_2)
        self.bt_cadProdut.pack(anchor="w", padx=15, pady=5)
        
        self.bt_cadProdut = cg.tk.Button(self.master, text="Login", font=self.font_2, command=self.login_valid)
        self.bt_cadProdut.pack(anchor="w", padx=15, pady=5)
        
        self.listViewer = cg.tk.Listbox(self.master, selectmode=cg.tk.MULTIPLE, height=20, width=88, font=self.font_3)
        self.listViewer.pack(anchor="e", padx=15, pady=5)

        # self.bt_reload = cg.tk.Button(master, text="Atualizar  ", font=self.font_2, command=self.load_listview)
        # self.bt_reload.grid(row=2, column=2, pady=10)
        self.bt_darBaixa = cg.tk.Button(self.master, text="Dar Baixa", font=self.font_2)
        self.bt_darBaixa.pack(anchor="w", padx=15, pady=5)
        
    #--------------------------
    
    def start_config(self):
        cg.init_config()        
    
    #--------------------------
      
    def login_valid(self):
        cg.log.init_log()
    
#------------------------------------------
if __name__ == "__main__":
    app = cg.tk.Tk()
    app.geometry("800x600")
    main_app = StockControl(app)
    app.mainloop()