from django.contrib import admin
from .models import QuestionChoice, Question, ExtraUserInfo, UserType, UserTypeAllocation, Course, Topic, UserTest, UserTestQuestion

# Register your models here.
admin.site.register(Question)
class QuestionChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice', 'correct', 'image', 'question')

admin.site.register(QuestionChoice, QuestionChoiceAdmin)
admin.site.register(ExtraUserInfo)

class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'type_description')
admin.site.register(UserType, UserTypeAdmin)

class UserTypeAllocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type')
admin.site.register(UserTypeAllocation, UserTypeAllocationAdmin)

admin.site.register(Course)
admin.site.register(Topic)

admin.site.register(UserTest)
admin.site.register(UserTestQuestion)
