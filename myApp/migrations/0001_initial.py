# Generated by Django 3.0.3 on 2020-03-28 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rdate', models.DateTimeField()),
                ('rplace', models.CharField(max_length=20)),
                ('rnum', models.CharField(max_length=20)),
                ('rcat', models.CharField(max_length=20)),
                ('rphoto', models.ImageField(blank=True, null=True, upload_to='')),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
