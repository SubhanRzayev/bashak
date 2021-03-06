# Generated by Django 3.2.4 on 2022-04-18 16:35

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('haqqımızda', models.TextField(max_length=3000)),
                ('haqqımızda_en', models.TextField(max_length=3000, null=True)),
                ('haqqımızda_az', models.TextField(max_length=3000, null=True)),
                ('haqqımızda_ru', models.TextField(max_length=3000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Haqqımızda',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='Bakı şəhəri, Ziya Bünyadov prospekti 3105-ci məhəllə', max_length=200)),
                ('address_en', models.CharField(default='Bakı şəhəri, Ziya Bünyadov prospekti 3105-ci məhəllə', max_length=200, null=True)),
                ('address_az', models.CharField(default='Bakı şəhəri, Ziya Bünyadov prospekti 3105-ci məhəllə', max_length=200, null=True)),
                ('address_ru', models.CharField(default='Bakı şəhəri, Ziya Bünyadov prospekti 3105-ci məhəllə', max_length=200, null=True)),
                ('phone_number1', models.CharField(default='+994 70 252 11 16', max_length=200)),
                ('phone_number2', models.CharField(default='+994 50 888 18 88', max_length=200)),
                ('phone_number3', models.CharField(default='+994 12 511 51 57', max_length=200)),
                ('email', models.EmailField(blank=True, default='info@bashakgroup.az', max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Address',
            },
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200, verbose_name='vəzifə')),
                ('position_en', models.CharField(max_length=200, null=True, verbose_name='vəzifə')),
                ('position_az', models.CharField(max_length=200, null=True, verbose_name='vəzifə')),
                ('position_ru', models.CharField(max_length=200, null=True, verbose_name='vəzifə')),
                ('requirements', ckeditor_uploader.fields.RichTextUploadingField()),
                ('requirements_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('requirements_az', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('requirements_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('obligations', ckeditor_uploader.fields.RichTextUploadingField()),
                ('obligations_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('obligations_az', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('obligations_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('working_conditions', ckeditor_uploader.fields.RichTextUploadingField()),
                ('working_conditions_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('working_conditions_az', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('working_conditions_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=300, null=True, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name_plural': 'Karyera',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=120)),
                ('phone', models.CharField(max_length=80)),
                ('message', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Əlaqə',
            },
        ),
        migrations.CreateModel(
            name='Innovations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_az', models.CharField(max_length=200, null=True)),
                ('title_ru', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(max_length=2000)),
                ('description_en', models.TextField(max_length=2000, null=True)),
                ('description_az', models.TextField(max_length=2000, null=True)),
                ('description_ru', models.TextField(max_length=2000, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('content_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('content_az', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('content_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('news_image', models.ImageField(upload_to='media')),
                ('slug', models.CharField(blank=True, max_length=300, null=True, unique=True, verbose_name='Slug')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('main_news', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Innovations',
            },
        ),
        migrations.CreateModel(
            name='Korporativ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=3000)),
                ('description_en', models.TextField(max_length=3000, null=True)),
                ('description_az', models.TextField(max_length=3000, null=True)),
                ('description_ru', models.TextField(max_length=3000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Korporativ',
            },
        ),
        migrations.CreateModel(
            name='KorporativCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('title_en', models.CharField(max_length=120, null=True)),
                ('title_az', models.CharField(max_length=120, null=True)),
                ('title_ru', models.CharField(max_length=120, null=True)),
                ('image', models.ImageField(blank=True, default='IMG.JPG', null=True, upload_to='media')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('content_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('content_az', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('content_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('slug', models.CharField(blank=True, max_length=300, null=True, unique=True, verbose_name='Slug')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='core.korporativcategory')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('title', models.CharField(max_length=120)),
                ('title_en', models.CharField(max_length=120, null=True)),
                ('title_az', models.CharField(max_length=120, null=True)),
                ('title_ru', models.CharField(max_length=120, null=True)),
                ('description', models.TextField(max_length=2000)),
                ('description_en', models.TextField(max_length=2000, null=True)),
                ('description_az', models.TextField(max_length=2000, null=True)),
                ('description_ru', models.TextField(max_length=2000, null=True)),
                ('general', ckeditor_uploader.fields.RichTextUploadingField()),
                ('general_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('general_az', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('general_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('slug', models.CharField(blank=True, max_length=300, null=True, unique=True, verbose_name='Slug')),
                ('sector_image', models.ImageField(upload_to='media')),
            ],
            options={
                'ordering': ['count'],
            },
        ),
        migrations.CreateModel(
            name='RehberlikCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200)),
                ('position_en', models.CharField(max_length=200, null=True)),
                ('position_az', models.CharField(max_length=200, null=True)),
                ('position_ru', models.CharField(max_length=200, null=True)),
                ('full_name', models.CharField(max_length=200)),
                ('full_name_en', models.CharField(max_length=200, null=True)),
                ('full_name_az', models.CharField(max_length=200, null=True)),
                ('full_name_ru', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to='media')),
                ('facebook_link', models.CharField(blank=True, max_length=120, null=True)),
                ('linkedin_link', models.CharField(blank=True, max_length=120, null=True)),
                ('korporativcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_detail', to='core.korporativcategory')),
            ],
            options={
                'verbose_name_plural': 'Rehberlik Team',
            },
        ),
        migrations.CreateModel(
            name='CategoryDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('title_en', models.CharField(max_length=120, null=True)),
                ('title_az', models.CharField(max_length=120, null=True)),
                ('title_ru', models.CharField(max_length=120, null=True)),
                ('description', models.TextField(max_length=1000)),
                ('description_en', models.TextField(max_length=1000, null=True)),
                ('description_az', models.TextField(max_length=1000, null=True)),
                ('description_ru', models.TextField(max_length=1000, null=True)),
                ('image', models.ImageField(upload_to='media')),
                ('category_design', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories_design', to='core.sector')),
            ],
            options={
                'verbose_name_plural': 'CategoriesDesign',
            },
        ),
        migrations.CreateModel(
            name='CareerCsv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=120)),
                ('cv', models.FileField(blank=True, null=True, upload_to='career/cvler/')),
                ('career', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='careers', to='core.career')),
            ],
        ),
    ]
