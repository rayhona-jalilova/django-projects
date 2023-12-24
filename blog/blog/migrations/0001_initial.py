# Generated by Django 5.0 on 2023-12-21 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
