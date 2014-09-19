from django.contrib import admin

from models import Job, JobRun


class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_run_time', 'last_run_status',
                    'next_run_time')

admin.site.register(Job, JobAdmin)


class JobRunAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'success', 'status', 'time_started',
                    'time_finished',)
    list_display_links = ('name', 'status',)
    list_filter = ('success', 'status',)
    search_fields = ('name',)

admin.site.register(JobRun, JobRunAdmin)
