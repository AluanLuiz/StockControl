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
        self.ent_BarCode = cg.tk.Entry(self.frameT, font=font_2, width=20)
        self.ent_BarCode.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
        #--------- 
        #--------- ↓ Nome
        self.name = cg.tk.Label(self.frameT, text="Nome simples do Produto:", font=font_1)
        self.name.grid(row=1, column=0, padx=10, pady=10)
        #--
        self.ent_name = cg.tk.Entry(self.frameT, font=font_2, width=20)
        self.ent_name.grid(row=1, column=2, columnspan=2, padx=10, pady=10)
        #---------
        #--------- ↓ Descrição
        self.description = cg.tk.Label(self.frameT, font=font_1, text="Descrição do Produto:")
        self.description.grid(row=2, column=0, padx=10, pady=10)
        #--
        self.ent_desc = cg.tk.Entry(self.frameT, font=font_2, width=20)
        self.ent_desc.grid(row=2, column=2, columnspan=2, padx=10, pady=10)
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
        self.ent_fornec = cg.tk.Entry(self.frameT, font=font_2, width=20)
        self.ent_fornec.grid(row=5, column=2, columnspan=2, padx=10, pady=10)
        
    #------------------------
    
    def actions_btn(self):
        font_Btn = ("Arial", 20)
        
        #--------- ↓ Botão Salvar
        self.save_forms = cg.tk.Button(self.frame_btn, text="Salvar o \n registro", font=font_Btn,
                                       width=12, height=2, bd=4, highlightthickness=3, command=self.save_regis)   
        self.save_forms.grid(row=0, column=4, columnspan=1, padx=10, pady=10)
        
        #--------- ↓ Botão Cancelar e Sair
        self.cancel = cg.tk.Button(self.frame_btn, text="Cancelar e \n Sair", font=font_Btn, 
                                       width=12, height=2, bd=4, highlightthickness=3, command=self.end_ents)   
        self.cancel.grid(row=0, column=0, columnspan=1, padx=10, pady=10)
    
    #------------------------
    
    def validate_forms(self):  
        #-- Metodo de validação do forms
        code_bar = self.ent_BarCode.get()
        name_simple = self.ent_name.get()
        descr = self.ent_desc.get()
        quant = self.quant_sb.get()
        loc = self.ent_local.get()
        fornec = self.ent_fornec.get()
        
        cursor = self.conect.cursor()

        try:
            # -- Verificação do Código do Porduto/Material
            if code_bar.strip() == "":
                cg.messagebox.showerror("Erro", "Códigos de Barras não pode ser vazio.")
                return "invalido"
            
            else:
                cursor.execute("SELECT bar_code FROM Products WHERE bar_code = ?", (code_bar,))
                codebar_reference = cursor.fetchone()
                if codebar_reference and codebar_reference[0] == code_bar:
                    cg.messagebox.showerror("Erro", "O Código do Produto já existe.")
                    return "invalido"
            
            # -- Verificação do Nome
            if name_simple.strip() == "":
                cg.messagebox.showerror("Erro", "Nome do produto não pode ser vazio.")
                return "invalido"
            
            else:
                cursor.execute("SELECT name_simple FROM Products WHERE name_simple = ?", (name_simple,))
                name_reference = cursor.fetchone()
                if name_reference and name_reference[0] == name_simple:
                    cg.messagebox.showerror("Erro", "Um produto com esse nome, já existe.")
                    return "invalido"
            
            # -- Verificação da Descricao
            if descr.strip() == "":
                cg.messagebox.showerror("Erro", "Descrição do produto não pode ser vazio.")
                return "invalido"
            
            # -- Verificação da Quantide
            quanti = int(quant)
            if quanti <= 0:
                cg.messagebox.showerror("Erro", "Quantidade do Produto deve ser no mínimo 1")
                return "invalido"
            
            # -- Verificando se o nicho está ocupado
            if loc.strip() == "":
                cg.messagebox.showerror("Erro", "Local de armazenamento não pode ser vazio.")
                return "invalido"
            
            else:
                cursor.execute("SELECT local_arm FROM Products WHERE local_arm  = ?", (loc,))
                loc_reference = cursor.fetchone()
                if loc_reference and loc_reference[0] == loc:
                    cg.messagebox.showerror("Erro", "O local já está ocupado.")
                    return "invalido"
            
            # -- Verificação do Fornecedor
            if fornec.strip() == "":
                cg.messagebox.showerror("Erro", "O Fornecedor não pode ser vazio.")
                return "invalido"                          
               
        except cg.sql.Error as e:
            #print("Erro ao salvar o registro do produto:", e)
            cg.messagebox.showerror("Erro", "Não foi possível salvar o registro do produto", e)
            return
        finally:
            cursor.close()
        
        return "Valido"
    
    #------------------------
    
    def save_regis(self):
        valid =  self.validate_forms()
        
        cursor = self.conect.cursor()
        if valid == "Valido":
            code_bar = self.ent_BarCode.get()
            name_simple = self.ent_name.get()
            descr = self.ent_desc.get()
            quant = self.quant_sb.get()
            loc = self.ent_local.get()
            fornec = self.ent_fornec.get()

            if fornec.isalpha():
                cursor.execute("SELECT id_fornecedor, name, cnpj FROM Fornecedores WHERE name = ?", (fornec,))
                fornec_reference = cursor.fetchone()
                if fornec_reference is None:
                    confirm_msg = f"O fornecedor '{fornec}' não foi encontrado. Deseja registrá-lo?"
                    if cg.messagebox.askyesno("Confirmação", confirm_msg):
                        self.forms_fornec()
                        return
                    else:
                        cg.messagebox.showerror("Aviso", "Por favor, coloque o fornecedor correto.")
                        print("Fornecedor não confirmado.")
                        return "invalido"
                    
                else:
                    confirm_msg = f"O fornecedor '{fornec}' foi encontrado. Deseja mantê-lo no registro?"
                    if cg.messagebox.askyesno("Confirmação", confirm_msg):
                        id_f = fornec_reference[0]
                        print("Fornecedor confirmado.")
                    else:
                        cg.messagebox.showerror("Aviso", "Por favor, coloque o fornecedor correto.")
                        print("Fornecedor não confirmado.")
                        return "invalido"
                    
            else:
                cursor.execute("SELECT id_fornecedor, name, cnpj FROM Fornecedores WHERE cnpj = ?", (fornec,))
                fornec_reference = cursor.fetchone()
                if fornec_reference is None:
                    confirm_msg = f"O fornecedor com o CNPJ '{fornec}' não foi encontrado. Deseja registrá-lo?"
                    if cg.messagebox.askyesno("Confirmação", confirm_msg):
                        self.forms_fornec()
                        return
                    else:
                        cg.messagebox.showerror("Aviso", "Por favor, coloque o fornecedor correto.")
                        print("Fornecedor não confirmado.")
                        return "invalido"
                else:
                    confirm_msg = f"O fornecedor '{fornec}' foi encontrado. Deseja mantê-lo no registro?"
                    if cg.messagebox.askyesno("Confirmação", confirm_msg):
                        id_f = fornec_reference[0]
                        print("Fornecedor confirmado.")
                    else:
                        cg.messagebox.showerror("Aviso", "Por favor, coloque o fornecedor correto.")
                        print("Fornecedor não confirmado.")
                        return "invalido"
        
            
            try:
                cursor.execute("INSERT INTO Products (bar_code, name_simple, description, quant_dispon, local_arm, id_fornecedor) VALUES (?, ?, ?, ?, ?, ?)",
                               (code_bar, name_simple, descr, quant, loc, id_f))
                self.conect.commit()
                cg.messagebox.showinfo("Sucesso", "Registro do produto salvo com sucesso!") 
                self.end_ents()
                cursor.close()
                
            except cg.sql.Error as e:
                #print("Erro ao salvar o registro do produto:", e)
                cg.messagebox.showerror("Erro", "Não foi possível salvar o registro do produto", e)
                return
            finally:
                cursor.close()
    
    #------------------------
    
    def end_ents(self):
        self.ent_BarCode.delete(0, cg.tk.END)
        self.ent_name.delete(0, cg.tk.END)
        self.ent_desc.delete(0, cg.tk.END)
        self.ent_local.delete(0, cg.tk.END)
        self.ent_fornec.delete(0, cg.tk.END)
        self.quant_sb.delete(0, cg.tk.END)
        
        self.regis.destroy()

#------------------------------------------

def init_regis_prod():
    regis = cg.tk.Tk()
    app = RegisterProd(regis)
    regis.geometry("570x420")
    regis.mainloop()