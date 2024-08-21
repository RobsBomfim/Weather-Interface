import requests
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# Função para atualizar o tempo para uma cidade específica
def atualizar_tempo(event=None):
    api_key = 'bcba586e5ec1ace515e321e634e4c329'
    cidade = entrada_cidade.get()
    link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br'

    try:
        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()

        weather_description = requisicao_dic['weather'][0]['description']
        temperatura = requisicao_dic['main']['temp'] - 273.15

        # Atualizar os labels na interface com os resultados
        label_tempo.config(text=f'Tempo: {weather_description}')
        label_temperatura.config(text=f'Temperatura: {temperatura:.1f}°C')

    except Exception as e:
        print(f'Erro ao obter dados do clima: {e}')
        label_tempo.config(text='Erro ao obter dados do clima')
        label_temperatura.config(text='')

# Configuração da interface gráfica
janela = Tk()
janela.title('Weather Interface')
janela.resizable(width=False, height=False)
janela.config(bg='#263238')  # DarkBlue
janela.geometry("500x350")

# Separador
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)

# Frame para entrada de cidade e botão
frame1 = Frame(janela, width=500, height=50, bg='#4db6ac', relief="flat")
frame1.grid(row=1, column=0)

label_cidade = Label(frame1, text="Digite o nome da cidade:", bg='#4db6ac', fg='white')
label_cidade.grid(row=0, column=0, padx=10, pady=5)

entrada_cidade = Entry(frame1, width=30)
entrada_cidade.grid(row=0, column=1, padx=10, pady=5)

# Vincular pressionamento de Enter à função atualizar_tempo
entrada_cidade.bind('<Return>', atualizar_tempo)

botao_atualizar = Button(frame1, text="Atualizar Tempo", command=atualizar_tempo)
botao_atualizar.grid(row=0, column=2, padx=10, pady=5)

# Frame para exibir resultados
frame2 = Frame(janela, width=340, height=300, bg='#263238', relief="flat")
frame2.grid(row=2, column=0, sticky=NW)

label_tempo = Label(frame2, text="", bg='#263238', fg='white')
label_tempo.grid(row=0, column=0, padx=10, pady=5, sticky=W)

label_temperatura = Label(frame2, text="", bg='#263238', fg='white')
label_temperatura.grid(row=1, column=0, padx=10, pady=5, sticky=W)

janela.mainloop()