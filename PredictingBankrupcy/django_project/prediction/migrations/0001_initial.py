# Generated by Django 3.1 on 2020-11-10 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='financialData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entryNo', models.IntegerField()),
                ('companyName', models.CharField(max_length=100)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('ASSETS', models.FloatField()),
                ('CASH', models.FloatField()),
                ('CFFO', models.FloatField()),
                ('COGS', models.FloatField()),
                ('CURASS', models.FloatField()),
                ('CURDEBT', models.FloatField()),
                ('DEBTS', models.FloatField()),
                ('INC', models.FloatField()),
                ('INCDEP', models.FloatField()),
                ('INV', models.FloatField()),
                ('REC', models.FloatField()),
                ('SALES', models.FloatField()),
                ('WCFO', models.FloatField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
