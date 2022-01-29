# Generated by Django 4.0.1 on 2022-01-27 15:34

import bootcamp.models
from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootcamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True)),
                ('website', models.URLField(max_length=255)),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=225, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('careers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=8)),
                ('averageRating', django.contrib.postgres.fields.ranges.IntegerRangeField()),
                ('averageCost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('photo', models.ImageField(null=True, upload_to=bootcamp.models.bootcamp_image_file_path)),
                ('housing', models.BooleanField(default=False)),
                ('jobAssitance', models.BooleanField(default=False)),
                ('jobGuarantee', models.BooleanField(default=False)),
                ('acceptGi', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]