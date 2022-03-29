from email.headerregistry import Address
import itertools
from tkinter import *
from tkinter import font
import pip._vendor.requests
from setuptools import Command 
import requests
import webbrowser
from time import sleep


root = Tk()    


class Application():
    def __init__(self) -> None:
        self.trajeto = []
        self.ceps_buscados = 0
        self.root = root
        self.link_mapa = 'https://www.google.com.br/maps/dir'
        self.add_endereco = '{},{}+{}/'
        self.tela()
        self.frames_de_tela()
        self.widgets_frame1()
        self.dados_frame2()
        root.mainloop()
    def tela(self):
        self.root.title("Constulta CEP")
        self.root.configure(background='#1e3743')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width= 900, height=1000)
        self.root.minsize(width= 500, height=400)
    def frames_de_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth=0.96, relheight=0.20)
        self.frame_2 = Frame(self.root, bd = 4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx= 0.02, rely=0.23, relwidth=0.96, relheight=0.40)
        self.frame_3 = Frame(self.root, bd = 4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_3.place(relx= 0.02, rely=0.64, relwidth=0.96, relheight=0.30)
        
    def widgets_frame1(self):
        ### Criação do botão de buscar
        self.bt_buscar = Button(self.frame_1,  text="Buscar", bd=2, bg='#107db2', fg='white', 
                            font=('verdana', 10, 'bold'), command=self.busca_cep)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.55)
        ### Criação da label e entrada do CEP
        self.lb_cep = Label(self.frame_1, text="CEP", bg='#dfe3ee', fg='#107db2', font=(10))
        self.lb_cep.place(relx=0.05, rely=0.05)
        self.cep_entry = Entry(self.frame_1, font=(10))
        self.cep_entry.place(relx=0.05, rely=0.3, relwidth= 0.20, relheight=0.35)
        self.lb_erro = Label(self.frame_1, text="", bg='#dfe3ee', fg='#107db2')
        self.lb_erro.place(relx=0.05, rely=0.70)
    def dados_frame2(self):
        ### Mostra os dados do CEP buscado
        self.lb_cep = Label(self.frame_2, text="CEP:", bg='#dfe3ee', fg='#107db2', font=(10))
        self.lb_cep.place(relx=0.01, rely=0.05)
        self.lb_logradouro = Label(self.frame_2, text="LOGRADOURO:", bg='#dfe3ee', fg='#107db2', font=(10))
        self.lb_logradouro.place(relx=0.01, rely=0.2)
        self.lb_complemento = Label(self.frame_2, text="COMPLEMENTO:", bg='#dfe3ee', fg='#107db2', font=(10))
        self.lb_complemento.place(relx=0.01, rely=0.35)
        self.lb_bairro = Label(self.frame_2, text="BAIRRO:", bg='#dfe3ee', fg='#107db2', font=(10))
        self.lb_bairro.place(relx=0.01, rely=0.50)
        self.lb_cidade = Label(self.frame_2, text="CIDADE:", bg='#dfe3ee', fg='#107db2', font=(10))
        self.lb_cidade.place(relx=0.01, rely=0.65)
        self.lb_estado = Label(self.frame_2, text="ESTADO:", bg='#dfe3ee', fg='#107db2', font=(10))
        self.lb_estado.place(relx=0.01, rely=0.80)
        
        ### Criação do botão de ver no mapa
        self.bt_ver_mapa = Button(self.frame_2,  text="Ver no Mapa", bd=2, bg='#107db2', fg='white', 
                            font=('verdana', 10, 'bold'), command=self.ver_mapa)
        self.bt_ver_mapa.place(relx=0.7, rely=0.1, relwidth=0.3, relheight=0.38)
        
    def busca_cep(self):
        self.ceps_buscados = self.ceps_buscados + 1
        self.cepbuscado = self.cep_entry.get()
        if len(self.cepbuscado) != 8:
            self.lb_erro.config(text='QUANTIDADE DE DIGITOS NÃO É VÁLIDA')
            self.cep_entry.delete(0, END)
        
        else:
            self.request = requests.get('https://viacep.com.br/ws/{}/json'.format(self.cepbuscado))
            self.address = self.request.json()
           
            if 'erro' not in self.address:
                self.mostra_cep = Label(self.frame_2, text=self.address['cep'], bg='#dfe3ee', fg='#107db2', font=10)
                self.mostra_cep.place(relx=0.25, rely=0.05)
                self.mostra_logradouro = Label(self.frame_2, text=self.address['logradouro'], bg='#dfe3ee', fg='#107db2', font=10)
                self.mostra_logradouro.place(relx=0.25, rely=0.2)
                self.mostra_complemento = Label(self.frame_2, text=self.address['complemento'], bg='#dfe3ee', fg='#107db2', font=10)
                self.mostra_complemento.place(relx=0.25, rely=0.35)
                self.mostra_bairro = Label(self.frame_2, text=self.address['bairro'], bg='#dfe3ee', fg='#107db2', font=10)
                self.mostra_bairro.place(relx=0.25, rely=0.50)
                self.mostra_cidade = Label(self.frame_2, text=self.address['localidade'], bg='#dfe3ee', fg='#107db2', font=10)
                self.mostra_cidade.place(relx=0.25, rely=0.65)
                self.mostra_estado = Label(self.frame_2, text=self.address['uf'], bg='#dfe3ee', fg='#107db2', font=10)
                self.mostra_estado.place(relx=0.25, rely=0.80)
      
                self.cep = self.address['cep']
                self.logradouro = self.address['logradouro']
                self.cidade = self.address['localidade']
                self.estado = self.address['uf']
                self.cep_entry.delete(0, END)
                self.lb_erro.config(text='')
                self.trajeto.append(self.address)
                
                self.ceps_buscados = self.ceps_buscados + 1
                
                #self.link_mapa = self.link_mapa + "" + self.add_endereco
                #print(self.link_mapa)
                
            else:
                self.lb_erro.config(text='CEP INVÁLIDO')
                self.cep_entry.delete(0, END)
    def ver_mapa(self):
        if len(self.trajeto) == 1:
            webbrowser.open(
                f"https://www.google.com.br/maps/place/{self.logradouro},+{self.cidade}+{self.estado},+{self.cep}"
            )
        else:
            trajetos = [
                    (
                        f"{self.trajeto[i].get('logradouro')},",
                        f"{self.trajeto[i].get('localidade')}+",
                        f"{self.trajeto[i].get('uf')}/",
                    )
                for i in range(len(self.trajeto))
            ]
            
            url_trajetos = "".join(list(itertools.chain(*trajetos)))
            webbrowser.open(f"{self.link_mapa}/{url_trajetos}")
       
       
        
              
    

Application()







    




