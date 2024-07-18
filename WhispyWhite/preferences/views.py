from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import Preferences
from django.views.decorators.http import require_POST
import json

@require_POST
def toggle_theme(request):
    data = json.loads(request.body)
    theme = data.get('theme')
    if request.user.is_authenticated:
        preferences, created = Preferences.objects.get_or_create(user=request.user)
        preferences.theme = theme
        preferences.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'User not authenticated'}, status=403)


# Create your views here.
