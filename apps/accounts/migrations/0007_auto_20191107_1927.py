# Generated by Django 2.2.4 on 2019-11-07 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20191031_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualidentifier',
            name='issuer',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='individualidentifier',
            name='subdivision',
            field=models.CharField(blank=True, default='', help_text="A country's subdivision such as a state or province.", max_length=2, verbose_name='State'),
        ),
    ]
