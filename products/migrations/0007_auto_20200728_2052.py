# Generated by Django 3.0.7 on 2020-07-28 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_promotions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComingSoon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('available_date', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Promotions',
        ),
    ]
