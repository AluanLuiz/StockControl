import config as cg

#------------------------------------------

class Regist_Forn:
    def __init__(self, regis_forn):
        self.regi_F = regis_forn
        self.regi_F.title("Registrar Fornecedor")
        self.conect = cg.sql.connect(cg.db_cam)

        self.frameT = cg.tk.Frame(self.regi_F)
        self.frameT.grid(row=0, column=0, columnspan=4, sticky="ew")
              
        self.frame_btn = cg.tk.Frame(self.regi_F, bd=2)
        self.frame_btn.grid(row=1, column=0, columnspan=4, sticky="ew")
        
        self.regi_F.grid_rowconfigure(2, weight=1)
        self.regi_F.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.forms_forn()
        self.actions_btn()
    
    #--------------------------
    
    def forms_forn(self):
        font_1 = ("Arial", 16)
        font_2 = ("Arial", 14)
        
        #--------- ↓ Nome do Fornecedor
        self.name_f_lbl = cg.tk.Label(self.frameT, text="Nome do fornecedor:", font=font_1)
        self.name_f_lbl.grid(row=1, column=0, padx=10, pady=10)
        #--
        self.ent_name_f = cg.tk.Entry(self.frameT, font=font_2, width=20)
        self.ent_name_f.grid(row=1, column=2, columnspan=2, padx=10, pady=10)
        #---------
        #--------- ↓ CNPJ   
        self.cnpj_lbl = cg.tk.Label(self.frameT, font=font_1, text="CNPJ do fornecedor:")
        self.cnpj_lbl.grid(row=2, column=0, padx=10, pady=10)
        #--
        self.ent_cnpj = cg.tk.Entry(self.frameT, font=font_2, width=20)
        self.ent_cnpj.grid(row=2, column=2, columnspan=2, padx=10, pady=10)
        
        self.ent_cnpj.bind('<KeyRelease>', self.format_cnpj)
        #--------- 
        #--------- ↓ Contato
        self.contate_lbl = cg.tk.Label(self.frameT, font=font_1, text="Contato do fornecedor:")
        self.contate_lbl.grid(row=3, column=0, padx=10, pady=10)
        #--
        self.ent_contate = cg.tk.Entry(self.frameT, font=font_2, width=20)
        self.ent_contate.grid(row=3, column=2, columnspan=2, padx=10, pady=10)
        #---------
        
    #------------------------
    
    def actions_btn(self):
        font_Btn = ("Arial", 18)
        
        #--------- ↓ Botão Salvar
        self.save = cg.tk.Button(self.frame_btn, text="Salvar o \n registro", font=font_Btn,
                                       width=12, height=2, bd=4, highlightthickness=3, command=self.save_forms)   
        self.save.grid(row=0, column=4, columnspan=1, padx=10, pady=10)
        
        #--------- ↓ Botão Cancelar e Sair
        self.cancel = cg.tk.Button(self.frame_btn, text="Cancelar e \n Sair", font=font_Btn, 
                                       width=12, height=2, bd=4, highlightthickness=3, command=self.end_ents)   
        self.cancel.grid(row=0, column=0, columnspan=1, padx=10, pady=10)

    #-----------------------
    
    def end_ents(self):
        self.ent_name_f.delete(0, cg.tk.END)
        self.ent_cnpj.delete(0, cg.tk.END)
        self.ent_contate.delete(0, cg.tk.END)
        
        self.regi_F.destroy()
        
    #-----------------------
    def save_forms(self):
        ok = self.valid_forms()
        
        cursor =  self.conect.cursor()
        
        if ok == True:
            name = self.ent_name_f.get()
            pj = self.ent_cnpj.get()
            contat = self.ent_contate.get()
            
            try:
                cursor.execute("INSERT INTO Fornecedores (name, cnpj, contato) VALUES (?, ?, ?)",
                               (name, pj, contat))
                self.conect.commit()
                cg.msg.showinfo("Sucesso", "Registro do Fornecedor salvo com sucesso!") 
                cursor.close()
                self.end_ents()
                    
            except cg.sql.Error as e:
                cg.msg.showerror("Erro", "Não foi possível salvar o registro do fornecedor", e)
                return
            
            finally:
                cursor.close()
            
        else:
            cg.msg.showerror("Erro", "Não foi possivel validar o registro.")
            return
    
    #-----------------------
      
    def valid_forms(self):
        name = self.ent_name_f.get()
        pj = self.ent_cnpj.get()
        contat = self.ent_contate.get()
        
        cursor = self.conect.cursor()
        
        try:
            if name.strip() == "":
                cg.msg.showerror("Erro", "O Nome não pode ser vazio.")
                return False
            else:
                cursor.execute("SELECT name FROM Fornecedores WHERE name = ?", (name,))
                name_reference = cursor.fetchone()
                if name_reference == name:
                    cg.msg.showerror("Erro","Esse nome já está registrado no Banco de Dados. \n Recomendamos colocar outro nome.")
                    return False
            
            if pj.strip() == "":
                cg.msg.showerror("Erro", "O CNPJ não pode ser vazio.")
                return False
            else:
                cursor.execute("SELECT cnpj FROM Fornecedores WHERE cnpj = ?", (pj,))
                cnpj_reference = cursor.fetchone()
                if cnpj_reference == pj:
                    cg.msg.showerror("Erro", "Esse CNPJ já está registrado no Banco de Dados. \n Confirme se digitou corretamente.")
                    return False
            
            if contat.strip() == "":
                cg.msg.showerror("Erro", "O Contato não pode ser vazio.")
                return False
            else:
                cursor.execute("SELECT contato FROM Fornecedores WHERE contato = ?", (contat,))
                contato_reference = cursor.fetchone()
                if contato_reference == contat:
                    confirm_msg = "Este contato já está registrado \n Deseja mante-lo?"
                    if cg.msg.askyesno("Confirmação", confirm_msg):
                        cg.msg.showinfo("Informando", "O contato será salvo.")
                    else:
                        cg.msg.showwarning("Alerta", "Insira outro contato para o registro!")
                        return False
                    
        except:
            cg.msg.showerror("Erro", "Não foi possível salvar o registro do fornecedor")
            return
        
        finally:
            cursor.close()
        
        return True
    
    #-----------------------
    # Formatação do campo CNPJ
    
    def format_cnpj(self, event):
        pj_f = self.ent_cnpj.get()
        
        cnpj = cg.re.sub(r'\D', '', pj_f) # Remove todos os caracteres não numéricos do texto atual 
        
        if len(cnpj) == 0:
            self.ent_cnpj.delete(0, cg.tk.END)
            return

        if len(cnpj) <= 3:
            self.ent_cnpj.delete(0, cg.tk.END)
            self.ent_cnpj.insert(cg.tk.END, cnpj)
        elif len(cnpj) <= 6:
            self.ent_cnpj.delete(0, cg.tk.END)
            self.ent_cnpj.insert(cg.tk.END, cnpj[:3] + '.' + cnpj[3:])
        elif len(cnpj) <= 8:
            self.ent_cnpj.delete(0, cg.tk.END)
            self.ent_cnpj.insert(cg.tk.END, cnpj[:3] + '.' + cnpj[3:6] + '.' + cnpj[6:])
        elif len(cnpj) <= 14:
            self.ent_cnpj.delete(0, cg.tk.END)
            self.ent_cnpj.insert(cg.tk.END, cnpj[:3] + '.' + cnpj[3:6] + '.' + cnpj[6:9] + '/' + cnpj[9:])
        else:
            self.ent_cnpj.delete(0, cg.tk.END)
            self.ent_cnpj.insert(cg.tk.END, cnpj[:3] + '.' + cnpj[3:6] + '.' + cnpj[6:9] + '/' + cnpj[9:13] + '-' + cnpj[13:15])
    
        
#------------------------------------------        

def init_regis_fornec():
    regisF = cg.tk.Tk()
    app = Regist_Forn(regisF)
    regisF.geometry("460x300")
    regisF.mainloop()