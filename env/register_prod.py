import config as cg

#------------------------------------------

class RegisterProd:
    def __init__(self, regis_prod):
        self.regis = regis_prod
        self.regis.title("Registrar Produto")
        self.conect = cg.sql.connect(cg.db_cam)

        self.frameT = cg.tk.Frame(self.regis)
        self.frameT.grid(row=0, column=0, columnspan=4, sticky="ew")
              
        self.frame_btn = cg.tk.Frame(self.regis, bd=2)
        self.frame_btn.grid(row=1, column=0, columnspan=4, sticky="ew")
        
        self.regis.grid_rowconfigure(2, weight=1)
        self.regis.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.forms_prod()
        self.actions_btn()
        
    #------------------------
    def forms_prod(self):
        font_1 = ("Arial", 16)
        font_2 = ("Arial", 14)
        
        
        #--------- ↓ Código de Barras
        self.barCode = cg.tk.Label(self.frameT, text="Código de Barras do Produto:", font=font_1)
        self.barCode.grid(row=0, column=0, padx=10, pady=10)
        #--
        self.entry_BarCode = cg.tk.Entry(self.frameT, font=font_2, width=20)
        self.entry_BarCode.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
        #--------- 
        #--------- ↓ Nome
        self.name = cg.tk.Label(self.frameT, text="Nome simples do Produto:", font=font_1)
        self.name.grid(row=1, column=0, padx=10, pady=10)
        #--
        self.entry_name = cg.tk.Entry(self.frameT, font=font_2, width=20)
        self.entry_name.grid(row=1, column=2, columnspan=2, padx=10, pady=10)
        #--------- ↓ Descrição
        self.description = cg.tk.Label(self.frameT, font=font_1, text="Descrição do Produto:")
        self.description.grid(row=2, column=0, padx=10, pady=10)
        #--
        self.entry_desc = cg.tk.Entry(self.frameT, font=font_2, width=20)
        self.entry_desc.grid(row=2, column=2, columnspan=2, padx=10, pady=10)
        #--------- 
        #--------- ↓ 
    
    def actions_btn(self):
        font_Btn = ("Arial", 20)
        
        self.save_forms = cg.tk.Button(self.frame_btn, text="Salvar o \n registro", font=font_Btn, 
                                       width=12, height=2, bd=1, highlightthickness=1)   
        self.save_forms.grid(row=0, column=4, columnspan=1, padx=10, pady=10)
                     
        self.cancel = cg.tk.Button(self.frame_btn, text="Cancelar e \n Sair", font=font_Btn, 
                                       width=12, height=2, bd=2, highlightthickness=1)   
        self.cancel.grid(row=0, column=0, columnspan=1, padx=10, pady=10)
#------------------------------------------

def init_regis_prod():
    regis = cg.tk.Tk()
    app = RegisterProd(regis)
    regis.geometry("800x500")
    regis.mainloop()