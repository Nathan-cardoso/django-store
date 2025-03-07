from django.db import models


class Promotion(models.Model):
    description = models.CharField(
        max_length=255
    )

    discount = models.FloatField()


class Collection(models.Model):

    title = models.CharField(
        max_length=255
    )

    feature_product = models.ForeignKey(
        'Product',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )


class Product(models.Model):

    title = models.CharField(
        max_length=255
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    inventory = models.IntegerField()

    last_update = models.DateTimeField(
    auto_now=True
    )

    collection = models.ForeignKey(
        Collection,
        on_delete=models.PROTECT
    )

    promotions = models.ManyToManyField(
        Promotion,
        related_name="products"
    )


class Customer(models.Model):

    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOISE = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]

    first_name = models.CharField(
        max_length=255
    )

    last_name = models.CharField(
        max_length=255
    )

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=15
    )

    birth_date = models.DateField(
        null=True
    )

    membership = models.CharField(
        max_length=1,
        choices=MEMBERSHIP_CHOISE,
        default=MEMBERSHIP_BRONZE
    )


class Order(models.Model):

    PAYMENTSTATUS_PENDING = 'P'
    PAYMENTSTATUS_COMPLETED = 'C'
    PAYMENTSTATUS_FALIDED= 'F'

    PAYMENTSTATUS_CHOISE = [
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('F', 'Faliled')
    ]

    placed_at = models.DateTimeField(
        auto_now_add=True
    )

    payment_status = models.CharField(
        max_length=1,
        choices=PAYMENTSTATUS_CHOISE,
        default=PAYMENTSTATUS_PENDING
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT
    )


class OrderItem(models.Model):


    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )

    quantity = models.PositiveSmallIntegerField()

    unit_price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )


class Adress(models.Model):

    street = models.CharField(
        max_length=255

    )

    city = models.CharField(
        max_length=255
    )

    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        primary_key=True
    )


class Cart(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveSmallIntegerField()
