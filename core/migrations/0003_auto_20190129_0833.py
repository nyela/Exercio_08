# Generated by Django 2.1.4 on 2019-01-29 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190129_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='cliente',
            field=models.CharField(default='', max_length=200, verbose_name='cliente'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='descricao',
            field=models.CharField(default='', max_length=200, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='fornecedor',
            field=models.CharField(default='', max_length=200, verbose_name='fornecedor'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='produto',
            field=models.CharField(default='', max_length=200, verbose_name='produto'),
        ),
    ]
