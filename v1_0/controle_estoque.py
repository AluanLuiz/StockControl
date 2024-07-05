#2023-12-06
#Finalizado em 2024-02-16
#Controle de Estoque, com bd

import tkinter as tk
from tkinter import messagebox
from tkinter import font
import sqlite3 as sql
import os #"Ative se quiser verificar pelo terminal o reload -1"


#- Início da classe ControleEstoque -----------------------------------------

class ControleEstoque:
    def __init__(self,master):
        self.master = master

        self.master.title("Controle de Estoque")
        db_v1 = "v1_0/armazem.db"
        self.conexao = sql.connect(db_v1)
        self.criar_tabela()

        self.start_timer()

        self.font_1 = font.Font(family="Arial", size=16)
        self.font_2 = font.Font(family="Arial", size=14)
        self.font_3 = font.Font(family="Arial", size=10)


        self.title = tk.Label(master, text="Controle de Estoque", font=self.font_1)
        self.title.grid(row=0, column=1, columnspan=2, pady=10)

        self.bt_cadProdut = tk.Button(master, text="Cadastrar Produto", font=self.font_2, command=self.forms_CadProd)
        self.bt_cadProdut.grid(row=0, column=3, columnspan=2, padx=10, pady=10)

        self.listViewer = tk.Listbox(master, selectmode=tk.MULTIPLE, height=20, width=88, font=self.font_3)
        self.listViewer.grid(row=1, column=1, columnspan=3, padx=15, pady=10)

        # self.bt_reload = tk.Button(master, text="Atualizar  ", font=self.font_2, command=self.load_listview)
        # self.bt_reload.grid(row=2, column=2, pady=10)
        self.bt_darBaixa = tk.Button(master, text="Dar Baixa", font=self.font_2, command=self.saidaProdut)
        self.bt_darBaixa.grid(row=2, column=3, pady=10)

        self.load_listview()

    #------------------------------------------

    def forms_CadProd(self):
        cad_produt = tk.Toplevel(self.master)
        CadastroProduto(cad_produt)

    #------------------------------------------

    def saidaProdut(self):
        produt_id = self.obter_codBarras()
        # OR - produt_id = self.obter_id()
        baixa_estoque = tk.Toplevel(self.master)
        BaixaEstoque(baixa_estoque, produt_id)

    #------------------------------------------

    def load_listview(self):
        self.listViewer.delete(0, tk.END)

        cursor = self.conexao.cursor()
        cursor.execute("SELECT id, cod_barras, nome_produto, quant_dispon, valor_venda, fornecedor, valor_fornecedor FROM estoque")
        registros = cursor.fetchall()

        for registro in registros:
            info_produt = self.formatar_info(registro)
            self.listViewer.insert(tk.END, info_produt)
            #print(info_produt) -1

    def formatar_info(self, item):
        return f"{item[0]}, {item[1]} - {item[2]}, Disponível: {item[3]}, R${item[4]} - {item[5]}, ultímo preço R${item[6]}"\

    #------------------------------------------

    def start_timer(self, interval_ms=5000):
        self.master.after(interval_ms, self.reload_listview)

    def reload_listview(self):
        #self.clear_terminal() -1
        self.load_listview()
        self.start_timer()

    #------------------------------------------

    def criar_tabela(self):
        cursor = self.conexao.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS estoque (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           nome_produto TEXT NOT NULL,
                           cod_barras TEXT CHECK(LENGTH(cod_barras) = 13),
                           quant_dispon INTERGER NOT NULL,
                           valor_venda REAL NOT NULL,
                           fornecedor TEXT NOT NULL,
                           valor_fornecedor REAL NOT NULL
                        )
                    ''')
        self.conexao.commit()
    #------------------------------------------

    # def obter_id(self):  #Obtem o id único do banco de dados
    #     selecionados = self.listViewer.curselection()

    #     if selecionados:
    #         index = selecionados[0]
    #         produt_selecionado = self.listViewer.get(index).split(", ")[0]

    #         cursor = self.conexao.cursor()
    #         cursor.execute("SELECT id FROM estoque WHERE id = ?", (produt_selecionado,))
    #         tarefa_id = cursor.fetchone()

    #         if tarefa_id:
    #             return tarefa_id[0]
    #         else:
    #             print(f"Produto selecionado: {produt_selecionado}")
    #             print("ID não encontrado no banco de dados.")
    #             return None
    #     else:
    #         print("Nenhum item selecionado.")
    #         return None

    def obter_codBarras(self): # Obtem o código de barras do produto no banco de dados, como se tivesse usado o leitor físico
        selecionados = self.listViewer.curselection()

        if selecionados:
            index = selecionados[0]
            # ↓ Isolando o código de barras da string selecionada da listViewer.
            codbarras = self.listViewer.get(index).split(", ")[1]  # Obtem do index a string após a ,
            produt_selecionado = codbarras.split(" - ")[0] # Isola o código de barras da string que está antes do -

            cursor = self.conexao.cursor()
            cursor.execute("SELECT cod_barras FROM estoque WHERE cod_barras = ?", (produt_selecionado,))
            tarefa_codBarras = cursor.fetchone()

            if tarefa_codBarras:
                return tarefa_codBarras[0]
            else:
                print(f"Produto selecionado: {produt_selecionado}")
                print("Código de barras não encontrado no banco de dados.")
                return None
        else:
            print("Nenhum item selecionado.")
            return None

    #------------------------------------------
    # Utíl para manutenção e/ou verificação do banco -1
    # def clear_terminal(self): -1
    #     os.system('cls' if os.name == 'nt' else 'clear') -1

#- Fim da classe ControleEstoque -----------------------------------------

#- Início da classe BaixaEstoque -----------------------------------------
class BaixaEstoque:
    def __init__(self, baixa, produt_id):
        self.baixa = baixa
        self.baixa.geometry("360x350")
        self.baixa.title("Cadastro de Produto")

        self.produto = produt_id

        self.conexao = sql.connect("armazem.db")
        self.infoProdut()

        self.font_1 = font.Font(family="Arial", size=16)
        self.font_2 = font.Font(family="Arial", size=14)

        self.lbl_nomeProd = tk.Label(baixa, text=f"Produto: {self.nome_produto}", font=self.font_1)
        self.lbl_nomeProd.grid(row=0, column=0, padx=10, pady=10)
        
        self.lbl_codBar = tk.Label(baixa, text=f"Código de Barras: {self.cod_barras}", font=self.font_1)
        self.lbl_codBar.grid(row=1, column=0, padx=10, pady=10)
        
        self.lbl_fornecedor = tk.Label(baixa, text=f"Fornecedor: {self.fornecedor}", font=self.font_1)
        self.lbl_fornecedor.grid(row=2, column=0, padx=10, pady=10)
        
        self.lbl_quant = tk.Label(baixa, text=f"Quantidade Disponível: {self.quant_dispon} Un", font=self.font_2)
        self.lbl_quant.grid(row=3, column=0, padx=10, pady=10)

        self.lbl_quant_retirar = tk.Label(baixa, text="Quantidade a Retirar:", font=self.font_2)
        self.lbl_quant_retirar.grid(row=4, column=0, padx=10, pady=10)
        
        self.spin_quant_Aretirar = tk.Spinbox(self.baixa, from_=0, to=self.quant_dispon, font=self.font_2)
        self.spin_quant_Aretirar.grid(row=5, column=0, padx=10, pady=10)
        
        self.btn_confirmar = tk.Button(baixa, text="Confirmar", font=self.font_2, command=self.confirmar_baixa)
        self.btn_confirmar.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    #------------------------------------------

    def confirmar_baixa(self):
        quant_a_retirar = int(self.spin_quant_Aretirar.get())
        if quant_a_retirar > 0:
            confirmacao = messagebox.askyesno("Confirmação", f"Deseja retirar {quant_a_retirar} unidades?")
            if confirmacao:
                nova_quantidade = self.quant_dispon - quant_a_retirar
                cursor = self.conexao.cursor()
                cursor.execute("UPDATE estoque SET quant_dispon = ? WHERE cod_barras = ?", (nova_quantidade, self.cod_barras))
                self.conexao.commit()
                self.baixa.destroy()
        else:
            messagebox.showwarning("Seleção Inválida", "Selecione uma quantidade válida para retirar.")
            cursor.close() 
            self.baixa.destroy()

    #------------------------------------------

    def infoProdut(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT nome_produto, cod_barras, fornecedor, quant_dispon FROM estoque WHERE cod_barras = ?", (self.produto,))
        registro = cursor.fetchone()
            
        if registro is not None:
            
            self.nome_produto = registro[0]
            self.cod_barras = registro[1]
            self.fornecedor = registro[2]
            self.quant_dispon = registro[3]
            
            # print(f"Produto: {nome_produto}")
            # print(f"Código de Barras: {cod_barras}")
            # print(f"Fornecedor: {fornecedor}")
            # print(f"Quantidade Disponível: {quant_dispon} Un")
        
        else:
            messagebox.showwarning("Produto não encontrado", "O produto não foi encontrado no estoque.")
            cursor.close()
            self.baixa.destroy()
    #------------------------------------------
    
#- Fim da classe BaixaEstoque -----------------------------------------

#- Início da classe CadastroProduto -----------------------------------------

class CadastroProduto:
    def __init__(self, cad):
        self.cad = cad
        self.cad.geometry("430x350")
        self.cad.title("Cadastro de Produto")

        self.conexao = sql.connect("armazem.db")

        self.font_2 = font.Font(family="Arial", size=14)

        self.lbl_nome = tk.Label(cad, text="Nome do Produto:", font=self.font_2)
        self.lbl_nome.grid(row=0, column=0, padx=10, pady=10)
        self.txt_nome = tk.Entry(cad)
        self.txt_nome.grid(row=0, column=1, padx=10, pady=10)

        self.lbl_codBarras = tk.Label(cad, text="Código de Barras do Produto:", font=self.font_2)
        self.lbl_codBarras.grid(row=1, column=0, padx=10, pady=10)
        self.txt_codBarras = tk.Entry(cad)
        self.txt_codBarras.grid(row=1, column=1, padx=10, pady=10)

        self.lbl_quant = tk.Label(cad, text="Quantidade Disponível:", font=self.font_2)
        self.lbl_quant.grid(row=2, column=0, padx=10, pady=10)
        self.txt_quant = tk.Entry(cad)
        self.txt_quant.grid(row=2, column=1, padx=10, pady=10)

        self.lbl_valorVenda = tk.Label(cad, text="Valor de Venda: R$", font=self.font_2)
        self.lbl_valorVenda.grid(row=3, column=0, padx=10, pady=10)
        self.txt_valorVenda = tk.Entry(cad)
        self.txt_valorVenda.grid(row=3, column=1, padx=10, pady=10)

        self.lbl_fornecedor = tk.Label(cad, text="Fornecedor:", font=self.font_2)
        self.lbl_fornecedor.grid(row=4, column=0, padx=10, pady=10)
        self.txt_fornecedor = tk.Entry(cad)
        self.txt_fornecedor.grid(row=4, column=1, padx=10, pady=10)

        self.lbl_valorFornec = tk.Label(cad, text="Valor do fornecedor: R$", font=self.font_2)
        self.lbl_valorFornec.grid(row=5, column=0, padx=10, pady=10)
        self.txt_valorFornec = tk.Entry(cad)
        self.txt_valorFornec.grid(row=5, column=1, padx=10, pady=10)

        self.btn_salvar = tk.Button(cad, text="Salvar", font=self.font_2, command=self.salvar_produto)
        self.btn_salvar.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

        self.btn_sair = tk.Button(cad, text="Sair", font=self.font_2, command=self.sair)
        self.btn_sair.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    #------------------------------------------

    def salvar_produto(self):
        cadastroValido = self.validarCad()

        if cadastroValido == "Válido":
            nome_prod = self.txt_nome.get()
            codBarras_prod = self.txt_codBarras.get()
            quant_prod = self.txt_quant.get()
            valorV = self.txt_valorVenda.get()
            fornecedor = self.txt_fornecedor.get()
            valorF = self.txt_valorFornec.get()

            cursor = self.conexao.cursor()

            try:
                cursor.execute("INSERT INTO estoque (nome_produto, cod_barras, quant_dispon, valor_venda, fornecedor, valor_fornecedor) VALUES (?, ?, ?, ?, ?, ?)",
                               (nome_prod, codBarras_prod, quant_prod, valorV, fornecedor, valorF))
                self.conexao.commit()

                self.txt_nome.delete(0, tk.END)
                self.txt_codBarras.delete(0, tk.END)
                self.txt_quant.delete(0, tk.END)
                self.txt_valorVenda.delete(0, tk.END)
                self.txt_fornecedor.delete(0, tk.END)
                self.txt_valorFornec.delete(0, tk.END)
                
                self.cad.destroy()
                cursor.close()
            except sql.Error as e:
                cursor.close()
                print("Erro ao salvar o cadastro do produto:", e)
                messagebox.showerror("Erro", "Não foi possível salvar o cadastro do produto")

    #------------------------------------------

    def validarCad(self):
        nome_prod = self.txt_nome.get()
        codBarras_prod = self.txt_codBarras.get()
        quant_prod = self.txt_quant.get()
        valorV = self.txt_valorVenda.get()
        fornecedor = self.txt_fornecedor.get()
        valorF = self.txt_valorFornec.get()

        cursor = self.conexao.cursor()

        try:

            if nome_prod.strip() == "":
                messagebox.showerror("Erro", "Nome do produto não pode ser vazio")
                return

            cursor.execute("SELECT cod_barras FROM estoque WHERE cod_barras = ? ", (codBarras_prod,))
            cod_salvo = cursor.fetchone()
            if cod_salvo and cod_salvo[0] == codBarras_prod:
                messagebox.showerror("Erro", "O Código de Barras já existe.")
                return

            elif len(codBarras_prod) != 13:
                messagebox.showerror("Erro", "Código de Barras Invalido")
                return

            try:
                quant_prod = int(quant_prod)
                if quant_prod < 0:
                    messagebox.showerror("Erro", "A quantidade deve ser um número inteiro positivo.")
                    return
            except ValueError:
                messagebox.showerror("Erro", "A quantidade deve ser um número inteiro.")
                return

            try:
                valorV = float(valorV)
                if valorV < 0:
                    messagebox.showerror("Erro", "O valor de venda deve ser um número positivo.")
                    return
            except ValueError:
                messagebox.showerror("Erro", "O valor de venda deve ser um número.")
                return

            if fornecedor.strip() == "":
                messagebox.showerror("Erro", "Nome do Fornecedor não pode ser vazio")
                return

            try:
                valorF = float(valorF)
                if valorF < 0:
                    messagebox.showerror("Erro", "O valor de compra do fornecedor deve ser um número positivo.")
                    return
            except ValueError:
                messagebox.showerror("Erro", "O valor de compra do fornecedor deve ser um número.")
                return

        except sql.Error as e:
            print("Erro ao salvar o cadastro do produto:", e)
            messagebox.showerror("Erro", "Não foi possível salvar o cadastro do produto")
            return
        finally:
            cursor.close()

        return "Válido"

    #------------------------------------------

    def sair(self):
        self.cad.destroy()

#- Fim da classe CadastroProduto -----------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = ControleEstoque(root)
    root.geometry("650x500")
    root.mainloop()