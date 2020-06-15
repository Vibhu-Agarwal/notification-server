# Generated by Django 3.0.7 on 2020-06-15 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('method', models.CharField(choices=[('post', 'POST'), ('delete', 'DELETE'), ('patch', 'PATCH'), ('get', 'GET')], default='post', max_length=6)),
                ('data', models.TextField(null=True)),
                ('time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
                'ordering': ['time', 'created_at'],
            },
        ),
    ]
