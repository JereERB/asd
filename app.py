from distutils.log import debug
from itertools import product
from flask import Flask, jsonify
import flask

#Objeto que inicializa mi servidor
app = Flask(__name__)

from productos import products


#
@app.route('/ping')
def ping():
    return jsonify({
        "message": "Ping 20ms"
    })

@app.route('/products')
def getProducts():
    return jsonify({"Productos":products , "message": "Product's List"}) 

@app.route('/products/<string:product_name>')
def getproduct(product_name):#singular
    #Recorre nuestra lista de productos

    productsFound = [product for product in products if product['name']==product_name]
    if(len(productsFound) >0):         
        return  jsonify({"Prducto" : productsFound[0]})#Hace que solo me imprima el producto
    else:
        return jsonify({"Message" : "Product not found"})

#Correr el servidor
if __name__ == '__main__':
    app.run(debug=True,port=4000)


'''
mylist = [1,4,7,8,20]

newlist = [x for x in mylist if x%2 == 0]
print(newlist)

'''