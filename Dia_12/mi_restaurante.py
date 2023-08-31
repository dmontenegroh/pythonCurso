from tkinter import *

# iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('1500x630+450+100')

# evitar maximizar
aplicacion.resizable(0, 0)

# titulo de la ventana
aplicacion.title("Mi Restaurante - Sistema de Facturacion")

# color de fondo de la ventana
aplicacion.config(bg='#eaf1fb')


# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(
    panel_superior, text='Sistema de Facturacion', fg='#041E49',
    font=('Dosis', 45), bg='#eaf1fb', width=27)
etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT, bg='#ffffff')
panel_izquierdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(aplicacion, bd=1, relief=FLAT, bg='#ffffff', padx=50)
panel_costos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='#041E49', bg='#ffffff')
panel_comidas.pack(side=LEFT)

# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='#041E49', bg='#ffffff')
panel_bebidas.pack(side=LEFT)
# panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='#041E49', bg='#ffffff')
panel_postres.pack(side=LEFT)

# panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(aplicacion, bd=1, relief=FLAT, bg='#eaf1fb')
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(aplicacion, bd=1, relief=FLAT, bg='#eaf1fb')
panel_recibo.pack()

# panel botones
panel_botones = Frame(aplicacion, bd=1, relief=FLAT, bg='#eaf1fb')
panel_botones.pack()

lista_comidas = ['pollo', 'cordero', 'salmon',
                 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola',
                 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'brownies',
                 'flan', 'mousse', 'tiramisu', 'pastel1', 'pastel2']

# generar items comida
variables_comida = []
cuadros_comida = []
textos_comida = []
contador = 0
for comida in lista_comidas:

    # crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0, bg='#ffffff', variable=variables_comida[contador])

    comida.grid(row=contador, column=0, sticky=W)

    # crear los cuadros de entrada
    cuadros_comida.append('')
    textos_comida.append('')
    textos_comida[contador] = StringVar()
    textos_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas, font=('Dosis', 19, 'bold'),
                                     bd=1, width=6, state=DISABLED, bg='#ffffff', textvariable=textos_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1)

    contador += 1


# generar items bebida
variables_bebida = []
cuadros_bebida = []
textos_bebida = []
contador = 0
for bebida in lista_bebidas:
    # crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=(
        'Dosis', 19, 'bold'), onvalue=1, offvalue=0, bg='#ffffff', variable=variables_bebida[contador])

    bebida.grid(row=contador, column=0, sticky=W)

    # crear los cuadros de entrada
    cuadros_bebida.append('')
    textos_bebida.append('')
    textos_bebida[contador] = StringVar()
    textos_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas, font=('Dosis', 19, 'bold'),
                                     bd=1, width=6, state=DISABLED, bg='#ffffff', textvariable=textos_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, column=1)
    contador += 1

# generar items postre
variables_postre = []
cuadros_postre = []
textos_postre = []
contador = 0
for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=(
        'Dosis', 19, 'bold'), onvalue=1, offvalue=0, bg='#ffffff', variable=variables_postre[contador])

    postre.grid(row=contador, column=0, sticky=W)

    # crear los cuadros de entrada
    cuadros_postre.append('')
    textos_postre.append('')
    textos_postre[contador] = StringVar()
    textos_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres, font=('Dosis', 19, 'bold'),
                                     bd=1, width=6, state=DISABLED, bg='#ffffff', textvariable=textos_postre[contador])
    cuadros_postre[contador].grid(row=contador, column=1)

    contador += 1

# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()


# etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_costo_postres = Label(panel_costos,
                               text='Costo Postres',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_costo_postres.grid(row=2, column=0)

texto_costo_postres = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_postre)
texto_costo_postres.grid(row=2, column=1, padx=41)

etiqueta_subtotal = Label(panel_costos,
                          text='Subtotal',
                          font=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

etiqueta_impuestos = Label(panel_costos,
                           text='Impuestos',
                           font=('Dosis', 12, 'bold'),
                           bg='azure4',
                           fg='white')
etiqueta_impuestos.grid(row=1, column=2)

texto_impuestos = Entry(panel_costos,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_impuesto)
texto_impuestos.grid(row=1, column=3, padx=41)

etiqueta_total = Label(panel_costos,
                       text='Total',
                       font=('Dosis', 12, 'bold'),
                       bg='azure4',
                       fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)


# evitar que la pantalla se cierre
aplicacion.mainloop()
