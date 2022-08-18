## Compre-weather-forecast 
### 기상 예보를 모아서 보여주는 크롤링 프로그램

-----
❓ Problem : 이상기후로 기상청의 날씨 예보 정확도가 떨어지고 있다.
👉 Idea : 한국 기상청 뿐만 아니라 세계 여러 기상예보를 참고하자
😒 Another Problem : 근데 일일이 웹서핑 하는거 귀찮다.
⭐ Solution : 이걸 한번에 자동으로 모아서 그래프로 보여주는 자동화 프로그램은 없을까?

 

![](https://velog.velcdn.com/images/tjdwns2243/post/b5c7c476-e570-41a6-bc3d-d40f00defc29/image.png)
한국 주요도시 19군데의 정보만 제공한다.
![](https://velog.velcdn.com/images/tjdwns2243/post/77223fa2-e28b-4b6c-bfee-c9afc8fc4430/image.png)
기상예보 정확도가 높은 편으로 알려진 [Accuweather](https://www.accuweather.com/ko/kr/south-korea-weather)(미국), [BBC Weather](https://www.bbc.com/weather/1835848)(영국), [The Weatehr Channel](https://weather.com/ko-KR/weather/today/l/KSXX0037:1:KS?Goto=Redirected)(미국), [기상청](https://www.weather.go.kr/w/index.do)(한국)의 기상예보를 매일 오후 11시마다 schedule 라이브러리를 통해 자동으로 크롤링을 실행을 한다.

 크롤링은 Selenium을 통해 실행하며 해당 정보들을 하나로 모아 그래프로 표현하는 것은 단순히 matplotlib로 하였다. 코드의 구체적인 동작 방식을 다이어그램으로 표현하면 다음과 같다.

![](https://velog.velcdn.com/images/tjdwns2243/post/a89d01dc-ca9b-4b69-b140-b42d7de47f2c/image.png)

😊 소감 : 
해당 프로젝트를 통해서 단순하게나마나 백엔드의 동작 원리에 대해 대략적으로 알 수 있었고, 파이썬과 웹 크롤러에 좀 더 익숙해 질 수 있는 기회였다. 
이 토이 프로젝트를 통해 어떠한 방향으로 백엔드 공부를 해야 할지 방향성을 잡을 수 있었다. 