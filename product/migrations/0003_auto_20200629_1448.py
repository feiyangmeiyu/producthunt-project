# Generated by Django 3.0.7 on 2020-06-29 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200629_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.TextField(default='This is the url.'),
        ),
    ]
