# Generated by Django 4.2.4 on 2023-08-17 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_blogs_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('desc', models.CharField(max_length=1000)),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.blogs')),
            ],
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
