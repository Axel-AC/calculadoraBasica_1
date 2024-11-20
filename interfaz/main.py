import clr
import tkinter as tk
# path = r'C:\Users\cony\Desktop\c#\calculadoraBasica_1\calculadoraBasica_1\bin\Debug\calculadoraBasica_1.dll'
path2 = r'..\calculadoraBasica_1\bin\Debug\calculadoraBasica_1'

clr.AddReference(path2)


from calculadoraBasica_1 import Calculadora


calc = Calculadora()

# Tk = tk()

window = tk.Tk()
window.title("calculadora")
window.geometry('250x250')

label_num1 = tk.Label(window, text="Número 1:")
label_num1.grid(row=0, column=0)

entry_num1 = tk.Entry(window)
entry_num1.grid(row=0, column=1)



label_num2 = tk.Label(window, text="Número 2:")
label_num2.grid(row=1, column=0)

entry_num2 = tk.Entry(window)
entry_num2.grid(row=1, column=1)

label_op = tk.Label(window, text="Operacion")
label_op.grid(row=2,column=0)

entry_op = tk.Entry(window)
entry_op.grid(row=2, column=1)

def Resultado():
    try:
        num1 = float(entry_num1.get())  
        num2 = float(entry_num2.get()) 
        op = entry_op.get()

        r = calc.Operar(num1,num2,op)
        entry_resultado.config(text=f'el resultado es {r}')
    except ValueError:
        entry_resultado.config(text=f'introduce valores validos')


button = tk.Button(window, text='Resolver', command=Resultado)
button.grid(row=3, column=1)

entry_resultado = tk.Label(window,text='', font=("Arial", 14))
entry_resultado.grid(row=5,column=1)


window.mainloop()