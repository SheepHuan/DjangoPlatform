# Generated by Django 5.0 on 2023-12-13 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BenchmarkCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile_model', models.FileField(upload_to='models_files/')),
                ('profile_params', models.JSONField(null=True)),
                ('profile_result', models.JSONField(null=True)),
            ],
        ),
    ]