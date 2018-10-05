from django.shortcuts import render
post1 = ''

posts = [
    {
        'author': 'Don',
        'title': 'Introvert Challenges',
        'content': """If you're anything like me, it can be difficult finding the motivation to get out of your comfort zone, especially for social interactions. 
        If you register for this site we will send you hourly social challenges that will give you ideas on how to make that leap and have some fun! We hope you have a great time with these 
        Introvert Challenges :)""",
        'date_posted': 'September 1st'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})