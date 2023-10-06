# Generated by Django 4.2.6 on 2023-10-06 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('shop_name', models.CharField(max_length=100, null=True)),
                ('longitude', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('discription', models.TextField(null=True)),
                ('salary', models.FloatField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(max_length=30, null=True)),
                ('experience', models.CharField(max_length=30, null=True)),
                ('eduction', models.CharField(max_length=100, null=True)),
                ('skill', models.CharField(max_length=100, null=True)),
                ('job_link', models.URLField(null=True)),
                ('ratings', models.IntegerField(null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='infodb',
        ),
    ]
