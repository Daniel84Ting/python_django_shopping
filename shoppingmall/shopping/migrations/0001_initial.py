# Generated by Django 3.2 on 2021-04-25 16:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('cover', models.ImageField(upload_to='uploads/%Y/$m/%d')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
