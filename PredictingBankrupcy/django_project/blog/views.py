from django.shortcuts import render
from django.http import HttpResponse


posts = [
	{
		'author': 'mtbost',
		'title': 'Project Blog 1',
		'content': 'This is the home page!',
		'date_posted': 'October 15, 2020'
	},
	
	{
		'author': 'mtbost',
		'title': 'Project Blog 2',
		'content': 'Second post content',
		'date_posted': 'October 15, 2020'
	}


]

# Create your views here.
def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title':'About'})

