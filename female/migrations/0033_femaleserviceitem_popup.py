# Generated by Django 3.2 on 2022-09-20 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('popup', '0001_initial'),
        ('female', '0032_femaleservicecategory_popup'),
    ]

    operations = [
        migrations.AddField(
            model_name='femaleserviceitem',
            name='popup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='popup.popup', verbose_name='Popup'),
        ),
    ]
