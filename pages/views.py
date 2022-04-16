from pipes import Template
from re import template
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"
# Create your views here.
class AboutPageView(TemplateView):
    template_name = "about.html"
