import matplotlib.pyplot as plt
import pandas as pd
import io
import base64

class Estadistica:

    def __init__(self):
        self.df = pd.read_excel('info/datos_stock.xlsx')
    
    def datosExcel(self):

        return self.df

    def graficoTotalFacturadodecompraventa(self):
        img = io.BytesIO()

        metodo = self.df['Compra/Venta'].unique()
        totalf = []
        for i in metodo:
            suma = self.df.loc[self.df['Compra/Venta'] == i, ['Total Facturado']].sum()[0]
            totalf.append(suma)

        plt.figure(figsize=(10,5))
        plt.bar(metodo, totalf, color='teal')
        plt.title('Total facturado de acuerdo a la compra y venta')
        plt.xticks(rotation=10)
        plt.ylabel('Total Facturado')
        plt.xlabel('Compra o Venta')
        plt.savefig(img, format='png')
        img.seek(0)

        img_url = base64.b64encode(img.getvalue()).decode()
        return img_url

    def graficoFrecuenciadelCliente(self):

        img = io.BytesIO()

        cliente = self.df['Cliente']
        plt.figure(figsize=(10,5))
        plt.hist(cliente, bins=None, color='gray')
        plt.title('Frecuencia de compras o ventas por el cliente')
        plt.xticks(rotation=10)
        plt.ylabel('Frecuencia')
        plt.xlabel('Cliente')

        plt.savefig(img, format='png')
        img.seek(0)

        img_url = base64.b64encode(img.getvalue()).decode()
        return img_url
        
    def graficodeprecioporproveedor(self):

        img = io.BytesIO()

        proveedor = self.df['Proveedor'].unique()
        precio = []
        for i in proveedor:
            suma = self.df.loc[self.df['Proveedor'] == i, ['Precio']].sum()[0]
            precio.append(suma)

        plt.figure(figsize=(10,5))
        plt.bar(proveedor, precio, color = 'brown')
        plt.title('frecuencia de precio de productos por proveedor')
        plt.xticks(rotation=10)
        plt.ylabel('Precio del producto')
        plt.xlabel('Proveedor')
        plt.savefig(img, format='png')
        img.seek(0)

        img_url = base64.b64encode(img.getvalue()).decode()
        return img_url

    def graficoFrecuenciadelproducto(self):

        img = io.BytesIO()

        x = self.df['Producto']
        plt.figure(figsize=(10,5))
        plt.hist(x, bins=None, color='green')
        plt.title('Frecuencia de los prductos comprados o vendidos')
        plt.xticks(rotation=10)
        plt.ylabel('Frecuencia')
        plt.xlabel('Producto')

        plt.savefig(img, format='png')
        img.seek(0)

        img_url = base64.b64encode(img.getvalue()).decode()
        return img_url
