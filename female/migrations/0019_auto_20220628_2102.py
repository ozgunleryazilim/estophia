# Generated by Django 3.2 on 2022-06-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('female', '0018_femalehomeslidertranslation_redirect_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='femalehomeslidertranslation',
            name='redirect_link',
        ),
        migrations.AddField(
            model_name='femalehomeslidertranslation',
            name='redirect_url',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Redirect Link'),
        ),
    ]
