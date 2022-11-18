from flask import Flask, render_template, request
import logging
from logging import Formatter, FileHandler
from forms import *
import os


app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')

