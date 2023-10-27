from flask import Flask, render_template, request, url_for, redirect



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'   

    
    from .views import views

    # Register your blueprints
    app.register_blueprint(views, url_prefix='/')
    

    return app