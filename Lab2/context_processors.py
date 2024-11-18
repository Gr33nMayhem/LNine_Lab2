from django.utils import translation

from Lab2 import settings
from accounts.models import UserProfile


def user_profile_and_language(request):
    context = {}

    # if settings.LANGUAGE_SESSION_KEY exists in the session, activate the language
    if settings.LANGUAGE_SESSION_KEY in request.session:
        translation.activate(request.session[settings.LANGUAGE_SESSION_KEY])

    if request.user.is_authenticated:
        # Add user profiles and language to context
        context['user_profiles'] = UserProfile.objects.filter(user=request.user)
        context['user_language'] = request.user.language
    return context
