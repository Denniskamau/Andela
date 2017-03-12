class Office():
    @staticmethod
    def office_space():
        office_mates = []
        name = raw_input("Please input your name::")
        name = +1
        
        if name <= 6:
            office_mates.append(name)
            print "WELCOME, YOU HAVE BEEN ADDED INTO THE OFFICE"
            print len(office_mates)
            print office_mates
        elif name > 6:
            print "The office is curently full"

   
