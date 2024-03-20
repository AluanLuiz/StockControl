import config as cg

#-----------------------------------------
class User_Cad:
    def __init__(self, new_user):
        self.new = new_user
        
        self.new.title("Cadastrar Usuário")
        
        self.conect = cg.sql.connect(cg.db_cam) 
        
        self.frame_ent = cg.tk.Frame(self.new)
        self.frame_ent.grid(row=0, column=0, columnspan=4, sticky="ew")
        
        self.frame_bt = cg.tk.Frame(self.new)
        self.frame_bt.grid(row=1, column=0, columnspan=4, sticky="ew")
        
        self.new.grid_rowconfigure(2, weight=1)
        self.new.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        self.entrys()
        self.buttons()

    #-----------------------------

    def entrys(self):
        font_1 = ("Arial", 16)
        font_2 = ("Arial", 14)
        
        #--------- ↓ Nome
        self.name = cg.tk.Label(self.frame_ent, text="Nome de usuário:", font=font_1)
        self.name.grid(row=0, column=0, padx=10, pady=10)
        #--
        self.ent_name = cg.tk.Entry(self.frame_ent, font=font_2, width=20)
        self.ent_name.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
        #---------
        
        #--------- ↓ Senha 1
        self.password_one = cg.tk.Label(self.frame_ent, font=font_1, text="Digite uma senha,\n mínimo de 6 caracteres:")
        self.password_one.grid(row=1, column=0, padx=10, pady=10)
        #--
        self.ent_pass_one = cg.tk.Entry(self.frame_ent, font=font_2, width=20, show="*")
        self.ent_pass_one.grid(row=1, column=2, columnspan=2, padx=10, pady=10)
        #--------- 
        
        #--------- ↓ Senha 2
        self.password_two = cg.tk.Label(self.frame_ent, font=font_1, text="Repita a senha:")
        self.password_two.grid(row=2, column=0, padx=10, pady=10)
        #--
        self.ent_pass_two = cg.tk.Entry(self.frame_ent, font=font_2, width=20, show="*")
        self.ent_pass_two.grid(row=2, column=2, columnspan=2, padx=10, pady=10)
        #--------- 
        
        #--------- ↓ Level User
        self.lvl_us = cg.tk.Label(self.frame_ent, font=font_1, text="Nível de Usuário:")
        self.lvl_us.grid(row=3, column=0, padx=10, pady=10)
        #--
        self.lvl_var = cg.tk.StringVar(self.frame_ent)
        self.lvl_var.set("Padrão")
        self.lvl_options = ["Padrão", "Gerente", "Admin"]
        self.lvl_ent = cg.tk.OptionMenu(self.frame_ent, self.lvl_var, *self.lvl_options)
        self.lvl_ent.config(font=(font_2[0], font_2[1] + 2), width=15) 
        self.lvl_ent.grid(row=3, column=2, columnspan=2, padx=10, pady=10)
        #--------- 
        
    #-----------------------------
    
    def buttons(self):
        font_Btn = ("Arial", 16)
        
        #--------- ↓ Botão Salvar
        self.save_forms = cg.tk.Button(self.frame_bt, text="Salvar o \n Usuário", font=font_Btn,
                                       width=12, height=2, bd=4, highlightthickness=3, command=self.save_user)   
        self.save_forms.grid(row=0, column=3, columnspan=1, padx=10, pady=10)
        
        #--------- ↓ Botão Cancelar e Sair
        self.cancel = cg.tk.Button(self.frame_bt, text="Cancelar e \n Sair", font=font_Btn, 
                                       width=12, height=2, bd=4, highlightthickness=3,  command=self.end_ents)   
        self.cancel.grid(row=0, column=0, columnspan=1, padx=10, pady=10)
        
    #-----------------------------
    
    def save_user(self):
        valided = self.valid_entry()
        
        if valided == True:
            cursor = self.conect.cursor()
            
            username = self.ent_name.get()
            pas_1 = self.ent_pass_one.get()
            lv = self.nivel() 
            
            try:
                cursor.execute("INSERT INTO Users (name_user, password, user_level) VALUES (?, ?, ?)",
                               (username, pas_1, lv))
                self.conect.commit()
                cg.msg.showinfo("Sucesso", "O usuário foi registrado com sucesso.")
                self.end_ents()
                
            except Exception as e:
                cg.msg.showerror("Erro", f"Não foi possível savar os dados no BD: {str(e)}")
                return False
            finally:
                cursor.close()     
        
    def valid_entry(self):
        username = self.ent_name.get()
        pas_1 = self.ent_pass_one.get()
        pas_2 = self.ent_pass_two.get()
        # lv = self.nivel()

        cursor = self.conect.cursor()
        
        try:
            #---
            if username.strip() == "":
                cg.msg.showerror("Erro", "O nome de usuário não pode ser vazio.")
                return False
            else:
                cursor.execute("SELECT name_user FROM Users WHERE name_user = ?", (username,))
                name_reference = cursor.fetchone()
                if name_reference is not None:
                    cg.msg.showerror("Erro", "Este nome de usuário já está em uso. \n Utilize outro nome.")
                    return False
            #---
            if pas_1.strip() == "":
                cg.msg.showerror("Erro", "Senha não pode ser vazio.")
                return False
            if len(pas_1) < 6:
                cg.msg.showerror("Erro", "As senha deve conter no mínimo 6 digitos.")
                return False
            #+
            if pas_2.strip() == "":
                cg.msg.showerror("Erro", "Repitir senha não pode ser vazio.")
                return False
            if len(pas_2) < 6:
                cg.msg.showerror("Erro", "As senha deve conter no mínimo 6 digitos.")
                return False
            #+
            if pas_1.strip() != pas_2.strip():
                cg.msg.showerror("Erro", "As senhas digitadas não coincidem.")  
                return False
            
            return True
        
        except Exception as e:
            cg.msg.showerror("Erro", f"Ocorreu um erro ao validar os campos: {str(e)}")
            return False
        finally:
            cursor.close()
    
    #-- ↓ Retornando o nível de Usuário de forma numérica.
    def nivel(self):
        level = self.lvl_var.get()
        
        if level == "Padrão":
            return 1
        elif level == "Gerente":
            return 2
        elif level == "Admin":
            return 3
        else:
            return False
           
    #-----------------------------
        
    def end_ents(self):
        self.ent_name.delete(0, cg.tk.END)
        self.ent_pass_one.delete(0, cg.tk.END)
        self.ent_pass_two.delete(0, cg.tk.END)
        self.new.destroy()    

#------------------------------------------

def init_CadUser():
    cad_u = cg.tk.Tk()
    app = User_Cad(cad_u)
    cad_u.geometry("530x380")
    cad_u.mainloop()