# -*- coding: utf-8 -*-


# Lager en variabel, cars, som er antall biler, med verdi 100
cars = 100

# Lager en variabel, space_in_a_car, som er antall passasjerer det er plass til i en bil
space_in_a_car = 4.0

# Lager en variabel, drivers, som er antall sjåfører
drivers = 30

# Lager en variabel, passengers, som er antall passasjerer
passengers = 90

# Lager en variabel, cars_not_driven, som er lik antall biler minus antall sjåfører
cars_not_driven = cars - drivers

# Lager en variabel, cars_driven, som er lik antall sjåfører
cars_driven = drivers

# Lager en variabel, carpool_capacity, som er lik antall biler som blir kjørt ganger antall plasser til passasjerer i hver bil
carpool_capacity = cars_driven * space_in_a_car

# Lager en variabel, average_passangers_per_car, som er antall passasjerer delt på antall biler som blir kjørt
average_passengers_per_car = passengers / cars_driven


# Printer ut tekst og variabler

print "There are", cars, "cars available"
print "There are only", drivers, "available"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "we need to put about", average_passengers_per_car, "in each car"

