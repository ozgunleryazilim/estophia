# Generated by Django 3.2 on 2022-06-26 20:52

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('male', '0013_malebeforeafteritem_malebeforeafterpageseo_malebeforeafterpageseotranslation'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaleBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogs', verbose_name='Banner Image')),
                ('view_count', models.IntegerField(default=0, verbose_name='View Count')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MaleBlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('order', models.IntegerField(default=1, verbose_name='Ordering')),
            ],
            options={
                'verbose_name': 'Blog Category',
                'verbose_name_plural': 'Blog Categories',
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MaleBlogsPageSeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image', models.ImageField(blank=True, null=True, upload_to='blogs//banner', verbose_name='Banner Image')),
                ('meta_keywords', models.ManyToManyField(blank=True, to='common.Keywords', verbose_name='Meta Anahtar Kelimeler')),
            ],
            options={
                'verbose_name': 'Blogs Page SEO',
                'verbose_name_plural': 'Blogs Page SEO',
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MaleBlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name *')),
                ('email', models.EmailField(max_length=254, verbose_name='Email *')),
                ('comment', models.TextField(verbose_name='Write review *')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Is Approved')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='male.maleblog', verbose_name='Blog')),
            ],
            options={
                'verbose_name': 'Blog Comment',
                'verbose_name_plural': 'Blog Comments',
                'ordering': ('-created_date',),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='maleblog',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='male.maleblogcategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='maleblog',
            name='meta_keywords',
            field=models.ManyToManyField(blank=True, to='common.Keywords', verbose_name='Meta Anahtar Kelimeler'),
        ),
        migrations.CreateModel(
            name='MaleBlogTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='Title')),
                ('slug', models.SlugField(max_length=200, verbose_name='Slug')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Content Body 1')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='male.maleblog')),
            ],
            options={
                'verbose_name': 'Blog Translation',
                'db_table': 'male_maleblog_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MaleBlogsPageSeoTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('seo_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='SEO Başlığı')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Meta Açıklaması')),
                ('banner_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Banner Title')),
                ('banner_description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Banner Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='male.maleblogspageseo')),
            ],
            options={
                'verbose_name': 'Blogs Page SEO Translation',
                'db_table': 'male_maleblogspageseo_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MaleBlogCategoryTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('slug', models.SlugField(max_length=200, verbose_name='Slug')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='male.maleblogcategory')),
            ],
            options={
                'verbose_name': 'Blog Category Translation',
                'db_table': 'male_maleblogcategory_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
