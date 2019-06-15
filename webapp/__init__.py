from flask import current_app
from flask import Flask, render_template
from webapp.weather import weather_by_city

def create_app(): 
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        page_title = 'Новости + погода'
        weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        return render_template('index.html', page_title=page_title, weather=weather)

    return app