from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("<marquee><h1><b>Đe si, svijete!</b></h1></marquee>")
