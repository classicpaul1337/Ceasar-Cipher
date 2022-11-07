from ceasar import Ceasar


service_is_on = True
while service_is_on:
    ceasar = Ceasar()
    ceasar.cipher()
    query = input("Are you still using this service? yes / no: ").lower()
    if query != 'yes':
        service_is_on = False
        print("Goodbye!")
