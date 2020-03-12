from django.shortcuts import render

def index(request):
  context = {
    'judul':'Home',
    'nav': [
      #['/','Home'],
      ['/theiz','Theis' ],
      ['/janzen','Janzen' ],
      ['/charl','Charl' ],    
    ]
  }

  return render(request,'home.html',context)