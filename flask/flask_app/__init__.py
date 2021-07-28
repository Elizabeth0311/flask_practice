from flask import Flask , render_template


app = Flask(__name__)



@app.route('/') # ㄱㅣ본주소 + / 
def index():
    # apple = 'apple'  #jinja
    return render_template('index.html') #알아서 html 파일 찾아줌

@app.route('/main')
def main():
    return render_template('main_body.html')

if __name__ == '__main__' :
    app.run(debug=True)
