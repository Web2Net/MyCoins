# Generated by Django 2.2.7 on 2019-11-26 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_coin_mcm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gyrt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gyrt', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Redkost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redkost', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='coin',
            name='tirazh',
            field=models.CharField(blank=True, help_text='Тираж', max_length=20),
        ),
        migrations.AddField(
            model_name='coin',
            name='gyrt',
            field=models.ForeignKey(help_text='Гурт', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Gyrt'),
        ),
        migrations.AddField(
            model_name='coin',
            name='redkost',
            field=models.ForeignKey(help_text='Редкость', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Redkost'),
        ),
    ]
