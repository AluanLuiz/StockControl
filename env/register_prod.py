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
        #---------
        #--------- ↓ Descrição
        self.description = cg.tk.Label(self.frameT, font=font_1, text="Descrição do Produto:")
        self.description.grid(row=2, column=0, padx=10, pady=10)
        #--
        self.entry_desc = cg.tk.Entry(self.frameT, font=font_2, width=20)
        self.entry_desc.grid(row=2, column=2, columnspan=2, padx=10, pady=10)
        #--------- 
        #--------- ↓ Quantidade
        self.quant_lbl = cg.tk.Label(self.frameT, font=font_1, text="Quantidade:")
        self.quant_lbl.grid(row=3, column=0, padx=10, pady=10)
        #--
        self.quant_sb = cg.tk.Spinbox(self.frameT, font=font_2, width=20, from_= 1, to= 9999)
        self.quant_sb.grid(row=3, column=2, columnspan=2, padx=10, pady=10)
        #---------
        #--------- ↓ Local_armazenado (nicho)
        self.local_lbl = cg.tk.Label(self.frameT, font=font_1, text="Local Armazenado (Z-XY):")
        self.local_lbl.grid(row=4, column=0, padx=10, pady=10)
        #--
        self.ent_local = cg.tk.Entry(self.frameT, font=font_2, width=20)
        self.ent_local.grid(row=4, column=2, columnspan=2, padx=10, pady=10)
        #---------
        #--------- ↓ Fornecedor
        self.fornec_name_lbl = cg.tk.Label(self.frameT, font=font_1, text="Fornecedor:")
        self.fornec_name_lbl.grid(row=5, column=0, padx=10, pady=10)
        #--
        self.ent_fornec_name = cg.tk.Entry(self.frameT, font=font_2, width=20)
        self.ent_fornec_name.grid(row=5, column=2, columnspan=2, padx=10, pady=10)
        
    #------------------------
    
    def actions_btn(self):
        font_Btn = ("Arial", 20)
        
        #--------- ↓ Botão Salvar
        self.save_forms = cg.tk.Button(self.frame_btn, text="Salvar o \n registro", font=font_Btn,
                                       width=12, height=2, bd=4, highlightthickness=3, command=self.validate_forms)   
        self.save_forms.grid(row=0, column=4, columnspan=1, padx=10, pady=10)
        
        #--------- ↓ Botão Cancelar e Sair
        self.cancel = cg.tk.Button(self.frame_btn, text="Cancelar e \n Sair", font=font_Btn, 
                                       width=12, height=2, bd=4, highlightthickness=3)   
        self.cancel.grid(row=0, column=0, columnspan=1, padx=10, pady=10)
    
    #------------------------
    
    def validate_forms(self):
       pass
   
#------------------------------------------

def init_regis_prod():
    regis = cg.tk.Tk()
    app = RegisterProd(regis)
    regis.geometry("570x420")
    regis.mainloop()