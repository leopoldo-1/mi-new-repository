#!/usr/bin/env python3
#-*- coding: utf8 -*-
"Sample hello world Flask app"

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "<h1>Hello World!</h1>"

@app.route("/products")
def products():
  product_list = ["Apples", "Oranges", "Bannans"]

  bullet_list = "".join("<li>%s</li>" % product for product in product_list)
  return "<ul>%s</ul>" % bullet_list