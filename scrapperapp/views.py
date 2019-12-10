from django.shortcuts import render
from django.http import HttpResponse
import requests
import bs4 
# Create your views here.
#part1
#  def home(request):
#     # return HttpResponse('hello world! from home')
#     names=['amisha','sgn','krijan']
#     d={
#         'name' : names,
#         'college' :'katford'
#     }

def home(request):
    page = requests.get('https://fabpedigree.com/james/mathmen.htm')
    soup = bs4.BeautifulSoup(page.content,'html.parser')
    
    li=soup.find_all('li')
    names=[]
    for each in li:
        names.append(each.find('a').string)
        
        d={
            'names' : names
        }
    return render(request,'home.html',d)

def bootcamp(request):
    return HttpResponse('hello from bootcamp')
