from django.shortcuts import render

from django.views.generic import TemplateView
from django.http import HttpResponse

from .djforms import RegForm

# Create your views here.

"""
    one dispatcher user's requests
"""
def raw_index(in_request):
    """
        Get parameters from url: site/?name=user&a=30&...
    """
    name = in_request.GET.get('name', 'Guest')
    # print(f"get name {name}")
    
    """
        define variables for html
    """
    def_title = "Ucomm"
    def_welcome = f"Welcome to real world  {name}"
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


    """
        return data as html from templates(settings) ->'DIRS': [BASE_DIR/'templates'],
    """
    return render(request=in_request, template_name="index.html", context=def_context)


def get_post_request(request):
    ## first enter to page
    if request.method == "GET":                          
        def_context = {
            "hist": "zero",
            "title": "Get & Post"
        } 
    elif request.method == 'POST':
        mess = request.POST.get("data", '')
        ## return HttpResponse(f"Get from user data: {mess}") ## simple output

        '''
            get data by html form's <name> 
        '''
        username = request.POST.get("username")
        password = request.POST.get("user_password")
        repassword = request.POST.get("user_repassword")
        age = request.POST.get("user_age")
        premium = request.POST.get("premium") == 'on'

        print(f"get_post_request(): {username} {password}-{repassword} {age} premium: {premium}")
        
        def_context = {
            "hist": mess,
            "title": "Get & Post"
        }

    return render(request, "post.html", context=def_context)


def ext_post(request):

    print(f"\next_post(): ...")
    if request.method == 'POST':
        form = RegForm(request.POST)
       
        print(f"\next_post(): POST {form.is_valid()} ")
    
        print(f'\next_post(): {form.cleaned_data}')
        if form.is_valid(): ## is_valid also makes cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            password = request.POST.get("user_password")
            repassword = request.POST.get("user_password")
            age = request.POST.get("user_age")

            message = form.cleaned_data['message']
            box = form.cleaned_data['box']

            print(f"ext_post(): POST: {name} {email} {password} {repassword} {age} {message} {box}")
    else:
        form = RegForm()  ## form is a html-template that django try to find in html page by name
        ## print(f"\next_post(): render {form}")
    
    return render(request, 'post.html', context={'form': form} )


def req_index(in_request):
    name = in_request.GET.get('name', 'Guest')
    return HttpResponse(f"Hello {name}", status=400, reason="some develop issue...")


def ext_index(in_request):
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
    return render(in_request, template_name="ext_index.html", context=def_context)

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

    def get_name(self, request):
        return request.GET.get('name', 'Guest')

    def_context = {
        "title": def_title,
        "welcome": def_welcome,
        "events_list": def_event_list,
        "len_list": len_list
    }

    extra_context = def_context

