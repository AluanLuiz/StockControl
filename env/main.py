import config as cg

#------------------------------------------

class StockControl:
    def __init__(self, master):
        self.master = master
        self.master.title("Controle de Estoque")
        self.conect = cg.sql.connect(cg.db_cam)
        self.start_config()
         
        self.frame_title = cg.tk.Frame(self.master, bg="#D9D9D9")
        self.frame_title.grid(row=0, column=0, columnspan=5, sticky="ew")
        
        self.frame_buttons = cg.tk.Frame(self.master, bd=2, bg="#D9D9D9")
        self.frame_buttons.grid(row=1, column=0, columnspan=5, sticky="ew")
        
        self.frame_list = cg.tk.Frame(self.master, bg="#D9D9D9")
        self.frame_list.grid(row=2, column=0, columnspan=5, sticky="nsew")
        
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        
        self.add_title()
        self.add_list()
        self.add_Btn()
        self.load_listview()
     
    #--------------------------
    
    def add_title(self):
        font_1 = ("Arial", 20)
        self.title = cg.tk.Label(self.frame_title, bg="#D9D9D9", text="Controle de Estoque", font=font_1)
        self.title.pack(pady=10)
        
        self.log_user_lbl = cg.tk.Label(self.frame_title, bg="#D9D9D9", text="None", font=("Arial", 12))
        self.log_user_lbl.pack(pady=10)
        
    def add_list(self):
        font_3 = ("Arial", 14)
        self.listViewer = cg.tk.Listbox(self.frame_list, selectmode=cg.tk.MULTIPLE, height=20, width=90, font=font_3)
        self.listViewer.pack(expand=True, fill="both", padx=10, pady=10)
    
    def add_Btn(self):
        font_2 = ("Arial", 16)
        font_4 = ("Arial", 14)
        button_width = 10
        button_height = 2
        #---------
        #--------- ↓ Botão cadastro de produto
        self.bt_cadProdut = cg.tk.Button(self.frame_buttons, bg="#D9D9D9", text="Cadastrar", font=font_2, 
                                         width=button_width, height=button_height, bd=0, highlightthickness=0, command=self.cmd_cadProd)
        self.bt_cadProdut.grid(row=0, column=2, padx=10, pady=10)
        #--------- 
        #--------- ↓ Botão dar baixa (retirada do estoque)  
        self.bt_darBaixa = cg.tk.Button(self.frame_buttons, bg="#D9D9D9", text="Dar Baixa", font=font_2, 
                                        width=button_width, height=button_height, bd=0, highlightthickness=0)
        self.bt_darBaixa.grid(row=0, column=1, padx=10, pady=10)
        #---------
        #--------- ↓ Botão dar baixa (retirada do estoque)
        self.bt_Requisition_order = cg.tk.Button(self.frame_buttons, bg="#D9D9D9", text=("Ordem de \n Requisição"), 
                                                 font=font_4, width=button_width, height=button_height, bd=0, highlightthickness=0)
        self.bt_Requisition_order.grid(row=0, column=0, padx=10, pady=10)
        #--------- 
        #--------- ↓ Botão dar baixa (retirada do estoque)
        self.bt_cad_user= cg.tk.Button(self.frame_buttons, bg="#D9D9D9", text="Cadastrar \n usuário", font=font_4, 
                                       width=button_width, height=button_height, bd=0, highlightthickness=0)
        self.bt_cad_user.grid(row=0, column=3, padx=10, pady=10)
        #---------
        #--------- ↓ Botão de login
        # self.image_login = cg.tk.PhotoImage(file=cg.default_images["user_icon"])
        # self.bt_login = cg.tk.Button(self.frame_buttons, bg="#D9D9D9", image=self.image_login, command=self.login_valid, width=52, height=52, bd=0, highlightthickness=0)
        # self.bt_login.grid(row=0, column=4, padx=10, pady=10)
        
    #--------------------------
    
    def load_listview(self):
        self.listViewer.delete(0, cg.tk.END)
        
        cursor = self.conect.cursor()
        cursor.execute('''SELECT bar_code, name_simple, description,local_arm, quantidade_disponivel
                       FROM Products
                       ''')
        load_prod = cursor.fetchall()
        
        for regist in load_prod:
            info_prod = self.format_info(regist)
            self.listViewer.insert(cg.tk.END, info_prod)
            
    def format_info(self, item):
        return f"C.B. {item[0]}, Nome: {item[1]}, descrição: {item[2]} | Local:{item[3]} - Quantidade: {item[4]}"\
    
    #--------------------------
    def start_config(self):
        cg.init_config()        
      
    # def login_valid(self):
    #     self.ident, self.name, self.lvl = cg.log.init_log()
    #     if self.ident:
    #         self.log_user_lbl.config(text=f"{self.name} - {self.ident} ({self.lvl})")
    
    #--------------------------
    
    def cmd_cadProd(self):
        cg.rp.init_regis_prod()
          
    
#------------------------------------------

if __name__ == "__main__":
    iden, name, lvl = cg.log.init_log()
           
    app = cg.tk.Tk()
    app.geometry("800x600")
    main_app = StockControl(app)
    
    if iden:
        main_app.log_user_lbl.config(text=f"{name} - {iden} ({lvl})")
        
    app.mainloop()