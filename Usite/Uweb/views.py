from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

"""
    one dispatcher user's requests
"""
def index(request):
    """
        return data as html from templates(settings) ->'DIRS': [BASE_DIR/'templates'],
    """
    return render(request, "index.html")


"""
    OOP way
"""
class Index(TemplateView):
    template_name = "index.html"

