from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from .forms import movie_form
from django.views.generic import ListView
# Create your views here.
def index(request):
    movies=movie.objects.all()
    context={'movie_list':movies}
    return render(request,'index.html',context)
def detial(request,list_id):
    movie1=movie.objects.get(id=list_id)
    return render(request,'detials.html',{'movie':movie1})

def post1(request):
    if request.method=='POST':
        movie_name=request.POST.get('name')
        movie_year = request.POST.get('year')
        movie_disc = request.POST.get('discr')
        movie_img = request.FILES.get('img')
        upload_movie=movie(name=movie_name,year=movie_year,disc=movie_disc,image=movie_img)
        upload_movie.save()
        return redirect('/')
    return render(request,'post.html')
def update1(request,form_id):
   movi=movie.objects.get(id=form_id)
   formdit=movie_form(request.POST or None,request.FILES,instance=movi)
   if formdit.is_valid():
       formdit.save()
       return redirect('/')
   return render(request,'edit.html',{'for1':formdit,'movie':movi})

def delete(request,id):
    if request.method=='POST':
         movies=movie.objects.get(id=id)
         movies.delete()
         return redirect('/')
    return render(request,'delete.html')

class sample_list(ListView):
    model = movie
    template_name = 'sample.html'
    context_object_name = 'key'