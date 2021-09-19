# Generated by Django 3.2.7 on 2021-09-17 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=222)),
                ('surname', models.CharField(blank=True, max_length=222)),
                ('lastname', models.CharField(blank=True, max_length=222)),
                ('subject', models.CharField(blank=True, max_length=222)),
                ('level', models.CharField(blank=True, choices=[('Director', 'Direktor'), ('Zauch', 'Zauch'), ('Zamdirector', 'Zamdirektor'), ('Zavhoz', 'Zahvoz')], max_length=222)),
                ('level_years', models.IntegerField()),
                ('image', models.ImageField(upload_to='images')),
                ('classes', models.CharField(blank=True, choices=[('1 a', '1 a'), ('1 b', '1 b'), ('1 v', '1 v'), ('1 g', '1 g'), ('2 a', '2 a'), ('2 b', '2 b'), ('2 v', '2 v'), ('2 g', '2 g')], max_length=222)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]