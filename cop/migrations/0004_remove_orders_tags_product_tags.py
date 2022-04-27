# Generated by Django 4.0.2 on 2022-04-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cop', '0003_tag_orders_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='cop.tag'),
        ),
    ]