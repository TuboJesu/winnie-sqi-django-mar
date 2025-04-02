# Generated by Django 5.1.7 on 2025-04-02 10:54

import django.db.models.deletion
import review.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('year_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('genre', models.CharField(choices=[('FTSY', 'Fantasy'), ('SCIFI', 'Science Fiction'), ('MYST_THRILL', 'Mystery/Thriller'), ('ROM', 'Romance'), ('HIST_FIC', 'Historical Fiction'), ('HORROR', 'Horror'), ('DYST', 'Dystopian'), ('ADVN', 'Adventure'), ('BIO_AUTOBIO', 'Biography/Autobiography'), ('SELF_HELP', 'Self Help'), ('HIST', 'History'), ('SCI', 'Science'), ('BSNS', 'Business')], default='ADVN', max_length=15)),
                ('publication_date', models.DateField()),
                ('cover_image', models.ImageField(default='default-cover.jpg', upload_to=review.models.book_cover_upload_to)),
                ('isbn', models.CharField(max_length=100)),
                ('number_of_pages', models.PositiveIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='review.author')),
            ],
        ),
    ]
