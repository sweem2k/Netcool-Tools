from flask import Blueprint, render_template
import json
from Website import nc_unprocess


views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    
    #pulls all unproccesed alerts
    alerts_dict = nc_unprocess.nc_unproc()   

    return render_template("base.html", data = alerts_dict)    
