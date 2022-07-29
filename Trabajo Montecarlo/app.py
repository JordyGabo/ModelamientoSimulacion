from flask import Flask,render_template

app = Flask(__name__)

#================================================================
#========================> ENUNCIADO <===========================
@app.route("/montecarlo")
def principal():
    #-------------------------------------12
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    datos = pd.DataFrame() 
    ventas = [40, 41, 42, 43, 44, 45]
    semanas = [4, 10, 12, 9, 8, 7]
    datos["Ventas_Cajas_Leche"] = ventas
    datos["Numero_Semanas"] = semanas
    datos
    n1 = datos.to_html(classes="table table-hover table-striped", justify="justify-all")


    return render_template('index.html', n1=n1)


#================================================================
#========================> RESULTADO <===========================
@app.route("/montecarlo-resultado")
def secundario():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    datos = pd.DataFrame() 
    ventas = [40, 41, 42, 43, 44, 45]
    semanas = [4, 10, 12, 9, 8, 7]
    datos["Ventas_Cajas_Leche"] = ventas
    datos["Numero_Semanas"] = semanas
    datos

    #-------------------------------------13
    suma = datos["Numero_Semanas"].sum()
    x1 = datos["Numero_Semanas"] / suma
    datos["Probabilidad"] = x1
    datos
    n2 = datos.to_html(classes="table table-hover table-striped", justify="justify-all")


    #-------------------------------------14
    x2 = np.cumsum(datos["Probabilidad"])
    datos["FPA"] = x2
    datos
    n3 = datos.to_html(classes="table table-hover table-striped", justify="justify-all")


    #-------------------------------------15
    datos["min"] = datos["FPA"]
    datos["max"] = datos["FPA"]
    listaMin = datos["min"].values
    listaMax = datos["max"].values
    listaMin[0] = 0
    for i in range (1,6):
        listaMin[i] = listaMax[i-1]
    datos['min'] = listaMin
    datos
    n4 = datos.to_html(classes="table table-hover table-striped", justify="justify-all")


    #-------------------------------------16
    NumAleatorios = pd.DataFrame()
    NumAleatorios["ri"] = [0.11, 0.44, 0.90, 0.52, 0.00, 0.54, 0.56, 0.66, 0.52, 0.46,
                        0.24, 0.31, 0.49, 0.03, 0.50, 0.65, 0.80, 0.74, 0.32, 0.66]
    NumAleatorios
    n5 = NumAleatorios.to_html(classes="table table-hover table-striped", justify="justify-all")

    
    #-------------------------------------17
    min = datos['min'].values
    max = datos['max'].values
    dato1 = []
    dato2 = []
    Simulacion = pd.DataFrame()
    for j in range (len(NumAleatorios)):
        for i in range (len(datos)):
            if (NumAleatorios["ri"][j]>=datos["min"][i] and NumAleatorios["ri"][j]<datos["max"][i]):
                dato1.append(datos["Ventas_Cajas_Leche"][i])
                dato2.append(datos["Numero_Semanas"][i])
    Simulacion["ri"] = NumAleatorios["ri"]
    Simulacion["Numero_Semanas"] = dato2
    Simulacion["Ventas_Cajas_Leche"] = dato1
    Simulacion
    n6 = Simulacion.to_html(classes="table table-hover table-striped", justify="justify-all")

    #-------------------------------------18
    Falta = []
    Sobra = []

    for index, row in Simulacion.iterrows():
        Falta.append(42-row["Ventas_Cajas_Leche"])
        Sobra.append(row["Ventas_Cajas_Leche"]-42)
    Simulacion["Faltante"] = Falta
    Simulacion["Sobrante"] = Sobra
    Simulacion
    n7 = Simulacion.to_html(classes="table table-hover table-striped", justify="justify-all")


    #-------------------------------------19
    PromedioFaltante = Simulacion["Faltante"].mean()
    PromedioSobrante = Simulacion["Sobrante"].mean()
    print("Promedio Faltante =", PromedioFaltante)
    print("Promedio Sobrante =", PromedioSobrante)
    
    #-------------------------------------20
    from matplotlib import pyplot as plt
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    import io
    import base64

    buf = io.BytesIO()
    plt.plot(datos)
    fig = plt.gcf()

    canvas = FigureCanvasAgg(fig)
    canvas.print_png(buf)
    fig.clear()
    plot_url = base64.b64encode(buf.getvalue()).decode('UTF-8')
    
    return render_template('resultado.html', n2=n2, n3=n3, n4=n4, n5=n5, n6=n6, n7=n7)



if __name__ == '__main__':
    app.run(port=5000,debug=True)