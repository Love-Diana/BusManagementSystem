# Generated by Django 3.2 on 2021-12-27 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='punishment',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
