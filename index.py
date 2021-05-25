#number_of_place = 30
#number_of_person = 0
#nairobi_mombasa = 8500
#nairobi_kigali = 10000
#nairobi_entebbe = 9000
#nairobi_bujumbura = 11500
#nairobi_juba = 12500
#nairobi_goma = 13500
number_of_place = 30
number_of_person = 0

class bus:
    
    def destination(self):
        nairobi_mombasa = 8500
        nairobi_kigali = 10000
        nairobi_entebbe = 9000
        nairobi_bujumbura = 11500
        nairobi_juba = 12500
        nairobi_goma = 13500

class person():
    #number_of_person = 0
  
    def registration(self):
        
        nairobi_mombasa ='Your fare from Nairobi to Mombasa is 8500' 
        nairobi_kigali = 'Your fare from Nairobi to Kigali is 10000'
        nairobi_entebbe = 'Your fare from Nairobi to Entebbe is 9000'
        nairobi_bujumbura = 'Your fare from Nairobi to Bujumbura is 11500'
        nairobi_juba = 'Your fare from Nairobi to Juba is 12500'
        nairobi_goma = 'Your fare from Nairobi to Goma is 13500'
        name  = input("Enter your Name: ")
        print("\t")
        print("1. Nairobi to Mombasa")
        print("2. Nairobi to Kigali")
        print("3. Nairobi to Entebbe")
        print("4. Nairobi to Bujumbura")
        print("5. Nairobi to Juba")
        print("6. Nairobi to Goma")
        print("\t")
        #print("Select your direction: ")
        direction = input("Select your direction: ")
        while(number_of_person <= number_of_place):
            if(direction == '1'):
             print(name +" "+ nairobi_mombasa)
             number_of_person = number_of_person + 5
           # fees = nairobi_mombasa
            elif(direction == '2'):
              print(name +" "+ nairobi_kigali)
              number_of_person = number_of_person + 5
           #fees =  nairobi_kigali
            elif(direction == '3'):
              print(name +" "+ nairobi_entebbe)
              number_of_person = number_of_person + 5
            #fees = nairobi_entebbe
            elif(direction == '4'):
              print(name +" "+ nairobi_bujumbura)
              number_of_person = number_of_person + 5
            #fees = nairobi_bujumbura
            elif(direction == '5'):
              print(name +" "+ nairobi_juba)
              number_of_person = number_of_person + 5
            #fees = nairobi_juba
            elif(direction == '6'):
              print(name +" "+ nairobi_goma)
              number_of_person = number_of_person + 5
            #fees = nairobi_goma
            else:
              print("destination not available")
        

        

while(number_of_person <= number_of_place):
    print("Do you wish to continue to register passenger")
    print("Y or N")
    decision = input("Select decision: ")
    if(decision == "Y"):
     p = person()
     p.registration()
    else:
        print("The bus will leave with" + number_of_place + "person")
        break


        
