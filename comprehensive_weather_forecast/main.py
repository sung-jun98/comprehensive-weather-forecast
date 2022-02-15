from flask import Flask, request, render_template, make_response, session
from class_list import crawling_and_graph
from flask_cors import CORS
import schedule
import os
dict_of_landname = {'서울': 'Seoul', '부산': 'Busan', '대구': 'Daegu', '대전' : 'Daejeon', '광주' : 'Gwangju', '수원': 'Suwon', '울산': 'Ulsan', '청주': 'Cheongju-si', '제주' : 'Jeju-si', '춘천':'Chuncheon', '속초': "Sokcho", '김포국제공항' : 'Gimpo International Airport', '포항' : 'Pohand', '김해':'Gimhae' , '진주': 'Jinju', '목포' : 'Moppo', '군산' : 'Kunsan' , '원주' : 'Wonju', '강릉' : 'Kang-neung' }

def crawling_everyday():
    for i in dict_of_landname.keys():
        weather = crawling_and_graph.Weather_test(i)
        weather.bbc_weather()
        weather.accu_weather()
        weather.kma_weather()
        weather.twc_weather()
        print(i + '지역 크롤링 완료')
        
schedule.every().day.at("23:00").do(crawling_everyday)
#△5줄 : 파이썬의 schedule 라이브러리를 사용하여 매일 오후 11시에 크롤링 클래스가 실행하도록 설정.


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
    