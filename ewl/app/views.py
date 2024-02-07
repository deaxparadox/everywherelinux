from django.shortcuts import render

def error_404(request):
    return render(
        request,
        "404.html"
    )
    
def root(request):
    return render(
        request,
        "app/index.html"
    )