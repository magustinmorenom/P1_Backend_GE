from django.shortcuts import render

# Create your views here.
# myapi/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

@csrf_exempt
def get_scans(request):
    if request.method == 'POST':
        if 'image' in request.FILES:
            image = request.FILES['image']
            file_name = default_storage.save("scans/" + image.name, image)
            return JsonResponse({'message': 'Image uploaded successfully', 'file_name': file_name})
        else:
            return JsonResponse({'error': 'Parece que no anda. No image provided'}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)