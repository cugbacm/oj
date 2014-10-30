#!/usr/bin/env python
from django.shortcuts import render

def test(request):
  return render(request, 'cugbacm/login.html', {})
