from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest):
    return HttpResponse("<marquee><h1><b>Đe si, svijete!</b></h1></marquee>")
