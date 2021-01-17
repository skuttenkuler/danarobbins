# Generated by Django 3.1.5 on 2021-01-15 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danarobbins', '0002_auto_20210115_0513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(default='', max_length=50)),
                ('time', models.DateTimeField(default='')),
                ('artist_name', models.CharField(default='', max_length=50)),
                ('ticket_link', models.URLField(verbose_name='Concert Link')),
            ],
        ),
        migrations.DeleteModel(
            name='Gigs',
        ),
    ]