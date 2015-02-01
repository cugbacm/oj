from django.contrib import admin
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit, UserContestMap,ContestXls, OJAttribute
# Register your models here.
admin.site.register(User)
admin.site.register(Submit)
admin.site.register(Problem)
admin.site.register(Contest)
admin.site.register(ContestSubmit)
admin.site.register(UserContestMap)
admin.site.register(ContestXls)
admin.site.register(OJAttribute)

