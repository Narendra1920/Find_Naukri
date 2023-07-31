from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    peoples=[
    {"name":"ROhan","age":13},
     {"name":"ritik","age":12},
      {"name":"sapna","age":15},
       {"name":"sita","age":14}
    ]
    for i in peoples:
        print(i)

    return render(request,"index.html", context={'peoples':peoples})
def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")

# Create your views here.
