from flask import Flask
#Flask 객체 갖게 됨
#Flask는 생성자 를 1개 받는 데 그게 __name__
#__name__은 파일명을 의미
app = Flask(__name__)

#뷰함수 : 뷰 함수는 데이터베이스에서 검색된 항목들을 dict 타입으로 show_entries.html template 에 렌더링하여 리턴한다.
@app.route("/")

#함수종료시 요청한 쪽으로 응답되는 string값 
def helloworld():
	return "Hello world"

#app.run호출시 웹서버 동작. 어떤 ip에서 요청이 들어와도 응답을 할 거라는 의미
if __name__ == "__main__":
	app.run(host="0.0.0.0")
