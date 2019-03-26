from django.shortcuts import render
from funds.forms import task2_fundsForm
from funds.models import task2_funds
# Create your views here.
def showtask2(request):
    return render(request,'funds_master.html')
#from pymongo import MongoClient

def task2list(request):
    select_funds=request.POST.get("t")

    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017')
    db = client
    posts = db.fund
    x1 = {"select_funds": select_funds}
    posts.fund.insert(x1)
    return render(request, "funds_master.html", {"msg": "details saved"})