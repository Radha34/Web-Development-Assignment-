from flask import Flask,request
from flask_restful import Resource, Api, abort
import datetime

app = Flask(__name__)
api = Api(app)

orders = {}

class OrdersAPI(Resource):
    def get(self,order_id=None):
        if order_id is None:
            return orders
        if order_id not in orders:
            abort(404,message="Order_Id {} doesn't exist".format(order_id))   
        return(order_id)

    def post(self,order_id):
        if order_id not in orders:
            order = {}
            
            order['dish_name'] = request.form['dish_name']
            order['price'] = request.form['price']
            order['quantity'] = request.form['quantity']
            ordered_at = datetime.datetime.now()
            order['ordered_at'] = ordered_at.strftime('%d-%m-%Y %H:%M:%S')
            orders[order_id] = order
            return orders[order_id]
        abort(404, message="Order_Id {} already exists".format(order_id))         

    def put(self,order_id):
        if order_id in orders:
            order = {}
            
            order['dish_name'] = request.form['dish_name']
            order['quantity'] = request.form['quantity']
            
            orders[order_id].update(order)
            return orders[order_id]
        abort(404, message="Order_Id {} doesn't exist".format(order_id))    

    def delete(self,order_id):
        if order_id in orders:
            response_string = 'Your order with order_id {} is deleted'.format(order_id)
            del orders[order_id]
            return response_string
        abort(404,message="Order doesn't exist")        

api.add_resource(OrdersAPI,
              '/Orders/',
              '/Orders/<int:order_id>')

if __name__ == '__main__':
    app.run(debug = True)        
