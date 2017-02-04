import time
import winsound


while (1):
    cuckooHour = time.strftime('%I')
    cuckooMinute = time.strftime('%M')
    cuckooSecond = time.strftime('%S')
    if cuckooMinute in ('00', '10', '15', '20', '30', '40', '45', '50'):
        print 'DING'
        winsound.Beep(14000, 150)
        winsound.Beep(7000, 250)
        winsound.Beep(35000, 100)
        winsound.Beep(28000, 500)
        winsound.Beep(14000, 250)
        print cuckooHour + ':' + cuckooMinute + ':' + cuckooSecond

    time.sleep(60)
    
