# Generated by Django 4.2.5 on 2023-10-06 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_inq"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehicle",
            name="razorpay_order_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="vehicle",
            name="razorpay_payment_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="vehicle",
            name="razorpay_payment_signature",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name="Inq",
        ),
    ]
