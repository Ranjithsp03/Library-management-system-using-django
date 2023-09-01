# Generated by Django 3.2.14 on 2022-12-02 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0002_auto_20221202_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lib.book')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lib.student')),
            ],
        ),
    ]
