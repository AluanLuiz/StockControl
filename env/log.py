import config as cg
#------------------------------------------

class Login:
    def __init__(self, logon):
        self.master = logon

        self.master.title("Login")

        self.conect = cg.sql.connect(cg.db_cam)

        self.font_Title = cg.font.Font(family="Arial", size=16)
        self.font_Regular = cg.font.Font(family="Arial", size=14)
        self.font_text = cg.font.Font(family="Arial", size=10)

        #--------------------
        self.title = cg.tk.Label(logon, text="Login", font=self.font_Title)
        self.title.pack(anchor="w", padx=15, pady=5)
        #self.title.grid(row=0, column=0, padx=15, pady=6)
        #--------------------
        self.label_username = cg.tk.Label(logon, text="Nome de usuário:", font=self.font_Title)
        self.label_username.pack(anchor="w", padx=15, pady=5)
        #self.label_username.grid(row=1, column=0, padx=15, pady=6)

        self.entry_username = cg.tk.Entry(logon, font=self.font_text, width=30)
        self.entry_username.pack(anchor="w", padx=15, pady=5)
        #self.entry_username.grid(row=2, column=0, padx=15, pady=6)
        #--------------------
        self.label_password = cg.tk.Label(logon, text="Senha:", font=self.font_Title)
        self.label_password.pack(anchor="w", padx=15, pady=5)
        #self.label_password.grid(row=3, column=0, padx=15, pady=6)

        self.entry_password = cg.tk.Entry(logon, show="*", font=self.font_text, width=30)
        self.entry_password.pack(anchor="w", padx=15, pady=5)
        #self.entry_password.grid(row=4, column=0, padx=15, pady=6)
        #--------------------
        self.button_login = cg.tk.Button(logon, text="Entrar", font=self.font_Regular, command=self.entrar)
        self.button_login.pack(anchor="w", padx=15, pady=5)
        #self.button_login.grid(row=5, column=0, columnspan=2, padx=15, pady=6)

    #------------------------------------------

    def entrar(self):
        try:
            cursor = self.conect.cursor()
                        
            userName = self.entry_username.get()
            Password = self.entry_password.get()

            if userName == "" or Password == "":
                cg.messagebox.showerror("Erro", "Por favor, insira o nome de usuário e senha.")
                return

            cursor.execute("SELECT id_user, name_user, password, user_level FROM Users WHERE name_user = ?", (userName,))
            registro_User = cursor.fetchone()
                        
            if registro_User is None:
                cg.messagebox.showerror("Erro", "Usuário incorreto ou não existe.")
                return False

            if Password != registro_User[2]:
                cg.messagebox.showerror("Erro", "Senha incorreta.")
                return False

            cg.messagebox.showinfo("Login", "Bem Vindo, {}".format(registro_User[1]))
            self.iden = registro_User[0]
            #self.export_ID()
            self.master.destroy()
            return True
            
        except cg.sql.Error as e:
            cg.messagebox.showerror("Erro no Banco de Dados", str(e))
            return False
        
    def export_ID(self):
        id_on = self.iden
        ident = cg.tk.Toplevel(self.master)
        Id_user(ident, id_on)

class Id_user:
    def ID_user_ON(self, id_on):
        id = id_on
        return id

#------------------------------------------

def init_log():
    log = cg.tk.Tk()
    app = Login(log)
    log.geometry("250x250")
    log.mainloop()
    #return app.login_true