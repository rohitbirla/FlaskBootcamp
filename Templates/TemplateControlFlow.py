from flask import Flask,render_template

app  = Flask(__name__)

@app.route('/')
def index():
    # mylist = [1,2,3,4,5]
    # puppies = ['fluppy','rusky','spike']
    user_logged_in = True
    return render_template('basic.html',user_logged_in=user_logged_in)


if __name__ == '__main__':
    app.run(debug=True)
