# Generated by Django 3.2.4 on 2021-06-07 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0002_alter_announcement_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='media',
            field=models.FileField(blank=True, upload_to=None),
        ),
    ]
