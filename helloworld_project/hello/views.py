from django.shortcuts import render
from django.http import JsonResponse

def hello_world_json(request):
    if request.GET.get('format') == 'html':
        return render(request, 'hello/hello.html')  # Ensure the path is correct
    return JsonResponse({"Message": "Hello World!"})
