# Generated by Django 2.1.1 on 2018-10-28 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20181027_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='borrow_date',
            field=models.DateField(default=None, null=True),
        ),
    ]