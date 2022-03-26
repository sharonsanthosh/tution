# Generated by Django 4.0.3 on 2022-03-23 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.CharField(default='', max_length=240, null=True)),
                ('ifsc', models.CharField(default='', max_length=240, null=True)),
                ('branch', models.CharField(max_length=100)),
                ('transactiondate', models.DateField(blank=True, null=True)),
                ('amount', models.CharField(max_length=240, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='paymentuser', to='base_app.user_registration')),
            ],
        ),
    ]