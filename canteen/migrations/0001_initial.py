<<<<<<< HEAD
# Generated by Django 2.2.2 on 2020-04-29 21:08
=======
# Generated by Django 2.2.2 on 2020-04-30 18:22
>>>>>>> upstream/Restore

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Food_items',
=======
            name='Food_item',
>>>>>>> upstream/Restore
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('price', models.IntegerField(default=None)),
            ],
        ),
<<<<<<< HEAD
=======
        migrations.CreateModel(
            name='Profile3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('order_status', models.IntegerField(default=None)),
            ],
        ),
>>>>>>> upstream/Restore
    ]
