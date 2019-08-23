from django.shortcuts import render,redirect
from movies.models import Movie
from .forms import PostForm

def list(request):
    movie = Movie.objects.all().order_by('year')
    movie1 = movie[0]
    movie2 = movie[1]
    if request.method == 'POST':
        query= request.POST.get('word')
        alls = Movie.objects.filter(MName__icontains=query).order_by('year')
    else:
        alls = Movie.objects.all().order_by('year')
    return render(request, 'list.html',{'movie1':movie1,'movie2':movie2,'movie':alls})

def home(request):
    return redirect('list')


def watch(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'watch.html', {'movie':movie})