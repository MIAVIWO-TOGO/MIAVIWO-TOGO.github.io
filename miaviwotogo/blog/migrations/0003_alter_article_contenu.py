# Generated by Django 4.2.6 on 2023-10-06 13:04

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_contenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='contenu',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
