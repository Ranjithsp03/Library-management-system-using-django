# Generated by Django 3.2.14 on 2022-12-02 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0003_bookt'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='qty',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
