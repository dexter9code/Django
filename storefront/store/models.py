from asyncio.windows_events import NULL
from dataclasses import field, fields
from gc import collect
from pickle import TRUE
from pyexpat import model
from re import T
from tkinter import CASCADE
from tkinter.tix import Tree
from django.db import models


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    product_summary = models.TextField()
    # feature_product = models.ForeignKey(
    #     'Products', on_delete=models.SET_NULL, NULL=True, related_name='+')


class Products(models.Model):
    title = models.CharField(max_length=255)
    # it makes easier for search-engine to find our content(sreach engine optimize technqie)
    slug = models.SlugField()
    about = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    # update date&time everytime tables gets update
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'bronze'),
        (MEMBERSHIP_SILVER, 'silver'),
        (MEMBERSHIP_GOLD, 'gold'),
    ]
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

    class Meta:
        db_table = 'store.customers'
        indexes = [models.Index(fields=['last_name', 'first_name'])
                   ]


class Order(models.Model):
    STATUS_PEND = 'P'
    STATUS_COMP = 'C'
    STATUS_FAIL = 'F'

    STATUS = [
        (STATUS_PEND, 'pending'),
        (STATUS_COMP, 'completed'),
        (STATUS_FAIL, 'failed'),
    ]
    # store the datetime of order placed at
    place_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=STATUS, default=STATUS_PEND)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class Address(models.Model):
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True)


class Order_item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Products, on_delete=models.PROTECT)
    quantity = models.PositiveBigIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=TRUE)


class Cart_items(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    prouduct = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
