# -*- coding: utf-8 -*-


#Legger inn en variabel
formatter = "%r %r %r %r"

# Printer ut variabelen med ulikt innhold og ulikt format
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)

#Printer ut strengene på samme linje
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
