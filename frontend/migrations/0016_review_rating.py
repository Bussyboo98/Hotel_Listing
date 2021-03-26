# Generated by Django 3.1.1 on 2021-01-25 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0015_auto_20210119_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), ('', 'Choose Rating')], default='', max_length=15),
        ),
    ]