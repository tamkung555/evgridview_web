# Generated by Django 2.2.3 on 2020-04-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transformer_model', '0007_auto_20200410_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='transformer_c2',
            name='flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transformer_c2',
            name='impact',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='transformer_c2',
            name='loadProfile_base',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='transformer_c2',
            name='loadProfile_ev',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
    ]
