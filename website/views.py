from flask import Blueprint, Flask, render_template, redirect, url_for, request

views = Blueprint('views', __name__)


@views.route('/')
def home():     
        return render_template('index.html')

@views.route('/Iphones')
def Iphones():     
        return render_template('Iphone.html')

@views.route('/Iphone-repair')
def repair():     
        return render_template('repair.html')

@views.route('/accessories')
def accessories():     
        return render_template('accessories.html')



   