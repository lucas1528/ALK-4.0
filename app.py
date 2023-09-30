from tkinter import *
from tkinter import ttk
from database import Database
from functions import Functions
from injetor import Injetor
from placeholderentry import PlaceholderEntry
from colors import Colors
import validate
from relatorio import Relatorio_Injetor, Relatorio_Bomba

root = Tk()

class Application():
    def __init__(self):
        self.root:Tk = root
        self.criando_variaveis()
        self.config_colors()
        self.criando_layout()
        self.config_functions()
        self.config_regras()
        
        # CONFIGURANDO OS ELEMENTOS DE INTERAÇÃO

        root.mainloop()

    def criando_variaveis(self):
        self.injetor = None
        self.testes = list()
        self.injetores_testados = 0

    def config_colors(self):
        self.colors = Colors()

    def config_regras(self):
        self.carregar_todos_injetores()

    def carregar_todos_injetores(self):
        # carregando injetores ao iniciar
        injetores = self.functions.get_injetores()
        for i, injetor in enumerate(injetores):
            self.lista_injetores.insert(i, injetor)

    def config_functions(self):
        self.functions = Functions()

        # selecionando injetor
        self.lista_injetores.bind('<<ListboxSelect>>', self.selecionar_injetor)

        # pesquisar injetor
        self.pesquisar.bind('<KeyRelease>', self.pesquisar_injetor)
    
        # selecionar fabricante
        self.lista_fabricantes.bind('<<ComboboxSelected>>', self.selecionar_fabricante)

        # selecionando parametros do teste
        self.teste.bind('<<ComboboxSelected>>', self.selecionar_teste)

        # limpar entradas
        self.bt_limpar.bind('<Button-1>', self.limpar_entradas)

        # salvar laudo
        self.bt_salvar.bind('<Button-1>', self.salvar)

    
    def salvar(self, event):
        self.injetores_testados += 1
        teste = {
            '-DEBITO DDP-': self.entrada_debito_dp.get(),
            '-RETORNO DDP-': self.entrada_retorno_dp.get(),
            '-DEBITO ML-': self.entrada_debito_ml.get(),
            '-RETORNO ML-': self.entrada_retorno_ml.get(),
            '-DEBITO CP-': self.entrada_debito_cp.get(),
            '-RETORNO CP-': self.entrada_retorno_cp.get(),
            '-DEBITO PC-': self.entrada_debito_pc.get(),
            '-RETORNO PC-': self.entrada_retorno_pc.get(),
            '-DEBITO PI-': self.entrada_debito_pi.get(),
            '-RETORNO PI-': self.entrada_retorno_pi.get(),
        }
        self.testes.append(teste)
        if self.injetores_testados == self.quantidade_de_injetores.current()+1:
            injetor = self.injetor
            testes = self.testes

            testes.insert(0, {'-QUANTIDADE DE INJETORES-': self.quantidade_de_injetores.current()+1})


            self.gerar_relatorio(testes, injetor)
            
            self.testes = list()
            self.injetores_testados = 0
        else:
            self.limpar_entradas()
    

    def gerar_relatorio(self, testes, injetor):
        relatorio = Relatorio_Injetor(testes, injetor)
        relatorio.gerar()

    def limpar_entradas(self, event=None):
        self.entrada_debito_dp.delete(0, END)
        self.entrada_debito_ml.delete(0, END)
        self.entrada_debito_cp.delete(0, END)
        self.entrada_debito_pc.delete(0, END)
        self.entrada_debito_pi.delete(0, END)
        
        self.entrada_retorno_dp.delete(0, END)
        self.entrada_retorno_ml.delete(0, END)
        self.entrada_retorno_cp.delete(0, END)
        self.entrada_retorno_pc.delete(0, END)
        self.entrada_retorno_pi.delete(0, END)

        self.entrada_debito_dp.focus()
    
    def selecionar_teste(self, event=None):
        if self.injetor != None:
            teste = self.teste.get()

            if teste == 'Débito de Partida':
                self.pressao.configure(text=f'{self.injetor.pressao_ddp}')
                self.pulso.configure(text=f'{self.injetor.pulso_ddp}')
                self.frequencia.configure(text=f'{self.injetor.frequencia_ddp}')
                self.injetadas.configure(text=f'{self.injetor.injetadas_ddp}')
            elif teste == 'Marcha Lenta':
                self.pressao.configure(text=f'{self.injetor.pressao_ml}')
                self.pulso.configure(text=f'{self.injetor.pulso_ml}')
                self.frequencia.configure(text=f'{self.injetor.frequencia_ml}')
                self.injetadas.configure(text=f'{self.injetor.injetadas_ml}')
            elif teste == 'Carga Parcial':
                self.pressao.configure(text=f'{self.injetor.pressao_cp}')
                self.pulso.configure(text=f'{self.injetor.pulso_cp}')
                self.frequencia.configure(text=f'{self.injetor.frequencia_cp}')
                self.injetadas.configure(text=f'{self.injetor.injetadas_cp}')
            elif teste == 'Plena Carga':
                self.pressao.configure(text=f'{self.injetor.pressao_pc}')
                self.pulso.configure(text=f'{self.injetor.pulso_pc}')
                self.frequencia.configure(text=f'{self.injetor.frequencia_pc}')
                self.injetadas.configure(text=f'{self.injetor.injetadas_pc}')
            elif teste == 'Pré-Injeção':
                self.pressao.configure(text=f'{self.injetor.pressao_pi}')
                self.pulso.configure(text=f'{self.injetor.pulso_pi}')
                self.frequencia.configure(text=f'{self.injetor.frequencia_pi}')
                self.injetadas.configure(text=f'{self.injetor.injetadas_pi}')

    def selecionar_fabricante(self, event):
        self.pesquisar.remove(0, END)
        

        combobox = event.widget
        fabricante = combobox.get()

        if fabricante != 'Todos':
            lista_injetores = self.functions.selecionar_fabricante(fabricante)

            self.lista_injetores.delete(0, END)
            for i, injetor in enumerate(lista_injetores):
                self.lista_injetores.insert(i, injetor.codigo)

        else:
            self.carregar_todos_injetores()

    def pesquisar_injetor(self, event):
        self.lista_fabricantes.current(0)

        text = self.pesquisar.get()
        if text != 'Pesquisar':
            lista_injetores = self.functions.pesquisar_injetor(text)

            self.lista_injetores.delete(0, END)
            for i, injetor in enumerate(lista_injetores):
                self.lista_injetores.insert(i, injetor.codigo)
        
        else:
            self.carregar_todos_injetores()

    def selecionar_injetor(self, event):
        self.injetor: Injetor = self.functions.get_injetor(event)

        self.lista_injetores.select_anchor = event.widget.curselection()

        self.codigo.configure(text=self.injetor.codigo)
        self.tipo.configure(text=self.injetor.tipo)

        self.label_debito_dp.configure(text=f'{self.injetor.pd_ddp_menor}  a  {self.injetor.pd_ddp_maior}')
        self.label_debito_ml.configure(text=f'{self.injetor.pd_ml_menor}  a  {self.injetor.pd_ml_maior}')
        self.label_debito_cp.configure(text=f'{self.injetor.pd_cp_menor}  a  {self.injetor.pd_cp_maior}')
        self.label_debito_pc.configure(text=f'{self.injetor.pd_pc_menor}  a  {self.injetor.pd_pc_maior}')
        self.label_debito_pi.configure(text=f'{self.injetor.pd_pi_menor}  a  {self.injetor.pd_pi_maior}')

        self.label_retorno_dp.configure(text=f'0  a  {self.injetor.pr_ddp}')
        self.label_retorno_ml.configure(text=f'0  a  {self.injetor.pr_ml}')
        self.label_retorno_cp.configure(text=f'0  a  {self.injetor.pr_cp}')
        self.label_retorno_pc.configure(text=f'0  a  {self.injetor.pr_pc}')
        self.label_retorno_pi.configure(text=f'0  a  {self.injetor.pr_pi}')

        self.selecionar_teste()

        self.bt_salvar.configure(state=NORMAL)

    def criando_layout(self):
        self.tela()
        self.criando_frames()

        # FRAME CONFIG
        # self.criando_botoes_config()
        self.criando_entradas_config()
        self.criando_listas_config()
        self.criando_combobox_config()
        self.criando_labels_config()

        # FRAME PRINCIPAL
        self.criando_botoes_principal()
        self.criando_entradas_principal()
        self.criando_combobox_principal()
        self.criando_labels_principal()
        self.criando_labels_parametros_principal()

    def tela(self):
        self.root.title('ALK ELETRODIESEL - TABELA DIGITAL')
        self.root.configure(background='#1e3743')
        self.root.iconbitmap('icone.ico')
        self.root.geometry('900x650')
        self.root.maxsize(width=1000, height=700)
        self.root.minsize(width=900, height=650)

    def criando_frames(self):
        self.frame_config = Frame(
            self.root,
            background=self.colors.BG_FRAME_CONFIG,
            highlightbackground=self.colors.HIGHLIGHTBACKGROUND_CONFIG,
            highlightthickness=2
            )
        self.frame_config.place(relx=0.02, rely=0.03, relwidth=0.96, relheight=0.455)

        self.frame_principal = Frame(
            self.root,
            background=self.colors.BG_FRAME_CONFIG,
            highlightbackground=self.colors.HIGHLIGHTBACKGROUND_CONFIG,
            highlightthickness=2
            )
        self.frame_principal.place(relx=0.02, rely=0.515, relwidth=0.96, relheight=0.455)

    # FRAME CONFIG

    # def criando_botoes_config(self):
    #     self.bt_buscar = Button(self.frame_config, text='Buscar')
    #     self.bt_buscar.place(relx=0.3, rely=0.05, relwidth=0.1, relheight=0.1)

    def criando_entradas_config(self):
        self.pesquisar = PlaceholderEntry(self.frame_config, placeholder='Pesquisar')
        self.pesquisar.focus()
        self.pesquisar.place(relx=0.1, rely=0.05, relwidth=0.19, relheight=0.1)

    def criando_listas_config(self):
        font = ('Times', 17)

        self.lista_injetores = Listbox(self.frame_config, font=font, selectmode=SINGLE, exportselection=False)
        self.lista_injetores.place(relx=0.1, rely=0.28, relwidth=0.3, relheight=0.67)

    def criando_combobox_config(self):
        lista_fabricantes = ['Todos', 'Bosch', 'Denso', 'Siemens', 'Delphi']
        self.lista_fabricantes = ttk.Combobox(self.frame_config, values=lista_fabricantes, state='readonly', exportselection=False)
        self.lista_fabricantes.current(0)
        self.lista_fabricantes.place(relx=0.1, rely=0.17, relwidth=0.3, relheight=0.1)
        
        quantidade_de_injetores = ['1 Injetor', '2 Injetores', '3 Injetores', '4 Injetores', '5 Injetores', '6 Injetores']
        self.quantidade_de_injetores = ttk.Combobox(self.frame_config, values=quantidade_de_injetores, state='readonly', exportselection=False)
        self.quantidade_de_injetores.current(0)
        self.quantidade_de_injetores.place(relx=0.41, rely=0.17, relwidth=0.15, relheight=0.1)

    def criando_labels_config(self):
        font = ('Times', 15)

        self.label_pressão = Label(
            self.frame_config,
            text='Pressão:',
            bg=self.colors.BG_FRAME_CONFIG,
            font=font
            )
        self.label_pressão.place(relx=0.6, rely=0.55)

        self.label_pulso = Label(
            self.frame_config,
            text='Pulso:',
            bg=self.colors.BG_FRAME_CONFIG,
            font=font
            )
        self.label_pulso.place(relx=0.8, rely=0.55)

        self.label_frequencia = Label(
            self.frame_config,
            text='Frequência:',
            bg=self.colors.BG_FRAME_CONFIG,
            font=font
            )
        self.label_frequencia.place(relx=0.6, rely=0.8)

        self.label_injetadas = Label(
            self.frame_config,
            text='Injetadas:',
            bg=self.colors.BG_FRAME_CONFIG,
            font=font
            )
        self.label_injetadas.place(relx=0.8, rely=0.8)

        self.label_codigo = Label(
            self.frame_config,
            text='Código:',
            bg=self.colors.BG_FRAME_CONFIG,
            font=font
            )
        self.label_codigo.place(relx=0.41, rely=0.3)

        self.label_tipo = Label(
            self.frame_config,
            text='Tipo:',
            bg=self.colors.BG_FRAME_CONFIG,
            font=font
            )
        self.label_tipo.place(relx=0.41, rely=0.45)

        self.pressao = Label(
            self.frame_config,
            text='0',
            bg=self.colors.BG_FRAME_CONFIG,
            font=font
        )
        self.pressao.place(relx=0.689, rely=0.55)

        self.pulso = Label(
            self.frame_config,
            text='0',
            bg=self.colors.BG_FRAME_CONFIG,
            font=font
        )
        self.pulso.place(relx=0.87, rely=0.55)

        self.frequencia = Label(
            self.frame_config,
            text='0',
            bg=self.colors.BG_FRAME_CONFIG,
            font=font
        )
        self.frequencia.place(relx=0.72, rely=0.8)

        self.injetadas = Label(
            self.frame_config,
            text='0',
            bg=self.colors.BG_FRAME_CONFIG,
            font=font
        )
        self.injetadas.place(relx=0.9, rely=0.8)

        self.codigo = Label(
            self.frame_config,
            text='',
            bg=self.colors.BG_FRAME_CONFIG,
            font=font
        )
        self.codigo.place(relx=0.49, rely=0.3)

        self.tipo = Label(
            self.frame_config,
            text='',
            bg=self.colors.BG_FRAME_CONFIG,
            font=font
        )
        self.tipo.place(relx=0.47, rely=0.45)

    # FRAME PRINCIPAL

    def criando_botoes_principal(self):
        self.bt_limpar = Button(self.frame_principal, text='Limpar')
        self.bt_limpar.place(relx=0.8, rely=0.35, relwidth=0.1, relheight=0.1)

        self.bt_salvar = Button(self.frame_principal, text='Salvar', state=DISABLED)
        self.bt_salvar.place(relx=0.8, rely=0.5, relwidth=0.1, relheight=0.1)

    def criando_combobox_principal(self):
        testes = ['Débito de Partida', 'Marcha Lenta', 'Carga Parcial', 'Plena Carga', 'Pré-Injeção']
        self.teste = ttk.Combobox(self.frame_principal, values=testes, state='readonly', exportselection=False)
        self.teste.current(0)
        self.teste.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.1)

    def criando_labels_principal(self):
        font = ('Times', 13)

        self.label_debito_partida = Label(
            self.frame_principal,
            text='Débito de Partida',
            bg=self.colors.BG_FRAME_PRINCIPAL,
            font=font
        )
        self.label_debito_partida.place(relx=0.1, rely=0.25)

        self.label_marcha_lenta = Label(
            self.frame_principal,
            text='Marcha Lenta',
            bg=self.colors.BG_FRAME_PRINCIPAL,
            font=font
        )
        self.label_marcha_lenta.place(relx=0.1, rely=0.40)

        self.label_carga_parcial = Label(
            self.frame_principal,
            text='Carga Parcial',
            bg=self.colors.BG_FRAME_PRINCIPAL,
            font=font
        )
        self.label_carga_parcial.place(relx=0.1, rely=0.55)

        self.label_plena_carga = Label(
            self.frame_principal,
            text='Plena Carga',
            bg=self.colors.BG_FRAME_PRINCIPAL,
            font=font
        )
        self.label_plena_carga.place(relx=0.1, rely=0.70)

        self.label_pre_injecao = Label(
            self.frame_principal,
            text='Pré-Injeção',
            bg=self.colors.BG_FRAME_PRINCIPAL,
            font=font
        )
        self.label_pre_injecao.place(relx=0.1, rely=0.85)

        self.label_debito = Label(
            self.frame_principal,
            text='Débito',
            bg=self.colors.BG_FRAME_PRINCIPAL,
            font=font
        )
        self.label_debito.place(relx=0.45, rely=0.15)
    
        self.label_retorno = Label(
            self.frame_principal,
            text='Retorno',
            bg=self.colors.BG_FRAME_PRINCIPAL,
            font=font
        )
        self.label_retorno.place(relx=0.57, rely=0.15)

    def criando_entradas_principal(self):
        font = ('Times', 19)
        validar_entradas_principal = (self.root.register(validate.limitar_tamanho), '%P')

        self.entrada_debito_dp = Entry(self.frame_principal, font=font, validate='key', validatecommand=validar_entradas_principal)
        self.entrada_debito_dp.place(relx=0.3, rely=0.25, relwidth=0.05, relheight=0.1)

        self.entrada_retorno_dp = Entry(self.frame_principal, font=font, validate='key', validatecommand=validar_entradas_principal)
        self.entrada_retorno_dp.place(relx=0.36, rely=0.25, relwidth=0.05, relheight=0.1)

        self.entrada_debito_ml = Entry(self.frame_principal, font=font, validate='key', validatecommand=validar_entradas_principal)
        self.entrada_debito_ml.place(relx=0.3, rely=0.4, relwidth=0.05, relheight=0.1)

        self.entrada_retorno_ml = Entry(self.frame_principal, font=font, validate='key', validatecommand=validar_entradas_principal)
        self.entrada_retorno_ml.place(relx=0.36, rely=0.4, relwidth=0.05, relheight=0.1)

        self.entrada_debito_cp = Entry(self.frame_principal, font=font, validate='key', validatecommand=validar_entradas_principal)
        self.entrada_debito_cp.place(relx=0.3, rely=0.55, relwidth=0.05, relheight=0.1)

        self.entrada_retorno_cp = Entry(self.frame_principal, font=font, validate='key', validatecommand=validar_entradas_principal)
        self.entrada_retorno_cp.place(relx=0.36, rely=0.55, relwidth=0.05, relheight=0.1)

        self.entrada_debito_pc = Entry(self.frame_principal, font=font, validate='key', validatecommand=validar_entradas_principal)
        self.entrada_debito_pc.place(relx=0.3, rely=0.7, relwidth=0.05, relheight=0.1)

        self.entrada_retorno_pc = Entry(self.frame_principal, font=font, validate='key', validatecommand=validar_entradas_principal)
        self.entrada_retorno_pc.place(relx=0.36, rely=0.7, relwidth=0.05, relheight=0.1)

        self.entrada_debito_pi = Entry(self.frame_principal, font=font, validate='key', validatecommand=validar_entradas_principal)
        self.entrada_debito_pi.place(relx=0.3, rely=0.85, relwidth=0.05, relheight=0.1)

        self.entrada_retorno_pi = Entry(self.frame_principal, font=font, validate='key', validatecommand=validar_entradas_principal)
        self.entrada_retorno_pi.place(relx=0.36, rely=0.85, relwidth=0.05, relheight=0.1)

    def criando_labels_parametros_principal(self):
        font = ('Times', 13)

        self.label_debito_dp = Label(
            self.frame_principal,
            text='0  a  0',
            bg=self.colors.BG_FRAME_PRINCIPAL,
            font=font
        )
        self.label_debito_dp.place(relx=0.45, rely=0.25)

        self.label_retorno_dp = Label(
            self.frame_principal,
            text='0  a  0',
            bg=self.colors.BG_FRAME_PRINCIPAL,
            font=font
        )
        self.label_retorno_dp.place(relx=0.57, rely=0.25)

        self.label_debito_ml = Label(
            self.frame_principal,
            text='0  a  0',
            bg=self.colors.BG_FRAME_PRINCIPAL,
            font=font
        )
        self.label_debito_ml.place(relx=0.45, rely=0.4)

        self.label_retorno_ml = Label(
            self.frame_principal,
            text='0  a  0',
            bg=self.colors.BG_FRAME_PRINCIPAL,
            font=font
        )
        self.label_retorno_ml.place(relx=0.57, rely=0.4)

        self.label_debito_cp = Label(
            self.frame_principal,
            text='0  a  0',
            bg=self.colors.BG_FRAME_PRINCIPAL,
            font=font
        )
        self.label_debito_cp.place(relx=0.45, rely=0.55)

        self.label_retorno_cp = Label(
            self.frame_principal,
            text='0  a  0',
            bg=self.colors.BG_FRAME_PRINCIPAL,
            font=font
        )
        self.label_retorno_cp.place(relx=0.57, rely=0.55)

        self.label_debito_pc = Label(
            self.frame_principal,
            text='0  a  0',
            bg=self.colors.BG_FRAME_PRINCIPAL,
            font=font
        )
        self.label_debito_pc.place(relx=0.45, rely=0.7)

        self.label_retorno_pc = Label(
            self.frame_principal,
            text='0  a  0',
            bg=self.colors.BG_FRAME_PRINCIPAL,
            font=font
        )
        self.label_retorno_pc.place(relx=0.57, rely=0.7)

        self.label_debito_pi = Label(
            self.frame_principal,
            text='0  a  0',
            bg=self.colors.BG_FRAME_PRINCIPAL,
            font=font
        )
        self.label_debito_pi.place(relx=0.45, rely=0.85)

        self.label_retorno_pi = Label(
            self.frame_principal,
            text='0  a  0',
            bg=self.colors.BG_FRAME_PRINCIPAL,
            font=font
        )
        self.label_retorno_pi.place(relx=0.57, rely=0.85)

Application()