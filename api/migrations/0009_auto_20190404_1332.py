# Generated by Django 2.1.5 on 2019-04-04 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190403_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='img_Prodect')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='img',
        ),
        migrations.RemoveField(
            model_name='product',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='img3',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.Image'),
            preserve_default=False,
        ),
    ]