# Generated by Django 2.2.1 on 2019-06-17 19:04

from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'ContactInfo',
                'verbose_name_plural': 'ContactInfos',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Ingredient',
                'verbose_name_plural': 'Ingredients',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_id', models.CharField(max_length=50, unique=True)),
                ('restaurant_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Restaurant',
                'verbose_name_plural': 'Restaurants',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pkg_name', models.CharField(max_length=50)),
                ('for_n_persons', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('image', models.ImageField(default='menu/default.png', upload_to='menu/')),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browse.Restaurant')),
            ],
            options={
                'verbose_name': 'Package',
                'verbose_name_plural': 'Packages',
            },
        ),
        migrations.CreateModel(
            name='ItemList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browse.Item')),
                ('pkg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browse.Package')),
            ],
            options={
                'verbose_name': 'ItemList',
                'verbose_name_plural': 'ItemLists',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='item_list',
            field=models.ManyToManyField(through='browse.ItemList', to='browse.Package'),
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_id', models.CharField(max_length=50, unique=True)),
                ('branch_name', models.CharField(max_length=50)),
                ('branch_location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('branch_contact_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browse.ContactInfo')),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browse.Restaurant')),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branchs',
            },
        ),
    ]