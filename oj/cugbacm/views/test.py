#!/usr/bin/env python
from django.shortcuts import render
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from django.http import HttpResponse, HttpResponseRedirect

def test(request):
    return render(request, 'cugbacm/test.html', {})

