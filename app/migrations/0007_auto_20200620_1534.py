# Generated by Django 3.0.7 on 2020-06-20 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_contact_posting'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='gradation',
            field=models.IntegerField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='contact',
            name='posting',
            field=models.CharField(max_length=200),
        ),
    ]
