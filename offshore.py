from flask import Flask, render_template, request
#from services.routes import services_blueprint
from flask_frozen import Freezer


app = Flask(__name__)

#app.register_blueprint(services_blueprint, url_prefix='/Services')

freezer = Freezer(app)
app.secret_key = '0ff$hor3 k3y'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
@app.route('/')
def index():
    
    return render_template("index.html")

@app.route('/Environment-management/')
def EnvPolicy():
    return render_template("EnvPolicy.html")

@app.route('/Labour-management-policy/')
def LabourMgt():
    return render_template("Labormgt.html")


@app.route('/About_Us/')
def About_Us():
    return render_template("About.html")
 
@app.route('/Sustainability/')
def Sustainability():
    return render_template("sustainability.html")

@app.route('/Careers/')
def Careers():
    return render_template("career.html")

@app.route('/Code_of_Conduct/')
def Conduct():
    return render_template("conduct.html")

@app.route('/Corruption-policy/')
def Corruption():
    return render_template("corruption.html")

@app.route('/Find-us/')
def Offices():
    return render_template("contact.html")

@app.route('/Careers/join-us/')
def jobs():
    return render_template("Application.html")


@app.route('/Careers/')
def careers():
    return render_template("career.html")

@app.route('/People-&-Culture/')
def PC():
    return render_template("People.html")
@app.route('/Services/Sea-Freight/')
def sea_freight():
    return render_template ("Services/sea.html")

@app.route('/Services/Air-Freight/')
def air_freight():
    return render_template ("Services/air.html")

@app.route('/Services/Warehousing-&-Fulfillment/')
def FC():
    return render_template ("Services/fulfillment.html")

@app.route('/Services/Road-Freight/')
def road_freight():
    return render_template ("Services/road.html")
@app.route('/Services/Project-Cargo/')
def project_cargo():
    return render_template ("Services/project.html")
@app.route('/Services/Customs/')
def customs():
    return render_template ("Services/Customs.html")

@app.route('/FAQs/')
def faqs():
    return render_template ("faq.html")

@app.route('/Kebs-Banned-Products/')
def kebs():
    return render_template ("faq.html")

if __name__ == ("__main__"):
  app.run(debug=True) 