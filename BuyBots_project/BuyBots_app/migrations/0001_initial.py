# Generated by Django 2.0.7 on 2018-08-07 17:47

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
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_path', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('login', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BuyBots_app.Admin')),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('login', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('id_bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BuyBots_app.Bot')),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BuyBots_app.Client')),
            ],
        ),
        migrations.AddField(
            model_name='deal',
            name='id_developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BuyBots_app.Developer'),
        ),
        migrations.AddField(
            model_name='bot',
            name='id_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BuyBots_app.Category'),
        ),
        migrations.AddField(
            model_name='bot',
            name='id_developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BuyBots_app.Developer'),
        ),
    ]
