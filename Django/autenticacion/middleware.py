from django.shortcuts import redirect
from django.urls import reverse


class LoginRequiredMiddleware:
    ALLOWED_URLS =[
        reverse('login'),
        reverse('register'),
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:

            if request.path not in self.ALLOWED_URLS:
                return redirect('login')
        response = self.get_response(request)
        return response