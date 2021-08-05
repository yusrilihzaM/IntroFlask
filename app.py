from flask import Flask, render_template, request, make_response
app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    # return "<p>Hello, World!</p>"
    search=request.args.get('search')
    return render_template('index.html', search=search)

@app.route("/setting")
def show_setting():
    return "<p>halaman settings</p>"

@app.route("/profile/<username>")
def show_profile(username):
    return render_template('profile.html',username=username)

@app.route("/blog/<int:blog_id>")
def show_blog(blog_id):
    return "blog id %d" %blog_id  

@app.route("/login",methods=['GET','POST'])
def show_login():
    if request.method=='POST':
        resp=make_response("Email Kamu "+ request.form['email'])
        resp.set_cookie('email_user',request.form['email'])
        return resp
    return render_template('login.html')

@app.route("/getcookie")
def getCookie():
    email=request.cookies.get('email_user')
    return "email yang disimpan di cookie adalah "+email