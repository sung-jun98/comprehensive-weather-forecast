from flask import Flask, request, render_template, make_response, session
from class_list import crawling_and_graph
from flask_cors import CORS
import os

# weather = crawling_and_graph.Weather_test(land_name)
 #   weather.bbc_weather()
  #  weather.accu_weather()
   # weather.kma_weather()
    #weather.twc_weather()


#app = Flask(__name__, static_url_path='/static')
app = Flask(__name__)
CORS(app)
@app.route('/')
def hello():
    return render_template('start_page.html')

@app.route('/select')
def select():
    land_name = request.form['land_name']
    
    show_me_a_graph = crawling_and_graph.Making_graph(land_name) 
    show_me_a_graph.select_from_DB()
    
    return render_template('start_page.html', image_file = show_me_a_graph.chart)
    
    
if __name__ == "__main__":
    app.run(host = "0.0.0.0")
    