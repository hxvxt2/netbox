# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 16:22
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0010_devicebay_installed_device_set_null'),
        ('ipam', '0002_vrf_add_enforce_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='VLANGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vlan_groups', to='dcim.Site')),
            ],
            options={
                'ordering': ['site', 'name'],
            },
        ),
        migrations.AddField(
            model_name='vlan',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vlans', to='ipam.VLANGroup'),
        ),
        migrations.AlterUniqueTogether(
            name='vlangroup',
            unique_together=set([('site', 'name'), ('site', 'slug')]),
        ),
    ]
