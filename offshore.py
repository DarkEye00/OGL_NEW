from flask import Flask, render_template, request
#from flask_frozen import Freezer


app = Flask(__name__)

#freezer = Freezer(app)
app.secret_key = '0ff$hor3 k3y'

@app.route('/')
def index():
    
    return render_template("index.html")

@app.route('/Environment-management/')
def EnvPolicy():
    return render_template("EnvPolicy.html")

@app.route('/Labour-management-policy/')
def LabourMgt():
    return render_template("Labormgt.html")

@app.route('/Waste-management-plan/')
def WasteMgt():
    return render_template("WasteMgt.html")

@app.route('/About_Us/')
def About_Us():
    return render_template("About.html")

@app.route('/Speak_Up/')
def Speak():
    return render_template("speak.html")
 
@app.route('/Sustainability/')
def Sustainability():
    return render_template("sustainability.html")

@app.route('/Careers/')
def Careers():
    return render_template("career.html")

@app.route('/Code_of_Conduct/')
def Conduct():
    return render_template("conduct.html")

@app.route('/Services/')
def Services():
    return render_template("Services.html")

@app.route('/Corruption-policy/')
def Corruption():
    return render_template("corruption.html")

@app.route('/Find-us/')
def Offices():
    return render_template("contact.html")

@app.route('/our-culture/')
def culture():
    return render_template("culture.html")

@app.route('/join-us/')
def jobs():
    return render_template("Application.html")

@app.route('/Diversity-&-Inclusion/')
def diversity():
    return render_template("diversity.html")

@app.route('/Training/')
def training():
    return render_template("training.html")

@app.route('/Quote/')
def quote():
    return render_template("quote.html")



if __name__ == ("__main__"):
   app.run(debug=True)