# Generated by Django 3.1.7 on 2021-04-07 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='cover',
            field=models.ImageField(default='default cover', upload_to='images/'),
            preserve_default=False,
        ),
    ]
