import tkinter as tk 



# criando a janela 
janela  = tk.Tk()
janela.geometry('768x480')



# inserindo um texto
texto = tk.Label(janela, text = ' Isso é um teste ', font=('arial',16) )
texto.pack()


# inserindo um texto
texto_2 = tk.Label(janela, text = ' Isso é um teste ', font=('arial',16) )
texto_2.pack()


# inserido um input 
input_ = tk.Entry(janela, font=('arial',16))
input_.pack()



# criando um botão
btn  =  tk.Button(janela, text= 'clique aqui', font=('arial',16))
btn.pack()


# loop da janela
janela.mainloop()


