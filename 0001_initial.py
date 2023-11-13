# Generated by Django 4.2.3 on 2023-11-12 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('product_id', models.CharField(max_length=100)),
                ('brand_name', models.CharField(max_length=100)),
                ('product_description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_link', models.URLField()),
                ('product_category', models.CharField(blank=True, max_length=20, null=True)),
                ('rank', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['rank'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('preferred_category', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
