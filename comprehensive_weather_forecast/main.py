from flask import Flask, request, render_template, make_response, session
from class_list import crawling_and_graph
from flask_cors import CORS
import os

#weather = crawling_and_graph.Weather_test('서울')
#weather.bbc_weather()
#weather.accu_weather()
#weather.kma_weather()
#weather.twc_weather()
#△5줄 : 파이썬의 schedule 라이브러리를 사용하여 일정시간에 실행되도록 수정할 것(하루에 한번씩)

#app = Flask(__name__, static_url_path='/static')
app = Flask(__name__)
CORS(app)
@app.route('/') #맨 처음 접속했을 때의 시작페이지 리턴
def hello():
    return render_template('start_page.html') 

@app.route('/select', methods=['POST']) #사용자가 지명을 입력하고 난뒤 연결될 라우팅 경로
def select():
    land_name = request.form['land_name']
    
    show_me_a_graph = crawling_and_graph.Making_graph(land_name) 
    show_me_a_graph.select_from_DB()
    
    return render_template('start_page.html', graph_file = 'chart.png')
    
    
if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0")
    