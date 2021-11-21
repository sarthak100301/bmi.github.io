from flask import Flask,flash,render_template,request
app = Flask(__name__)

@app.route('/')
def b_m_i():
      
    return render_template('index.html')
@app.route('/', methods=['POST'])
def get_values():
    w = int(request.form['weight'])
    h = float(request.form['height'])
    
    bmi1 = w/(h*h)
    bmi = '%.2f'% round(bmi1,2)
    return render_template('index2.html', bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)