# -*- coding: utf-8 -*-
# Lager en variabel, x, der tallet 10 blir lagt inn
x = "There are %d types of people." % 10

# Variabelen binary og do_not, inneholder hver sin string
binary = "binary"
do_not = "don't"

# Lager en variabel, y, som inneholder en string med to variabler i seg
y = "Those who know %s and thos who %s." % (binary, do_not)

# Printer ut variablene x og y
print x
print y

# Printer ut en string pluss en variabel
print "I said %r." % x
print "I also said: '%s'." % y


hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Printer ut joke_evaluation med hilarious
print joke_evaluation % hilarious

# Gir en string verdier til variablene
w = "This is the left side of..."
e = "a string with a right side."

# Printer ut begge variablene
print w + e
