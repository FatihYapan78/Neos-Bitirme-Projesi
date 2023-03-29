# Generated by Django 4.1.5 on 2023-03-28 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appBitirme', '0028_alter_anumara_beden_alter_numara_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sepeturun',
            name='urun',
        ),
        migrations.AddField(
            model_name='sepeturun',
            name='Aurun',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appBitirme.anumara', verbose_name='Ürün'),
        ),
        migrations.AddField(
            model_name='sepeturun',
            name='Eurun',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appBitirme.ebeden', verbose_name='Ürün'),
        ),
    ]
