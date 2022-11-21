from flask import Flask,render_template,redirect,session,request
app = Flask(__name__)
app.secret_key = "Keep it safe"
# ---------------------------------------------------------------
@app.route('/')
def index():
        count=0
        session['count']=count
        session['addVisit']=session['count']
        return render_template("index.html")
# -------------------------------------------------
@app.route('/countVisit', methods=['post'])
def countVisit():
    session['addVisit'] = request.form['addVisit']
    session['addVisit'] = int(session['count'])+2
    return redirect('/show')

@app.route('/show')
def show_result():
    session['count'] +=2
    return render_template("index.html")

# -------------------------------------------------

@app.route('/resetVisit', methods=['post'])
def resetVisit():
    session['count'] = str(0)
    session['addVisit'] = request.form['reset']
    session['addVisit'] = int(session['count'])+1
    return redirect('/revisit')

@app.route('/revisit')
def revisit_result():
    return render_template("index.html")




# ---------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
