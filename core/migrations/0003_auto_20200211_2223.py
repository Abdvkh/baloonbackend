# Generated by Django 2.1.5 on 2020-02-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tyre_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tyre',
            name='type',
            field=models.CharField(choices=[('Л', 'Легковой'), ('Г', 'Грузовой')], max_length=2, null=True, verbose_name='Тип колеса'),
        ),
    ]
