from .models import Preferences

def user_preferences(request):
    if request.user.is_authenticated:
        preferences = Preferences.objects.filter(user=request.user).first()
    else:
        preferences = None

    return {
        'user_pref': preferences,
    }
