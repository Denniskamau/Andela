from armity import Armity 
from fellow import Fellow 
from staff import Staff 
class Room:
    s="staff"
    f="fellow"
    input = raw_input("Hi, please identify yourself by either: o for staff or s for fellow ::")


    if input == s:
        
        Staff.member()#runs the member method in a static manner.
    elif input == f:
        
        Fellow.fellower()#runs the fellower method in a static manner
    else:
        print "Invalid option"               
   
 
       

          