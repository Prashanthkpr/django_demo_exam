# Generated by Django 2.2.2 on 2019-06-07 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete='SET_NULL', to='exam.Question'),
        ),
    ]