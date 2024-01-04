from django.shortcuts import render, HttpResponse
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.
def index(request, id:str):
    
    with open(BASE_DIR / "static/index.html") as f:
        r = f.read()
        return render(request,"index.html", {"string": r})