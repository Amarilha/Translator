from tkinter import *
from tkinter import ttk, messagebox  # Importa módulos para criar a interface gráfica
from googletrans import Translator    # Importa o tradutor do Google
import googletrans                     # Importa a lista de idiomas disponíveis no Google Translate

# Configuração principal da janela
root = Tk()
root.title("Google Translator")       # Define o título da janela
root.geometry("1080x400")             # Define o tamanho da janela
root.resizable(False, False)          # Impede que a janela seja redimensionada
root.configure(background="white")    # Define a cor de fundo como branco

# Função para atualizar os rótulos dos idiomas escolhidos
def label_change():
    c = combo1.get()                  # Obtém o idioma selecionado no primeiro combobox
    c1 = combo2.get()                 # Obtém o idioma selecionado no segundo combobox
    label1.configure(text=c)          # Atualiza o texto do primeiro rótulo
    label2.configure(text=c1)         # Atualiza o texto do segundo rótulo
    root.after(1000, label_change)    # Executa esta função a cada 1 segundo

# Função para realizar a tradução
def translate_now():
    text_ = text1.get(1.0, END)       # Obtém o texto da área de entrada
    t1 = Translator()                 # Cria uma instância do tradutor
    trans_text = t1.translate(text_, src=combo2.get())  # Tradução com o idioma de origem definido pelo segundo combobox
    trans_text = trans_text.text      # Extrai o texto traduzido
    
    text2.delete(1.0, END)            # Limpa a área de texto de saída
    text2.insert(END, trans_text)     # Insere o texto traduzido na área de saída

# Ícone da janela
image_icon = PhotoImage(file="image/languages.png")  # Carrega a imagem do ícone
root.iconphoto(False, image_icon)                    # Define o ícone da janela

# Imagem de seta (representando troca de idiomas)
arrow_image = PhotoImage(file="image/exchange.png")  # Carrega a imagem da seta
image_label = Label(root, image=arrow_image, width=150)  # Cria um rótulo para exibir a imagem
image_label.place(x=460, y=50)                      # Posiciona a imagem na janela

# Lista de idiomas suportados
language = googletrans.LANGUAGES                    # Dicionário de idiomas suportados
languageV = list(language.values())                 # Converte os valores (nomes dos idiomas) para uma lista
lang1 = language.keys()                             # Obtém as chaves (códigos dos idiomas)

# Primeiro combobox (seleção do idioma de origem)
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")  # Cria o combobox
combo1.place(x=110, y=20)                                                 # Posiciona o combobox
combo1.set("ENGLISH")                                                     # Define o idioma padrão

# Rótulo para o primeiro idioma
label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

# Segundo combobox (seleção do idioma de destino)
combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")  # Define o texto padrão

# Rótulo para o segundo idioma
label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=750, y=50)

# Primeiro frame (área de entrada)
f = Frame(root, bg="Black", bd=5)       # Cria um frame com borda preta
f.place(x=10, y=118, width=440, height=210)  # Posiciona e dimensiona o frame

text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)  # Área de texto para entrada
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)              # Adiciona uma barra de rolagem
scrollbar1.pack(side="right", fill="y")  # Posiciona a barra de rolagem à direita
scrollbar1.configure(command=text1.yview)  # Sincroniza a barra de rolagem com a área de texto
text1.configure(yscrollcommand=scrollbar1.set)

# Segundo frame (área de saída)
f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)  # Área de texto para saída
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Botão de tradução
translate = Button(root, text="Translate", font=("Roboto", 15), activebackground="white", cursor="hand2", bd=1, 
                   width=10, height=2, bg="black", fg="white", command=translate_now)
translate.place(x=476, y=250)  # Posiciona o botão na janela

# Inicia o loop principal da interface
root.mainloop()
