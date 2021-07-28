from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/main')
# user 블루프린트의 이름 플라스크가 인지하는
# __name__ import이름 
# 해당 블루프린트의 이름 /는 꼭 붙여줘야함 

@bp.route('/') # 127.0.0.1:5000 + '/main' + '/' => 127.0.0.1:5000/main/
def index():
    return 'Welcome'