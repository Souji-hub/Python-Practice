dem = 0
try: 
    even = [2,4,6,8]
    check =  even[2]/dem
    print(even[5])

except ZeroDivisionError:
        print("denominator cannot be zero")

except IndexError:
        print("Index out of bound")

        
x = 'hello'

if  not type(x) is int:
        raise TypeError("Only integers are allowed")

def KelvinToFahrenheit(Temperature):
        assert(Temperature>=0),"Colder than absolute zero!"
        return ((Temperature - 273)*1.8)+32

print (KelvinToFahrenheit(273))
print(int (KelvinToFahrenheit(505.78)))
print(KelvinToFahrenheit(-5))