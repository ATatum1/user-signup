from flask import Flask, request, redirect, render_template
import cgi
import os

#template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True



#@app.route("/")
#def index():
#    return form


@app.route("/")
def index():
#    #template = jinja_env.get_template("user-form.html")
    return render_template("user-form.html")
   
     

@app.route("/", methods=["post"])
def validate_user():
    user_name = request.form["user_name"]
    pass_word = request.form["pass_word"]
    ver_psw = request.form["ver_psw"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verpsw_error = ""
    email_error = ""

    if user_name == "":
        username_error="Username is Required!"
        user_name=user_name
        
    count = 0
    for a in user_name:
        if (a.isspace()) == True:
            count+=1       


    if len(user_name) < 3 or len(user_name) > 20 or count > 0:
        username_error="Invalid Username! Username must be between 3 and 20 characters."
        user_name=user_name
        
        
       
    if "pass_word" == "":
        password_error="Password is Required!"
        pass_word = ""
 
    count = 0
    for a in pass_word:
        if (a.isspace()) == True:
            count+=1   

    if len(pass_word) < 3 or len(pass_word)>20 or count > 0:
        password_error="Invalid Password! Password must be between 3 and 20 characters and cannot contain a space."
        pass_word = ""

       

    if  ver_psw =="":
        verpsw_error="Please verify your password!"
        pass_word = ""
        ver_psw = ""

    
    if pass_word != ver_psw:
        verpsw_error="Passwords do not match. Pleae re-verfiy your password."
        pass_word = ""
        ver_psw = ""

    #if ver_psw != pass_word:
    #    verpsw_error="Passwords do not match. Pleae re-verfiy your password."
    #    pass_word = ""
    #    ver_psw = ""   
    
       
    
    if email == "":
        email = email 

    count = 0
    for a in email:
        if (a.isspace()) == True:
            count+=1

    
    if email != "":
        if "@" not in email or "." not in email or count > 0:
            email_error="Not a valid email address."
            email=email

    if not username_error and not password_error and not verpsw_error and not email_error:
      
        return render_template("user-greeting.html",user_name=user_name)
    
    return render_template("user-form.html",username_error=username_error,password_error=password_error,verpsw_error=verpsw_error,email_error=email_error,user_name=user_name,pass_word="",ver_psw ="",email=email)
        

#@app.route("/")
#def display_user_form():
#    return render_template("user-form.html",user_name="",username_error ="", pass_word="", password_error="", ver_psw="", verpws_error="", email="", email_error="")
#    #return render_template("user-form.html", )
    
app.run()


















##def hello():
 #   user_name = request.form["user_name"]
  #  template = jinja_env.get_template('user-greeting.html')
   # return "<h1>Welcome, " + user_name + "</h1>"


#template code startes here 
#template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

#@app.route("/")
#def index():
#    template = jinja_env.get_template('user-form.html')
#    return template.render()