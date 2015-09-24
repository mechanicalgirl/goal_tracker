# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('week', models.IntegerField()),
                ('day', models.IntegerField()),
                ('activity_date', models.DateTimeField(editable=False)),
            ],
            options={
                'ordering': ['goal'],
            },
        ),
        migrations.CreateModel(
            name='Dateset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('complete', models.BooleanField(default=False)),
                ('date_four', models.ForeignKey(related_name='date_four', to='goals.Date')),
                ('date_one', models.ForeignKey(related_name='date_one', to='goals.Date')),
                ('date_three', models.ForeignKey(related_name='date_three', to='goals.Date')),
                ('date_two', models.ForeignKey(related_name='date_two', to='goals.Date')),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
                ('complete', models.BooleanField(default=False, editable=False)),
                ('user', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Goalset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date started')),
                ('complete_date', models.DateTimeField(verbose_name=b'date completed', null=True, editable=False, blank=True)),
                ('goal_four', models.ForeignKey(related_name='goal_four', to='goals.Goal')),
                ('goal_one', models.ForeignKey(related_name='goal_one', to='goals.Goal')),
                ('goal_three', models.ForeignKey(related_name='goal_three', to='goals.Goal')),
                ('goal_two', models.ForeignKey(related_name='goal_two', to='goals.Goal')),
            ],
            options={
                'ordering': ['active_date'],
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('week', models.IntegerField()),
                ('day', models.IntegerField()),
                ('quote', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['week', 'day'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='quote',
            unique_together=set([('week', 'day')]),
        ),
        migrations.AddField(
            model_name='date',
            name='goal',
            field=models.ForeignKey(to='goals.Goal'),
        ),
        migrations.AddField(
            model_name='activity',
            name='date',
            field=models.ForeignKey(editable=False, to='goals.Date'),
        ),
        migrations.AlterUniqueTogether(
            name='goalset',
            unique_together=set([('goal_one', 'goal_two', 'goal_three', 'goal_four')]),
        ),
        migrations.AlterUniqueTogether(
            name='goal',
            unique_together=set([('user', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='dateset',
            unique_together=set([('date_one', 'date_two', 'date_three', 'date_four')]),
        ),
        migrations.AlterUniqueTogether(
            name='date',
            unique_together=set([('goal', 'week', 'day')]),
        ),
    ]
