import config as cg

#------------------------------------------

class StockControl:
    def __init__(self, master):
        self.master = master
        self.master.title("Controle de Estoque")
        self.conect = cg.sql.connect(cg.db_path)
        self.start_config()
          
        self.frame_title = cg.tk.Frame(self.master)
        self.frame_title.grid(row=0, column=0, columnspan=4, sticky="ew")
        
        self.frame_buttons = cg.tk.Frame(self.master)
        self.frame_buttons.grid(row=1, column=0, columnspan=4, sticky="ew")
        
        self.frame_list = cg.tk.Frame(self.master)
        self.frame_list.grid(row=2, column=0, columnspan=4, sticky="nsew")
        
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        self.add_title()
        self.add_list()
        self.add_Btn()
     
    #--------------------------
    
    def add_title(self):
        font_1 = ("Arial", 20)
        title = cg.tk.Label(self.frame_title, text="Controle de Estoque", font=font_1)
        title.pack(pady=10)
        
    def add_list(self):
        font_3 = ("Arial", 14)
        listViewer = cg.tk.Listbox(self.frame_list, selectmode=cg.tk.MULTIPLE, height=20, width=90, font=font_3)
        listViewer.pack(expand=True, fill="both", padx=10, pady=10)
    
    def add_Btn(self):
        font_2 = ("Arial", 16)
        button_width = 10
        button_height = 1
        #---------
        #--------- ↓ Botão cadastro de produto
        bt_cadProdut = cg.tk.Button(self.frame_buttons, text="Cadastrar", font=font_2, width=button_width, height=button_height)
        bt_cadProdut.grid(row=0, column=0, padx=10, pady=10)
        #--------- 
        #--------- ↓ Botão dar baixa (retirada do estoque)
        bt_darBaixa = cg.tk.Button(self.frame_buttons, text="Dar Baixa", font=font_2, width=button_width, height=button_height)
        bt_darBaixa.grid(row=0, column=1, padx=10, pady=10)
        #---------
        #--------- ↓ Botão de login
        self.image_login = cg.tk.PhotoImage(file=cg.default_images["user_icon"])
        self.bt_login = cg.tk.Button(self.frame_buttons, image=self.image_login, command=self.login_valid, width=52, height=52, bd=0, highlightthickness=0)
        self.bt_login.grid(row=0, column=2, padx=10, pady=10)
        
    #--------------------------
    
    def start_config(self):
        cg.init_config()        
      
    def login_valid(self):
        cg.log.init_log()
    
#------------------------------------------
if __name__ == "__main__":
    app = cg.tk.Tk()
    app.geometry("800x600")
    main_app = StockControl(app)
    app.mainloop()