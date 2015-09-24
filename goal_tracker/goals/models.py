from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
    """
    in-progress state: active == True AND complete == False
    complete cannot be True unless active already is
    """
    user = models.ForeignKey(User, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    complete = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        unique_together = ('user','name') # user cannot have multiple goals with the same name

class Goalset(models.Model):
    goal_one = models.ForeignKey(Goal, related_name='goal_one')
    goal_two = models.ForeignKey(Goal, related_name='goal_two')
    goal_three = models.ForeignKey(Goal, related_name='goal_three')
    goal_four = models.ForeignKey(Goal, related_name='goal_four')
    active_date = models.DateTimeField('date started', auto_now_add=True, editable=False)
    complete_date = models.DateTimeField('date completed', null=True, blank=True, editable=False)

    """
    set active_date and complete_date values
    when the goalset is created
    """

    def __str__(self):
        return 'Goal Set %s' % self.id

    def goal_user(self):
        return u"%s" % (self.goal_one.user)

    def start_date(self):
        return u"%s" % (self.active_date.strftime('%h %d, %Y'))

    def end_date(self):
        return u"%s" % (self.complete_date)
        # return u"%s" % (self.complete_date.strftime('%h %d, %Y'))

    class Meta:
        ordering = ["active_date"]
        unique_together = ("goal_one","goal_two","goal_three","goal_four",)

class Date(models.Model):
    goal = models.ForeignKey(Goal)
    week = models.IntegerField()
    day = models.IntegerField()
    activity_date = models.DateTimeField(null=False, blank=False, editable=False)

    def __str__(self):
        return self.goal.name

    def goal_date(self):
        return u"%s" % (self.activity_date.strftime('%h %d, %Y'))

    def goal_user(self):
        return u"%s" % (self.goal.user)

    class Meta:
        ordering = ["goal"]
        unique_together = ("goal","week","day",)

class Dateset(models.Model):
    date_one = models.ForeignKey(Date, related_name='date_one')
    date_two = models.ForeignKey(Date, related_name='date_two')
    date_three = models.ForeignKey(Date, related_name='date_three')
    date_four = models.ForeignKey(Date, related_name='date_four')
    complete = models.BooleanField(default=False, editable=True)

    def __str__(self):
        return self.date_one.activity_date

    def goal_user(self):
        return u"%s" % (self.date_one.goal.user)

    class Meta:
        unique_together = ("date_one","date_two","date_three","date_four")

class Activity(models.Model):
    date = models.ForeignKey(Date, editable=False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return '%s: %s' % (self.date, self.description)

    def activity_day(self):
        adate = self.date.activity_date.strftime('%h %d, %Y')
        return u"%s | %s | Week %s, Day %s | %s" % (self.date.goal.user.username,
            self.date.goal.name, self.date.week, self.date.day, adate)

    class Meta:
        ordering = ["date"]
