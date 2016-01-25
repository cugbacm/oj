from django.contrib import admin
from .models import Contest
from .models import ContestUser
from .models import ContestProblem
from .models import ContestSubmit

# Register your models here.
admin.site.register(Contest)
admin.site.register(ContestUser)
admin.site.register(ContestProblem)
admin.site.register(ContestSubmit)
