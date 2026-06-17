from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "nombre": "Actividad Compute Engine",
        "estudiante": "Nicolle Perez",
        "docker": True,
        "cloud": True
    })
