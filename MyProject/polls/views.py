from  django.http import  HttpResponse

def HelloWorldView(request):
    return HttpResponse("Hello world")