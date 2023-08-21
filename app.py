from flask import Flask, render_template, session,url_for,request,redirect

app=Flask(__name__)
app.secret_key="haa"

PLACEHOLDER="print('Hello, World!')"

@app.route('/',methods=['GET'])
def code():
    if session.get('code') is None:
        session['code']=PLACEHOLDER
    lines=session['code'].split('\n')
    context={"message":"Paste your python code",
             'code':session['code'],
             'num_lines':len(lines),
             'max_chars':len(max(lines,key=len))
             }
    return render_template("code_input.html",**context)

@app.route("/save_code",methods=['POST'])
def save_code():
    session['code']=request.form.get('code')
    return redirect(url_for('code'))

@app.route('/reset_session',methods=['POST'])
def reset_session():
    session.clear()
    session['code']=PLACEHOLDER
    return redirect(url_for('code'))