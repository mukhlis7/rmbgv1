# Generated by Django 4.0.5 on 2022-06-13 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmbgv1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imgtoproc',
            old_name='hotel_Main_Img',
            new_name='Image_To_Process',
        ),
        migrations.AddField(
            model_name='imgtoproc',
            name='name',
            field=models.CharField(default='nothing', max_length=50),
        ),
    ]