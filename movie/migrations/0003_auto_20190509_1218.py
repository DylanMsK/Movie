# Generated by Django 2.1.7 on 2019-05-09 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20190509_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='score',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='score_movie', to='movie.Score'),
        ),
    ]