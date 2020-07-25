
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food_item',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('price', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Profile3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('order_status', models.IntegerField(default=None)),
            ],
        ),
    ]
