# Generated by Django 3.1.7 on 2021-05-16 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='images/', verbose_name='Makalenize Foroğraf Ekleyin'),
        ),
    ]
