from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Rohit"
    letters = list(name)
    pup_dic = {'puppy':'jose'}
    return render_template('basic.html',name = name,letters=letters,pup_dic=pup_dic)
    

if __name__ == '__main__':
    app.run(debug=True)

