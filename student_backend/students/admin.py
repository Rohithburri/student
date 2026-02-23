from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(AcademicInformation)
admin.site.register(CourseInterest)
admin.site.register(FuturePlan)
admin.site.register(AdditionalInformation)
