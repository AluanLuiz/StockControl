import config as cg

#------------------------------------------
class Orders:
    def __init__(self, ordem):
        self.orde = ordem
        self.conect =  cg.sql.connect(cg.db_cam)
        self.orde.title("Ordens")
        
        self.frame_campos = cg.tk.Frame(self.orde)
        self.frame_campos.grid(row=0, column=0, columnspan=5, sticky="ew")

        self.buton_frame = cg.tk.Frame(self.orde)
        self.buton_frame.grid(row=1, column=0, columnspan=5, sticky="ew")
        
        self.orde.grid_rowconfigure(2, weight=1)
        self.orde.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        
        self.select()
        #self.entrys()
        
    #--------------------------
    
    def select(self):
        font_1 = ("Arial", 16)
        self.var_radio = cg.tk.StringVar()
        self.var_radio.set("Requisição")

        cg.tk.Radiobutton(self.frame_campos, text="Requisição", variable=self.var_radio, 
                          value="Requisição", font=font_1).grid(row=0, column=0, sticky="w")
        cg.tk.Radiobutton(self.frame_campos, text="Devolução", variable=self.var_radio, 
                          value="Devolução", font=font_1).grid(row=0, column=2, sticky="w")
        
        self.bttt = cg.tk.Button(self.buton_frame, text="Verificar", command=self.entrys).grid(row=0, column=0, sticky="w")

    
    def entrys(self):
        font_1 = ("Arial", 16)
        font_2 = ("Arial", 14)
        
        selection = self.var_radio.get()
        
        if selection == "Requisição":
            print(selection)
            
        elif selection == "Devolução":
            print(selection)
            
        else:
            print("erro")

            
#------------------------------------------

def init_orders():
    Ordens = cg.tk.Tk()
    app = Orders(Ordens)
    Ordens.geometry("500x500")
    Ordens.mainloop()
    
# init_orders()