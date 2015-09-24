from django.contrib import admin

from .models import Goal, Goalset, Date, Dateset, Activity

class GoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'complete')

class GoalsetAdmin(admin.ModelAdmin):
    list_display = ('id','goal_one','goal_two','goal_three','goal_four','goal_user','start_date','end_date')

class DateAdmin(admin.ModelAdmin):
    list_display = ('id', 'goal', 'week', 'day', 'goal_date', 'goal_user',)

class DatesetAdmin(admin.ModelAdmin):
    list_display = ('id','date_one','date_two','date_three','date_four','complete','goal_user',)

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'activity_day', 'description')
    readonly_fields=('date',)

admin.site.register(Goal, GoalAdmin)
admin.site.register(Goalset, GoalsetAdmin)
admin.site.register(Date, DateAdmin)
admin.site.register(Dateset, DatesetAdmin)
admin.site.register(Activity, ActivityAdmin)
