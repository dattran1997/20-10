from flask import Flask, render_template, request, redirect, url_for, session
from models.collection import User, Present
import mlab
import random

app = Flask(__name__)

mlab.connect()
app.secret_key = 'secret_key'

defname = "abc"
defpass = "123"

list_response =["đùa đấy đăng nhập lại đi bạn ơi!","đăng nhập sai nữa xóa acc giờ","đăng nhập đúng đi cú lừa đấy :))","đăng nhập vớ va vớ vẩn gõ phím cho nó cẩn thận vào",
"Tài Khoản của bạn đã bị xóa =))(đùa đấy!)","sai tài khoản mật khẩu rồi bạn gì ơi"]

def alow_to_login(user_found):
    session["logged_in"] = True
    session["username"] = str(user_found.username)
    session["user_id"] = str(user_found.id)
    print(session["username"])
    print(session["user_id"])

def validate_login(acccountname, password):
    try:
        user_found = User.objects.get(acccountname = acccountname, password = password)
    except:
        user_found = None
    # user_found = User.objects.get(username = username, password = password)
    if user_found is not None:
        return user_found
    else:
        return None


@app.route('/',methods=['GET','POST'])
def index():
    response = random.choice(list_response)

    if request.method == "GET":
        return render_template('index.html', response = "đăng nhập sai đi :v")
    elif request.method == "POST":
        form = request.form
        acccountname = form['acccountname']
        password = form['password']
        user_validated = validate_login(acccountname = acccountname, password = password)

        if (user_validated is not None):
            user_found = user_validated
            alow_to_login(user_found = user_found)
            return redirect(url_for("present",user_id = session['user_id']))
        else:
            return render_template('index.html', response = response)


@app.route('/present/<user_id>')
def present(user_id):
    if(session['logged_in'] == True) and (session["user_id"] == user_id):
        presents = Present.objects(reciverid = user_id)
        user = User.objects.get(id = user_id)
        user_image = user.image
        username = user.username
        return render_template('present.html', user_image = user_image, username = username, presents = presents)
    else:
        return "relogin to continue"


@app.route('/logout')
def logout():
    session["logged_in"] = False
    session["username"] = None
    session["user_id"] = None
    return "logout successful"


if __name__ == '__main__':
  app.run(debug=False)
