class Living():
    @staticmethod
    def living_room():
        room_mates=[]
        name = raw_input("Please input your name::")
        name = +1

        if name <= 6:
            room_mates.append(name)
            print "WELCOME, YOU HAVE BEEN ADDED INTO THE ROOM"
            print len(room_mates)
            print room_mates