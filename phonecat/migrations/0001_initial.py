# Generated by Django 3.0.5 on 2020-04-15 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhonesTab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('RegDate', models.DateTimeField(verbose_name='date published')),
                ('Address', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=30)),
            ],
        ),
    ]
