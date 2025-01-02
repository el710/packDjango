from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

"""
    one dispatcher user's requests
"""
def index(in_request):
    """
        define variables for html
    """
    def_title = "Ucomm"
    def_welcome = "Welcome to real world"

    def_context = {
        "title": def_title,
        "welcome": def_welcome
    }

    """
        return data as html from templates(settings) ->'DIRS': [BASE_DIR/'templates'],
    """
    return render(request=in_request, template_name="index.html", context=def_context)


"""
    OOP way
"""
class Index(TemplateView):
    template_name = "index.html"

