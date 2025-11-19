import tkinter as tk 

#interface para desktop
# capturando um texto do input e mostrando na label embaixo do botão


def display():
    texto  = input_.get()
    texto_3.config(text=texto)



# criando a janela 
janela  = tk.Tk()
janela.geometry('768x480')
janela.configure(bg='black')



# inserindo um texto
texto = tk.Label(janela, text = ' Isso é um teste ', font=('arial',16), fg ='black', bg='pink')
texto.pack()


# inserindo um texto
texto_2 = tk.Label(janela, text = ' Isso é um teste ', font=('arial',16) )
texto_2.pack()


# inserido um input 
input_ = tk.Entry(janela, font=('arial',16))
input_.pack()


# criando um botão
btn  =  tk.Button(janela, text= 'clique aqui', font=('arial',16), command=display)
btn.pack()



texto_3 = tk.Label(janela, text = 'aqui vai aparecer um texto', font=('arial',16) )
texto_3.pack()


# loop da janela
janela.mainloop()