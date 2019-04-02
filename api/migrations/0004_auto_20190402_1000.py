# Generated by Django 2.1.5 on 2019-04-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190401_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img2',
            field=models.ImageField(null=True, upload_to='img_Prodect'),
        ),
        migrations.AddField(
            model_name='product',
            name='img3',
            field=models.ImageField(null=True, upload_to='img_Prodect'),
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(related_name='prodects', to='api.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
