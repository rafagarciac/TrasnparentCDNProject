# Generated by Django 2.1.1 on 2018-10-27 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20181027_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='user_borrowed',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
