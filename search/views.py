# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.management import call_command

@login_required(login_url='/accounts/login/')
def search_index(request):
    call_command('search-index', '_all')
    return HttpResponse("Index process done.")