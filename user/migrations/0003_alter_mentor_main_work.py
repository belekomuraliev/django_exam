# Generated by Django 3.2 on 2022-11-28 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_student_work_study_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='main_work',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
