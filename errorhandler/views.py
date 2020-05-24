from django.shortcuts import render

# Create your views here.
def handler404(request, exception):
    return render(request, 'errorhandler/404.html', status=404)


def handler500(request):
    return render(request, 'errorhandler/500.html', status=500)


def handler403(request, exception):
    return render(request, 'errorhandler/403.html', status=403)


def handler400(request, exception):
    return render(request, 'errorhandler/400.html', status=400)
