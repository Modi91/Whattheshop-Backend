# Generated by Django 2.1.5 on 2019-04-03 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190403_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='madeorder', to='api.Order'),
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='product',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orderedproduct', to='api.Product'),
            preserve_default=False,
        ),
    ]
