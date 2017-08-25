# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic

# Create your views here.
def my_view(request):
    # View code here...
    return render(request, 'blog/index.html', {
        'foo': 'bar',
    },)# content_type='application/xhtml')