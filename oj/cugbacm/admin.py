from django.contrib import admin
from .models import User
from .models import Problem
from .models import Submit

# Register your models here.
admin.site.register(User)
admin.site.register(Problem)
admin.site.register(Submit)
