from django.db import models

from .utils import ChoiceEnum


class Make(models.Model):
    make = models.CharField('Make', max_length=40)

    def __str__(self):
        return self.make


class Car(models.Model):
    # Querying requires an extra word to type though...
    # red_cars = Car.objects.filter(color=Car.Colors.RED.value)
    # Encapsulation, we meet again.
    class CarSize(ChoiceEnum):
        SUBCOMPACT = "Subcompact"
        MID_SIZE = "Mid Size"
        COMPACT = "Compact"
        TWO_SEATER = "Two Seater"
        FULL_SIZE = "Full Size"
        STATIONWAGON_SMALL = "Station Wagon - Small"
        SUV_STANDARD = "SUV Standard"

    class Colors(ChoiceEnum):
        RED = "red"
        WHITE = "white"
        BLUE = "blue"
        BLACK = "black"
        YELLOW = "yellow"
        SILVER = "silver"

    base_color = models.CharField(max_length=6, choices=Colors.choices(), default=Colors.RED)
    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name='maker')
    model = models.CharField('Model', max_length=40)
    size = models.CharField(max_length=18, choices=CarSize.choices(), default=CarSize.FULL_SIZE)
    year = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.make} {self.year} {self.model}"
