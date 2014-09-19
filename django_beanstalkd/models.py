from django.db import models

STATUS_TYPE = (
    ('ready', 'Ready'),
    ('running', 'Running'),
    ('error', 'Error'),
    ('done', 'Done'),
)


class Job(models.Model):
    name = models.CharField(max_length=100, help_text='app.jobname')
    parameter = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True,
                                   help_text='Human description')
    next_run_time = models.DateTimeField(null=True, blank=True)
    last_run_time = models.DateTimeField(null=True, blank=True)
    last_run_status = models.CharField(max_length=100, null=True, blank=True)
    last_success_run = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        if self.description:
            s = '%s (%s)' % (self.description, self.name)
        else:
            s = "%s" % (self.name)
        return s


class JobRun(models.Model):
    job = models.ForeignKey(Job, related_name="runs", null=True, blank=True)
    name = models.CharField(max_length=100, help_text='app.jobname')
    parameter = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True,
                                   help_text='Human description')
    jid = models.IntegerField(null=True, blank=True,
                              help_text='Beanstalkd job id')
    pid = models.IntegerField(null=True, blank=True,
                              help_text='System process id')
    success = models.NullBooleanField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_TYPE,
                              null=True, blank=True)
    time_started = models.DateTimeField(null=True, blank=True)
    time_finished = models.DateTimeField(null=True, blank=True)
    stdout = models.TextField(null=True, blank=True)
    stderr = models.TextField(null=True, blank=True)
    exception = models.TextField(null=True, blank=True)

    def __unicode__(self):
        if self.description:
            s = '%s (%s)' % (self.description, self.name)
        else:
            s = "%s" % (self.name)
        return s
