

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('stock', models.IntegerField()),
                ('img', models.ImageField(null=True, upload_to='img_Prodect')),
                ('category', models.ManyToManyField(related_name='prodects', to='api.Category')),
            ],
        ),
    ]
