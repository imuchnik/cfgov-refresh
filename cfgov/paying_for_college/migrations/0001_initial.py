# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-25 02:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.TextField()),
                ('is_primary', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Aliases',
            },
        ),
        migrations.CreateModel(
            name='BAHRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip5', models.CharField(max_length=5)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ConstantCap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(blank=True, help_text='VARIABLE NAME FOR JS', max_length=255)),
                ('value', models.IntegerField()),
                ('note', models.TextField(blank=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['slug'],
            },
        ),
        migrations.CreateModel(
            name='ConstantRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(blank=True, help_text='VARIABLE NAME FOR JS', max_length=255)),
                ('value', models.DecimalField(decimal_places=5, max_digits=6)),
                ('note', models.TextField(blank=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['slug'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contacts', models.TextField(blank=True, help_text='COMMA-SEPARATED LIST OF EMAILS')),
                ('endpoint', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('internal_note', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Nickname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.TextField()),
                ('is_female', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['nickname'],
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(blank=True, null=True)),
                ('oid', models.CharField(max_length=40)),
                ('timestamp', models.DateTimeField()),
                ('errors', models.CharField(max_length=255)),
                ('emails', models.TextField(blank=True, help_text='COMMA-SEPARATED STRING OF EMAILS')),
                ('sent', models.BooleanField(default=False)),
                ('log', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=255)),
                ('accreditor', models.CharField(blank=True, max_length=255)),
                ('level', models.CharField(blank=True, max_length=255)),
                ('program_code', models.CharField(blank=True, max_length=255)),
                ('campus', models.CharField(blank=True, max_length=255)),
                ('cip_code', models.CharField(blank=True, max_length=255)),
                ('soc_codes', models.CharField(blank=True, max_length=255)),
                ('total_cost', models.IntegerField(blank=True, help_text='COMPUTED', null=True)),
                ('time_to_complete', models.IntegerField(blank=True, help_text='IN MONTHS', null=True)),
                ('completion_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('completion_cohort', models.IntegerField(blank=True, help_text='COMPLETION COHORT', null=True)),
                ('completers', models.IntegerField(blank=True, help_text='COMPLETERS OF THE PROGRAM', null=True)),
                ('titleiv_debt', models.IntegerField(blank=True, null=True)),
                ('private_debt', models.IntegerField(blank=True, null=True)),
                ('institutional_debt', models.IntegerField(blank=True, null=True)),
                ('mean_student_loan_completers', models.IntegerField(blank=True, help_text='TITLEIV_DEBT + PRIVATE_DEBT + INSTITUTIONAL_DEBT', null=True)),
                ('median_student_loan_completers', models.IntegerField(blank=True, help_text='TITLEIV_DEBT + PRIVATE_DEBT + INSTITUTIONAL_DEBT', null=True)),
                ('default_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('salary', models.IntegerField(blank=True, help_text='MEDIAN SALARY', null=True)),
                ('program_length', models.IntegerField(blank=True, help_text='IN MONTHS', null=True)),
                ('tuition', models.IntegerField(blank=True, null=True)),
                ('fees', models.IntegerField(blank=True, null=True)),
                ('housing', models.IntegerField(blank=True, help_text='HOUSING & MEALS', null=True)),
                ('books', models.IntegerField(blank=True, help_text='BOOKS & SUPPLIES', null=True)),
                ('transportation', models.IntegerField(blank=True, null=True)),
                ('other_costs', models.IntegerField(blank=True, null=True)),
                ('job_rate', models.DecimalField(blank=True, decimal_places=2, help_text='COMPLETERS WHO GET RELATED JOB', max_digits=5, null=True)),
                ('job_note', models.TextField(blank=True, help_text='EXPLANATION FROM SCHOOL')),
                ('test', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ope6_id', models.IntegerField(blank=True, null=True)),
                ('ope8_id', models.IntegerField(blank=True, null=True)),
                ('settlement_school', models.CharField(blank=True, default='', max_length=100)),
                ('data_json', models.TextField(blank=True)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=2)),
                ('zip5', models.CharField(blank=True, max_length=5)),
                ('enrollment', models.IntegerField(blank=True, null=True)),
                ('accreditor', models.CharField(blank=True, max_length=255)),
                ('ownership', models.CharField(blank=True, max_length=255)),
                ('control', models.CharField(blank=True, help_text="'Public', 'Private' or 'For-profit'", max_length=50)),
                ('url', models.TextField(blank=True)),
                ('degrees_predominant', models.TextField(blank=True)),
                ('degrees_highest', models.TextField(blank=True)),
                ('main_campus', models.NullBooleanField()),
                ('online_only', models.NullBooleanField()),
                ('operating', models.BooleanField(default=True)),
                ('under_investigation', models.BooleanField(default=False, help_text='Heightened Cash Monitoring 2')),
                ('KBYOSS', models.BooleanField(default=False)),
                ('grad_rate_4yr', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('grad_rate_lt4', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('grad_rate', models.DecimalField(blank=True, decimal_places=3, help_text='A 2-YEAR POOLED VALUE', max_digits=5, null=True)),
                ('repay_3yr', models.DecimalField(blank=True, decimal_places=10, help_text='GRADS WITH A DECLINING BALANCE AFTER 3 YRS', max_digits=13, null=True)),
                ('default_rate', models.DecimalField(blank=True, decimal_places=3, help_text='LOAN DEFAULT RATE AT 3 YRS', max_digits=5, null=True)),
                ('median_total_debt', models.DecimalField(blank=True, decimal_places=1, help_text='MEDIAN STUDENT DEBT', max_digits=7, null=True)),
                ('median_monthly_debt', models.DecimalField(blank=True, decimal_places=9, help_text='MEDIAN STUDENT MONTHLY DEBT', max_digits=14, null=True)),
                ('median_annual_pay', models.IntegerField(blank=True, help_text='MEDIAN PAY 10 YRS AFTER ENTRY', null=True)),
                ('avg_net_price', models.IntegerField(blank=True, help_text='OVERALL AVERAGE', null=True)),
                ('tuition_out_of_state', models.IntegerField(blank=True, null=True)),
                ('tuition_in_state', models.IntegerField(blank=True, null=True)),
                ('offers_perkins', models.BooleanField(default=False)),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='paying_for_college.Contact')),
            ],
        ),
        migrations.AddField(
            model_name='program',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paying_for_college.School'),
        ),
        migrations.AddField(
            model_name='notification',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paying_for_college.School'),
        ),
        migrations.AddField(
            model_name='nickname',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paying_for_college.School'),
        ),
        migrations.AddField(
            model_name='alias',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paying_for_college.School'),
        ),
    ]