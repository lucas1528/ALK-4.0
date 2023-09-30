import os
import subprocess
import threading
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime
from injetor import Injetor


class Relatorio_Injetor():
    def __init__(self, testes, injetor: Injetor):
        self.testes=testes[1:]
        self.dados_cliente = None
        pasta = os.path.join(os.path.expanduser('~'), 'Documents', 'laudos')
        if not os.path.exists(pasta):
            os.makedirs(pasta)
        self.save_name = os.path.join(os.path.expanduser('~'), 'Documents', 'laudos', f'laudo_{datetime.today().strftime("%d_%m_%Y_%H_%m_%S")}.pdf')
        self.canvas = canvas.Canvas(self.save_name, A4)
        # self.canvas: canvas.Canvas = canvas.Canvas(f'mypdf.pdf', A4)
        self.conts = int(testes[0]['-QUANTIDADE DE INJETORES-'])
        self.injetor = injetor
        

    def mm2p(self, milimetros):
        return milimetros / 0.352777

    def box(self, x, y, largura, altura):
        self.canvas.rect(self.mm2p(x), self.mm2p(y), self.mm2p(largura), self.mm2p(altura))

    def line(self, x1, y1, x2, y2):
        self.canvas.line(self.mm2p(x1), self.mm2p(y1), self.mm2p(x2), self.mm2p(y2))

    def string(self, x, y, fontsize, texto, font='Courier'):
        self.canvas.setFont(font, fontsize)
        self.canvas.drawString(self.mm2p(x), self.mm2p(y), texto)

    def image(self, imagem, x, y, largura, altura):
        self.canvas.drawImage(imagem, self.mm2p(x), self.mm2p(y), self.mm2p(largura), self.mm2p(altura))

    def padrao(self):

        # ALK ELETRODIESEL
        self.box(10, 190, 190, 97)
        self.line(10, 277, 200, 277)
        self.string(70, 279, 26, 'LAUDO TÉCNICO', 'Courier-Bold')

        # Cliente
        self.box(20, 200, 100, 67)
        self.line(20, 259, 120, 259)
        self.string(57, 261, 18, 'Cliente')
        self.line(21, 249, 119, 249)
        self.line(21, 239, 119, 239)
        self.line(21, 229, 119, 229)
        self.line(21, 219, 119, 219)
        self.line(21, 209, 119, 209)
        

        # Logo
        self.image('alklogo.png', 133, 212, 55, 55)

        # Data
        self.string(132, 205, 17, f'Data: {datetime.strftime(datetime.today(), "%d/%m/%Y")}')
        self.string(132, 200, 17, f'Hora: {datetime.strftime(datetime.today(), "%H:%M:%S")}')

        # Resultado
        self.box(10, 100, 190, 90)
        self.string(88, 184, 18, 'Resultado')
        self.line(10, 182, 200, 182)

        ## cabeçalho
        self.line(62, 177, 86, 177)
        self.line(62, 177, 62, 170)
        self.string(70.5, 171.5, 18, 'DP')
        self.line(86, 177, 86, 170)
        self.line(62, 170, 86, 170)

        self.line(62, 170, 86, 170)
        self.line(62, 170, 62, 163)

        # debito        
        self.string(65.7, 166.5, 12, f'{self.injetor.pd_ddp_maior}')
        self.string(65.7, 163.5, 12, f'{self.injetor.pd_ddp_menor}')

        # retorno        
        self.string(77.7, 166.5, 12, f'{self.injetor.pr_ddp}')
        self.string(77.7, 163.5, 12, '00')
        
        self.line(86, 170, 86, 163)
        self.line(62, 163, 86, 163)

        self.line(88, 177, 112, 177)
        self.line(88, 177, 88, 170)
        self.string(96.5, 171.5, 18, 'ML')
        self.line(112, 177, 112, 170)
        self.line(88, 170, 112, 170)

        self.line(88, 170, 112, 170)
        self.line(88, 170, 88, 163)

        # debito        
        self.string(91.7, 166.5, 12, f'{self.injetor.pd_ml_maior}')
        self.string(91.7, 163.5, 12, f'{self.injetor.pd_ml_menor}')

        # retorno        
        self.string(103.7, 166.5, 12, f'{self.injetor.pr_ml}')
        self.string(103.7, 163.5, 12, '00')

        self.line(112, 170, 112, 163)
        self.line(88, 163, 112, 163)

        self.line(114, 177, 138, 177)
        self.line(114, 177, 114, 170)
        self.string(122.7, 171.5, 18, 'CP')
        self.line(138, 177, 138, 170)
        self.line(114, 170, 138, 170)

        self.line(114, 170, 138, 170)
        self.line(114, 170, 114, 163)

        # debito        
        self.string(117.7, 166.5, 12, f'{self.injetor.pd_cp_maior}')
        self.string(117.7, 163.5, 12, f'{self.injetor.pd_cp_menor}')

        # retorno        
        self.string(129.7, 166.5, 12, f'{self.injetor.pr_cp}')
        self.string(129.7, 163.5, 12, '00')

        self.line(138, 170, 138, 163)
        self.line(114, 163, 138, 163)

        self.line(140, 177, 164, 177)
        self.line(140, 177, 140, 170)
        self.string(148.5, 171.5, 18, 'PC')
        self.line(164, 177, 164, 170)
        self.line(140, 170, 164, 170)

        self.line(140, 170, 164, 170)
        self.line(140, 170, 140, 163)

        # debito        
        self.string(143.5, 166.5, 12, f'{self.injetor.pd_pc_maior}')
        self.string(143.5, 163.5, 12, f'{self.injetor.pd_pc_menor}')

        # retorno        
        self.string(155.5, 166.5, 12, f'{self.injetor.pr_pc}')
        self.string(155.5, 163.5, 12, '00')

        self.line(164, 170, 164, 163)
        self.line(140, 163, 164, 163)

        self.line(166, 177, 190, 177)
        self.line(166, 177, 166, 170)
        self.string(174, 171.5, 18, 'PI')
        self.line(190, 177, 190, 170)
        self.line(166, 170, 190, 170)
        
        self.line(166, 170, 190, 170)
        self.line(166, 170, 166, 163)

        # debito        
        self.string(169.5, 166.5, 12, f'{self.injetor.pd_pi_maior}')
        self.string(169.5, 163.5, 12, f'{self.injetor.pd_pi_menor}')

        # retorno        
        self.string(181.5, 166.5, 12, f'{self.injetor.pr_pi}')
        self.string(181.5, 163.5, 12, '00')

        self.line(190, 170, 190, 163)
        self.line(166, 163, 190, 163)

        conts = self.conts
        h = 7

        for cont in range(1, conts+1):
            x = 2
            metrica_sup = 168 - h*cont + x
            metrica_inf = 163 - h*cont

            self.line(21, metrica_sup, 59, metrica_sup)
            self.line(21,metrica_sup, 21, metrica_inf)
            self.string(23, metrica_inf+2, 16, f'Injetor {cont}')
            self.line(59,metrica_sup, 59, metrica_inf)
            self.line(21, metrica_inf, 59, metrica_inf)

            # Debito de Partida
            self.line(62, metrica_sup, 62, metrica_inf)
            self.line(86, metrica_sup, 86, metrica_inf)
            self.line(62, metrica_inf, 86, metrica_inf)

            # Marcha Lenta
            self.line(88, metrica_sup, 88, metrica_inf)
            self.line(112, metrica_sup, 112, metrica_inf)
            self.line(88, metrica_inf, 112, metrica_inf)

            # Carga Parcial
            self.line(114, metrica_sup, 114, metrica_inf)
            self.line(138, metrica_sup, 138, metrica_inf)
            self.line(114, metrica_inf, 138, metrica_inf)

            # Plena Carga
            self.line(140, metrica_sup, 140, metrica_inf)
            self.line(164, metrica_sup, 164, metrica_inf)
            self.line(140, metrica_inf, 164, metrica_inf)

            # Pré-Injeção
            self.line(166, metrica_sup, 166, metrica_inf)
            self.line(190, metrica_sup, 190, metrica_inf)
            self.line(166, metrica_inf, 190, metrica_inf)

            if not cont < 1:
                self.line(74, metrica_sup+7, 74, metrica_inf)
                self.line(100, metrica_sup+7, 100, metrica_inf)
                self.line(126, metrica_sup+7, 126, metrica_inf)
                self.line(152, metrica_sup+7, 152, metrica_inf)
                self.line(178, metrica_sup+7, 178, metrica_inf)
            
            self.resultado(cont)
    
        # observações
        self.box(10, 50, 190, 50)
        self.string(88, 94, 16, 'OBSERVAÇÕES')
        self.line(10, 92, 200, 92)

    def cliente(self):
        self.string(22, 250, 16, 'Nome:')
        self.string(22, 240, 16, 'Marca:')
        self.string(22, 230, 16, 'Modelo:')
        self.string(22, 220, 16, 'Placa:')
        self.string(22, 210, 16, f'Injetor: {self.injetor.codigo}')
        # self.string(22, 250, 16, f'Nome: {self.dados_cliente["-CLIENTE-"]}')
        # self.string(22, 240, 16, f'Marca: {self.dados_cliente["-VEICULO-"]}')
        # self.string(22, 230, 16, f'Modelo: {self.dados_cliente["-MODELO-"]}')
        # self.string(22, 220, 16, f'Placa: {self.dados_cliente["-PLACA-"]}')
        # self.string(22, 210, 16, f'Injetor: {self.testes[0]["-INJETOR-"][0].replace("_", " ")}')

    def verificar_teste(self, menor, maior, resultado):
        if resultado != '':
            if int(resultado) >= int(menor):
                if int(resultado) <= int(maior):
                    self.canvas.setFillColor('#00C72E')
                else:       
                    self.canvas.setFillColor('#DB2515')
            else:
                self.canvas.setFillColor('#DB2515') 
        return str(resultado)

    def resultado(self, cont):
        h = cont*7
        metrica = 164.7 - h


        self.string(63.7, metrica, 16, self.verificar_teste(self.injetor.pd_ddp_menor, self.injetor.pd_ddp_maior, self.testes[cont-1]["-DEBITO DDP-"]))
        self.string(75.7, metrica, 16, self.verificar_teste(0, self.injetor.pr_ddp, self.testes[cont-1]["-RETORNO DDP-"]))
        self.string(89.7, metrica, 16, self.verificar_teste(self.injetor.pd_ml_menor, self.injetor.pd_ml_maior, self.testes[cont-1]["-DEBITO ML-"]))
        self.string(101.7, metrica, 16, self.verificar_teste(0, self.injetor.pr_ml, self.testes[cont-1]["-RETORNO ML-"]))
        self.string(115.7, metrica, 16, self.verificar_teste(self.injetor.pd_cp_menor, self.injetor.pd_cp_maior, self.testes[cont-1]["-DEBITO CP-"]))
        self.string(127.7, metrica, 16, self.verificar_teste(0, self.injetor.pr_cp, self.testes[cont-1]["-RETORNO CP-"]))
        self.string(141.7, metrica, 16, self.verificar_teste(self.injetor.pd_pc_menor, self.injetor.pd_pc_maior, self.testes[cont-1]["-DEBITO PC-"]))
        self.string(153.7, metrica, 16, self.verificar_teste(0, self.injetor.pr_cp, self.testes[cont-1]["-RETORNO PC-"]))
        self.string(167.7, metrica, 16, self.verificar_teste(self.injetor.pd_pi_menor, self.injetor.pd_pi_maior, self.testes[cont-1]["-DEBITO PI-"]))
        self.string(179.7, metrica, 16, self.verificar_teste(0, self.injetor.pr_pi, self.testes[cont-1]["-RETORNO PI-"]))

        self.canvas.setFillColorRGB(0, 0, 0)

    def observacoes(self):
        obs = self.canvas.beginText(45, 240)
        texto = self.dados_cliente['-OBSERVACAO-']
        count = 0
        linha = []
        for letra in texto:
            if letra == ' ' and len(linha) == 0:
                continue
            else:
                linha.append(letra)
                count += 1
                if count == 52:
                    obs.textLine(''.join(linha))
                    linha = []
        if len(linha) != 0 and len(linha) < 52:
            obs.textLine(''.join(linha))

        # for i in range(len(texto)/52):
        #     obs.textLine(texto[i*52:i])
        #     if len(f'{line} {sobrou}') >= 52:
        #         line = line.split(' ')
        #         new_line = ' '.join(line[0:-1])
        #         obs.textLine(new_line)
        #         obs.textOut(line[-1])
        #         sobrou = line[-1]
        #     else:
        #         pass

        self.canvas.drawText(obs)
        # self.string(15, 85, 16, self.dados_cliente['-OBSERVACAO-'].replace('\n', '<br />\n'))
        
    def rodape(self):
        self.string(25, 40, 18, 'ALK ELETRODIESEL Agradece sua preferência!')
        self.string(50, 30, 15, 'Tudo posso naquele que me fortalece.')
        self.string(125, 25, 15, 'Filipenses 4:13')
        self.string(15, 15, 13, 'Contato: (27) 99734-3040')
        self.string(90, 15, 13, 'Contato: (27) 99902-5830')
        self.string(15, 10, 13, 'CPNJ: 41.301.666-67')
        self.string(15, 5, 13, 'Endereço: Rua 7 de Setembro, Vila Nova, Ibatiba - ES')

    def abrir(self):
        # os.system(self.save_name)
        subprocess.run([self.save_name], shell=True)

    def gerar(self):
        self.padrao()
        self.cliente()
        # self.observacoes()
        self.rodape()

        self.canvas.save()

        abrir = threading.Thread(target=self.abrir, daemon=True)
        abrir.start()

class Relatorio_Bomba():
    def __init__(self, valor_real, bomba, dados_cliente) -> None:
        self.valor_real = valor_real
        self.dados_cliente = dados_cliente
        pasta = os.path.join(os.path.expanduser('~'), 'Documents', 'laudos')
        if not os.path.exists(pasta):
            os.makedirs(pasta)
        self.save_name = os.path.join(os.path.expanduser('~'), 'Documents', 'laudos', f'{dados_cliente["-CLIENTE-"]}_{datetime.today().strftime("%d_%m_%Y_%H_%m_%S")}.pdf')
        self.canvas = canvas.Canvas(self.save_name, A4)
        # self.canvas: canvas.Canvas = canvas.Canvas(f'mypdf.pdf', A4)
        self.bomba = bomba

    def mm2p(self, milimetros):
        return milimetros / 0.352777

    def box(self, x, y, largura, altura):
        self.canvas.rect(self.mm2p(x), self.mm2p(y), self.mm2p(largura), self.mm2p(altura))

    def line(self, x1, y1, x2, y2):
        self.canvas.line(self.mm2p(x1), self.mm2p(y1), self.mm2p(x2), self.mm2p(y2))

    def string(self, x, y, fontsize, texto, font='Courier'):
        self.canvas.setFont(font, fontsize)
        self.canvas.drawString(self.mm2p(x), self.mm2p(y), texto)

    def image(self, imagem, x, y, largura, altura):
        self.canvas.drawImage(imagem, self.mm2p(x), self.mm2p(y), self.mm2p(largura), self.mm2p(altura))

    def verificar_teste(self, menor, maior, resultado):
        if resultado != '':
            if int(resultado) >= int(menor):
                if int(resultado) <= int(maior):
                    self.canvas.setFillColor('#00C72E')
                else:       
                    self.canvas.setFillColor('#DB2515')
            else:
                self.canvas.setFillColor('#DB2515') 
        return str(resultado)

    def padrao(self):

        # ALK ELETRODIESEL
        self.box(10, 190, 190, 97)
        self.line(10, 277, 200, 277)
        self.string(70, 279, 26, 'LAUDO TÉCNICO', 'Courier-Bold')

        # Cliente
        self.box(20, 200, 100, 67)
        self.line(20, 259, 120, 259)
        self.string(57, 261, 18, 'Cliente')
        self.line(21, 249, 119, 249)
        self.line(21, 239, 119, 239)
        self.line(21, 229, 119, 229)
        self.line(21, 219, 119, 219)
        self.line(21, 209, 119, 209)
        

        # Logo
        self.image(os.getenv('TEMP')+'\\alklogo.png', 133, 212, 55, 55)

        # Data
        self.string(132, 205, 17, f'Data: {datetime.strftime(datetime.today(), "%d/%m/%Y")}')
        self.string(132, 200, 17, f'Hora: {datetime.strftime(datetime.today(), "%H:%M:%S")}')

        # Resultado
        self.box(10, 100, 190, 90)
        self.string(88, 184, 18, 'Resultado')
        self.line(10, 182, 200, 182)

        self.string(20, 165, 16, f'Valor Ideal: {self.bomba.volume_ideal_menor} à {self.bomba.volume_ideal_maior}')
        self.string(20, 158, 16, f'Valor Real :')
        self.string(64, 158, 16, self.verificar_teste(self.bomba.volume_ideal_menor, self.bomba.volume_ideal_maior, self.valor_real))
        self.canvas.setFillColorRGB(0, 0, 0)

        # observações
        self.box(10, 50, 190, 50)
        self.string(88, 94, 16, 'OBSERVAÇÕES')
        self.line(10, 92, 200, 92)

    def cliente(self):
        self.string(22, 250, 16, f'Nome: {self.dados_cliente["-CLIENTE-"]}')
        self.string(22, 240, 16, f'Marca: {self.dados_cliente["-VEICULO-"]}')
        self.string(22, 230, 16, f'Modelo: {self.dados_cliente["-MODELO-"]}')
        self.string(22, 220, 16, f'Placa: {self.dados_cliente["-PLACA-"]}')
        self.string(22, 210, 16, f'Bomba: {self.bomba.codigo}')

    def observacoes(self):
        obs = self.canvas.beginText(45, 240)
        texto = self.dados_cliente['-OBSERVACAO-']
        count = 0
        linha = []
        for letra in texto:
            if letra == ' ' and len(linha) == 0:
                continue
            else:
                linha.append(letra)
                count += 1
                if count == 52:
                    obs.textLine(''.join(linha))
                    linha = []
        if len(linha) != 0 and len(linha) < 52:
            obs.textLine(''.join(linha))

        # for i in range(len(texto)/52):
        #     obs.textLine(texto[i*52:i])
        #     if len(f'{line} {sobrou}') >= 52:
        #         line = line.split(' ')
        #         new_line = ' '.join(line[0:-1])
        #         obs.textLine(new_line)
        #         obs.textOut(line[-1])
        #         sobrou = line[-1]
        #     else:
        #         pass

        self.canvas.drawText(obs)
        # self.string(15, 85, 16, self.dados_cliente['-OBSERVACAO-'].replace('\n', '<br />\n'))
        
    def rodape(self):
        self.string(25, 40, 18, 'ALK ELETRODIESEL Agradece sua preferência!')
        self.string(50, 30, 15, 'Tudo posso naquele que me fortalece.')
        self.string(125, 25, 15, 'Filipenses 4:13')
        self.string(15, 15, 13, 'Contato: (27) 99734-3040')
        self.string(90, 15, 13, 'Contato: (27) 99902-5830')
        self.string(15, 10, 13, 'CPNJ: 41.301.666-67')
        self.string(15, 5, 13, 'Endereço: Rua 7 de Setembro, Vila Nova, Ibatiba - ES')

    def abrir(self):
        # os.system(self.save_name)
        subprocess.run([self.save_name], shell=True)

    def gerar(self):
        self.padrao()
        self.cliente()
        self.observacoes()
        self.rodape()

        self.canvas.save()

        abrir = threading.Thread(target=self.abrir, daemon=True)
        abrir.start()
