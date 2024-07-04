import config as cg

#------------------------------------------
class Orders:
    def __init__(self, ordem):
        self.orde = ordem
        self.conect =  cg.sql.connect(cg.db_cam)
        self.orde.title("Ordens")
        
        self.frame_campos = cg.tk.Frame(self.orde, bg="#B2B3B3")
        self.frame_campos.grid(row=0, column=1, columnspan=4, sticky="ew")

        self.buton_frame = cg.tk.Frame(self.orde)
        self.buton_frame.grid(row=4, column=2, columnspan=2, sticky="s")
        
        self.orde.grid_rowconfigure(4, weight=1)
        self.orde.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        
        self.frame_campos.grid_rowconfigure(9, weight=1)
        self.frame_campos.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        
        self.buton_frame.grid_rowconfigure(2, weight=1)
        self.buton_frame.grid_columnconfigure((0,1,2), weight=1)
                
        self.line_entries = []
        
        self.entrys()
        self.btns()
                 
    #--------------------------

    def entrys(self):
        self.font_1 = ("Arial", 16)
        self.font_2 = ("Arial", 20)
        
        #- Inicio Row 0 -
        self.type_lbl = cg.tk.Label(self.frame_campos, font=self.font_2, text=f"Ordem de Requisição")
        self.type_lbl.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
                                        
        self.num_order_lbl = cg.tk.Label(self.frame_campos, font=self.font_2)
        self.num_order_lbl.grid(row=0, column=3, padx=5, pady=5)
        
        self.date_lbl = cg.tk.Label(self.frame_campos, font=self.font_2)
        self.date_lbl.grid(row=0, column=4, padx=5, pady=5)
        #- Fim Row 0 -
        
        #-- Inicio Row 1 --
        self.line_lbl = cg.tk.Label(self.frame_campos, font=self.font_1, text="Item")
        self.line_lbl.grid(row=1, column=0, padx=5, pady=5)
        
        self.cod_lbl = cg.tk.Label(self.frame_campos, font=self.font_1, text="Código interno")
        self.cod_lbl.grid(row=1, column=1, padx=5, pady=5)
        
        self.desc_lbl = cg.tk.Label(self.frame_campos, font=self.font_1, text="Descrição")
        self.desc_lbl.grid(row=1, column=2, columnspan=2, padx=5, pady=5)
        
        self.qtde_lbl = cg.tk.Label(self.frame_campos, font=self.font_1, text="Qtde")
        self.qtde_lbl.grid(row=1, column=4, padx=5, pady=5)
        #-- Fim Row 1 --
        
        #--- Inicio Row 2~9 ---
        self.lines_ent(2)
        #--- Fim Row 2~9 ---  
        
        self.format_id()
        self.data_time()
 
    #--------------------------
    #-- Formatando o id da ordem, verificando no BD e atualizando a cadanova oordem aberta
    def format_id(self):
        cursor = self.conect.cursor()
        
        cursor.execute("SELECT MAX(id_order) FROM Orders")
        last_id = cursor.fetchall()[0]
                
        if last_id[0] is None:
            new_id = 1
        else:
            ref_id = int(last_id[0])
            new_id = ref_id + 1
            
        self.num_order_lbl.config(text=f"N° {new_id}")
        
    #--------------------------
    #-- Passando data-hora da máquina para o campo de date_lbl
    def data_time(self):
        time = cg.dt.datetime.now()
        format_time = time.strftime('%Y/%m/%d \n %H:%M')
        
        self.date_lbl.config(text=f"{format_time}")
        if self.orde.winfo_exists():
            self.orde.after(1000, self.data_time)
    
    #--------------------------

    def lines_ent(self, line_number):
        if not hasattr(self, 'number_lines'):
            self.number_lines = []
        self.number_lines.append(line_number)

        self.num_line = cg.tk.Label(self.frame_campos, font=self.font_1, text=f"{line_number-1}")
        self.num_line.grid(row=line_number, column=0, padx=5, pady=5)

        self.cod_ent = cg.tk.Entry(self.frame_campos, font=self.font_1, width=10)
        self.cod_ent.grid(row=line_number, column=1, padx=5, pady=5)

        self.desc_ent = cg.tk.Entry(self.frame_campos, font=self.font_1, width=30)
        self.desc_ent.grid(row=line_number, column=2, columnspan=2, padx=5, pady=5)

        self.qtde_ent = cg.tk.Spinbox(self.frame_campos, font=self.font_1, from_=1, to=999, width=8)
        self.qtde_ent.grid(row=line_number, column=4, padx=5, pady=5)

        self.line_entries.append((self.num_line, self.cod_ent, self.desc_ent, self.qtde_ent))

    #--------------------------
    
    def btns(self):
        fonte_3 = ("Arial", 32)
        
        self.add_line_btn = cg.tk.Button(self.buton_frame,text= "+" , command=self.add_line, font=fonte_3,  bd=1, highlightthickness=1, width=3, height=1)
        self.add_line_btn.grid(row=1, column=0, padx=5, pady=5)
    
        self.test_btn = cg.tk.Button(self.buton_frame,text= "-" , command=self.delete_last_line, font=fonte_3, bd=1, highlightthickness=1, width=3, height=1)
        self.test_btn.grid(row=1, column=1, padx=5, pady=5)
        
        self.save_btn = cg.tk.Button(self.buton_frame, text="Salvar\nOrdem", font=self.font_2, bd=2, highlightthickness=2, command=self.save_order)
        self.save_btn.grid(row=1, column=2, padx=5, pady=5)
     
    def add_line(self):
        if len(self.number_lines) < 7:
            next_line_number = len(self.number_lines) + 2
            self.lines_ent(next_line_number)
        else:
            cg.msg.showwarning("Aviso", "O limite é de 7 itens por ordem.")
            return
        #print("Botao funcionando")
    
    def delete_last_line(self):
        if self.number_lines:
            last_line_number = self.number_lines[-1]
            for widget in self.line_entries[-1]:
                widget.destroy()
            self.line_entries.pop()
            self.number_lines.pop()
            # print(f"Linha {last_line_number} deletada")
    
    #-----------------------------
    
    def save_order(self):
        cg.msg.showinfo("Ok")
    
    
#------------------------------------------

def init_orders():
    Ordens = cg.tk.Tk()
    app = Orders(Ordens)
    Ordens.geometry("800x500")
    Ordens.mainloop()

init_orders()