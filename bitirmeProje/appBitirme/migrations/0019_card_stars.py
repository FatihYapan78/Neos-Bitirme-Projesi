# Generated by Django 4.1.5 on 2023-03-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBitirme', '0018_alter_card_categorys'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='stars',
            field=models.FloatField(default=0, null=True, verbose_name='Puan'),
        ),
    ]
