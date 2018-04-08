from django.shortcuts import render

# Create your views here.

from .models import *

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class HostIndex(LoginRequiredMixin, ListView):
    template_name = 'hostmanage/index.html'

    context_object_name = 'host_list'

    model = Host

    def get_context_data(self, **kwargs):
        context = super(HostIndex, self).get_context_data(**kwargs)
        context['title_name'] = 'host page'
        return context

