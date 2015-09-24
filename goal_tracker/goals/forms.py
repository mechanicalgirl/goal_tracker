from django import forms

from .models import Goal, Goalset, Date, Dateset, Activity

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'description']

class GoalsetForm(forms.ModelForm):
    class Meta:
        model = Goalset
        fields = ['goal_one', 'goal_two', 'goal_three', 'goal_four']

    def __init__(self, *args, **kwargs):
        try:
            user = kwargs.pop('user')
            super(GoalsetForm, self).__init__(*args, **kwargs)
            self.fields['goal_one'].queryset = Goal.objects.filter(complete=False, user=user)
            self.fields['goal_two'].queryset = Goal.objects.filter(complete=False, user=user)
            self.fields['goal_three'].queryset = Goal.objects.filter(complete=False, user=user)
            self.fields['goal_four'].queryset = Goal.objects.filter(complete=False, user=user)
        except KeyError:
            super(GoalsetForm, self).__init__(*args, **kwargs)

class DateForm(forms.ModelForm):
    class Meta:
        model = Date
        fields = ['goal', 'week', 'day']

class DatesetForm(forms.ModelForm):
    class Meta:
        model = Dateset
        fields = ['date_one', 'date_two', 'date_three', 'date_four', 'complete']

class ActivityForm(forms.ModelForm):
    class Meta:
      model = Activity
      fields = ['description']
