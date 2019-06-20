from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'emaillist/index.htm')

def form(reqeust):
    return render(reqeust, 'emaillist/form.html')