# Generated by Django 3.1 on 2020-09-01 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('company_address', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('address_pin_location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BusinessOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_thumb', models.ImageField(upload_to='profile/')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessCampaign',
            fields=[
                ('business', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='campaign.business')),
                ('title', models.CharField(max_length=255)),
                ('stock_code', models.CharField(max_length=4)),
                ('stock_price', models.PositiveIntegerField()),
                ('stock_qty', models.PositiveSmallIntegerField()),
                ('deviden_periode', models.PositiveSmallIntegerField()),
                ('date_ended', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.businessowner'),
        ),
        migrations.CreateModel(
            name='CampaignImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='campaign_images/')),
                ('campaign', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='campaign.businesscampaign')),
            ],
        ),
    ]