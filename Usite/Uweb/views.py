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

def ext_index(in_requist):
    def_title = "Ucomm"
    def_welcome = "Welcome to real world"
    def_event_list = ["05:00   wake up",
                      "05:30   breakfast",
                      "06:00   start learning",
                      "09:00   start develop Ucomm",
                      "16:00   start Yandex-taxi",
                      "22:00   go home",
                      "23:00   go to bed"
                    ]
    len_list = len(def_event_list)

    def_context = {
        "title": def_title,
        "welcome": def_welcome,
        "events_list": def_event_list,
        "len_list": len_list
    }
    return render(in_requist, template_name="ext_index.html", context=def_context)

"""
    OOP way
"""
class Index(TemplateView):
    template_name = "index.html"

    def_title = "Ucomm"
    def_welcome = "Welcome to real world"
    def_event_list = ["05:00   wake up",
                      "05:30   breakfast",
                      "06:00   start learning",
                      "09:00   start develop Ucomm",
                      "16:00   start Yandex-taxi",
                      "22:00   go home",
                      "23:00   go to bed"
                    ]
    len_list = len(def_event_list)

    def_context = {
        "title": def_title,
        "welcome": def_welcome,
        "events_list": def_event_list,
        "len_list": len_list
    }

    extra_context = def_context

