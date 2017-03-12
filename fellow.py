from office import Office
from living import Living

class Fellow:
    @staticmethod # Makes the method static hence avoiding to intantiate it when calling it.
    def fellower():
         o="office"
         l="living"
         option = raw_input("How do you intend to use the room::")

         if option == o:
             Office.office_space() #calls the office function
         elif option == l:
             Living.living_room() #call living function
         else:
             print "Invalid option try again"

           

   