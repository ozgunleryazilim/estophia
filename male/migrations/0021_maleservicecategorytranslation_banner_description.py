# Generated by Django 3.2 on 2022-06-29 20:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('male', '0020_auto_20220629_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='maleservicecategorytranslation',
            name='banner_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Banner Description'),
        ),
    ]
