# Generated by Django 3.1.6 on 2021-03-26 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
        ('exercise', '0009_auto_20210326_0647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='equipment',
        ),
        migrations.AddField(
            model_name='exercise',
            name='equipment',
            field=models.ManyToManyField(to='equipment.Equipment'),
        ),
    ]
