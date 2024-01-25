# Generated by Django 4.1.13 on 2024-01-25 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[['PENDING', 'PENDING'], ['INPROGRESS', 'INPROGRESS'], ['COMPLETED', 'COMPLETED'], ['OVERDUE', 'OVERDUE']], default='PENDING', max_length=50),
        ),
    ]
