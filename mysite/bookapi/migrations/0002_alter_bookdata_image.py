# Generated by Django 4.1.7 on 2023-03-17 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdata',
            name='Image',
            field=models.ImageField(upload_to='Images'),
        ),
    ]