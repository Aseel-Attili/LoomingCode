# Generated by Django 5.0.3 on 2024-06-18 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0066_course_algo_course_back_course_basic_course_front_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaireresponse',
            name='q1',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='questionnaireresponse',
            name='q1_2',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='questionnaireresponse',
            name='q2',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='questionnaireresponse',
            name='q3',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='questionnaireresponse',
            name='q4',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='questionnaireresponse',
            name='q5',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
