# Generated by Django 2.1.7 on 2019-03-16 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20190316_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(),
        ),
    ]
