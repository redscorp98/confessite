from django.shortcuts import render
from Database import database
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'text': 'confess 1',
        'date': 'august',
    },
    {
        'text': 'confess 2',
        'date': 'sept',
    },
]


def home(request):

    return render(request, 'submit/home.html',)


def about(request):
    return render(request, 'submit/about.html')


def submissions(request):
    context = {
            'posts': posts
        }
    # context argument only takes a dictionary
    return render(request, 'submit/submissions.html', context=database.all_confessions())


def submit(request):
    if request.POST.get('submit-form-box') == '':
        return HttpResponse('<h1> Incomplete submission </h1>')
    else:
        print('Input ID:', request.POST.get('name'))
        database.add_confession(request.POST.get('submit-form-box'))
        return HttpResponse('<h1> Complete submission </h1>')
