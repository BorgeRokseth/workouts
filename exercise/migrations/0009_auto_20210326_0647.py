# Generated by Django 3.1.6 on 2021-03-26 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
        ('exercise', '0008_auto_20210326_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='equipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='equipment.equipment'),
        ),
    ]
