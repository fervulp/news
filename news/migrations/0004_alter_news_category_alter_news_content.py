# Generated by Django 4.0.3 on 2022-03-23 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_category_news_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(blank=True, max_length=10000, verbose_name='Содержание'),
        ),
    ]