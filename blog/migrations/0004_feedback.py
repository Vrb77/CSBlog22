# Generated by Django 4.0.4 on 2022-07-03 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_cdody_comment_cbody'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.CharField(default='', max_length=20)),
                ('suggestion', models.CharField(default='', max_length=150)),
            ],
        ),
    ]
