from django.shortcuts import render

# Create your views here.
def static_dir(request):
    return render(request, 'static_dir.html')