from django.shortcuts import render

def index(request):
  context = {
    'judul':'Theis',
    'nav': [
      ['/','Home'],
      ['/theiz','Theis' ],
      ['/janzen','Janzen' ],
      ['/charl','Charl' ],    
    ]
  }

  return render(request,'theiz/home.html',context)


def profile(request):
  return render(request,'theiz/profile.html')

def blog(request):
  return render(request,'theiz/blog.html')

def team(request):
  return render(request,'theiz/team.html')

def contact(request):
  return render(request,'theiz/contact.html')

