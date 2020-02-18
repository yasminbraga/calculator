from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate',methods=['GET','POST'])
def calculate():
    if request.method == 'POST':
        expression = request.form.get('expression')
        
        try:
            result = eval('{}'.format(expression))
        except Exception as error:
            result = error
        
        return render_template('index.html', result = result)
    return render_template('index.html')





app.run(debug=True)