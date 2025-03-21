from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import logout

class CustomErrorMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code == 404:
            return render(request, "404.html", status=404)
        elif response.status_code == 500:
            return render(request, "500.html", status=500)
        return response



