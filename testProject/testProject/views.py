from django.http import HttpResponse
def test(request):
    return HttpResponse("Hello tested pass")