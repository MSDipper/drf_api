# Generated by Django 4.1.7 on 2023-03-22 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='imageroom',
            field=models.ManyToManyField(blank=True, null=True, related_name='room', to='hotel.imageroom', verbose_name='Изображения'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Главное изображение'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name_video',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Заголовок к видео'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='video/', verbose_name='Видео'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='hotel.hotel', verbose_name='Отель'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='hotel.hotel', verbose_name='Отель'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='hotel.reviews', verbose_name='Родитель'),
        ),
    ]
