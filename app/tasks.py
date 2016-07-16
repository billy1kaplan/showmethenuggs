import random

#gets the current nugget value
def getNuggValue():
    changeNuggValue(random())

def changeNuggValue(newVal):
    import views
    print(newVal)
    views.nugg_data = newVal

t = Timer(3, getNuggValue)
t.start()
