# Generated by Django 4.0.5 on 2022-06-13 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImgToProc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
