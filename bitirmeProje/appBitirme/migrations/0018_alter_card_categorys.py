# Generated by Django 4.1.5 on 2023-03-23 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBitirme', '0017_comment_star_alter_card_text_alter_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='categorys',
            field=models.ManyToManyField(to='appBitirme.category', verbose_name='category'),
        ),
    ]
