from django.shortcuts import render
import pandas as pd
from home.database import Database

# Create your views here.
def index(request):
    db = Database()
    predval=str(round(db.Get_prediction_graph("tcs"),2))

    context={
        'name' :"Tata Consultancy Services Ltd.",
        'info' :"Tata Consultancy Services is the flagship company and a part of Tata group. It is an IT services, consulting and business solutions organization that has been partnering with many of the world's largest businesses in their transformation journeys for over 50 years. TCS offers a consulting-led, cognitive powered, integrated portfolio of business, technology and engineering services and solutions. ",
        'mkcap' :"₹ 1,131,151 Cr.",
        'pe' :"35.2",
        'shprice':'₹3,057.95',
        'prediction': predval
    }
    return render(request,"index.html",context)