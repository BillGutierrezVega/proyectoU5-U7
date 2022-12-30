# Generated by Django 4.1.4 on 2022-12-30 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('paymentDate', models.DateTimeField()),
                ('expirationDate', models.DateTimeField()),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.servicesmoldel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usermodel')),
            ],
        ),
        migrations.CreateModel(
            name='ExpiredPaymentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penalty_fee_amount', models.FloatField()),
                ('payment_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagos.paymentusermodel')),
            ],
        ),
    ]