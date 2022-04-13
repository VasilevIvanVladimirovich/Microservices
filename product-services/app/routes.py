from calendar import c
from unicodedata import name
from requests import request
from . import Product, app
from . import api
from . import db
import json
from flask import Flask, jsonify, redirect
from flask_restful import Api, Resource, reqparse
from collections import OrderedDict

parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("count", type=int)
parser.add_argument("price", type=int)


class Main(Resource):
    def get(self):
        products = Product.query.all()
        product_list = []
        product_tmp = {}
        for product in products:
            product_tmp = {'name':product.name,'count':product.count,'price':product.price}
            product_list.append(product_tmp)
            product_tmp = {}
        return jsonify(product_list)

    def post(self):
        newname = parser.parse_args()["name"]
        newcount= parser.parse_args()["count"]
        newprice = parser.parse_args()["price"]
        userModel = Product(name = newname,count = newcount,price = newprice)
        try:
            db.session.add(userModel)
            db.session.commit()
            return True
        except:
            return "Ошибка"
    
    def delete(self):
        delname = parser.parse_args()["name"]
        x = db.session.query(Product).filter(Product.name==delname).one()
        try:
            db.session.delete(x)
            db.session.commit()
            return True
        except:
            return "Ошибка"

    


api.add_resource(Main, "/api/product")
api.init_app(app)
