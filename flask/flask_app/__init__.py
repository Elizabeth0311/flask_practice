from flask import Flask
from flask_app.routes.main_route import bp as main_bp

app = Flask(__name__)
app.register_blueprint(main_bp)


@app.route('/', methods=['POST']) # ㄱㅣ본주소 + / 
def index():      #안에 실행할 자료 넣어주고 리턴값으로 변수 지정해줘도 가능 
    # dict_a = {  }
    return {'hello' : 'Flask'}, 200 #문자열, 튜플, 딕셔너리 형태 가능 #http status 응답코드 전달
    # return dict_a
 
#라우팅 디폴트값
@app.route('/user/', defaults={'user_id':0}) # 엔드포인트 설정 안하고싶을때, /user/여기부분에 값이 없을때 지정
#라우팅 추가 
@app.route('/user/<user_id>') # 라우팅 엔드포인트 설정해줘야됨 
def user_index(user_id):
    return f"Here is your user id : {user_id}"


if __name__ == '__main__' :
    app.run(debug=True)
