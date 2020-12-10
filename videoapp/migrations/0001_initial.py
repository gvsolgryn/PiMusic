# Generated by Django 3.1.4 on 2020-12-10 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('video_img', models.FileField(upload_to='')),
                ('tag', models.CharField(choices=[('Games', 'Games'), ('Anime', 'Anime'), ('Vlog', 'Vlog')], default='Games', max_length=20)),
                ('video_file', models.FileField(upload_to='')),
            ],
        ),
    ]
