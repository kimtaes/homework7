def IsLeapYear(year):
    if(year % 4) == 0:
        if( year % 100) == 0:
            if(year % 400) == 0:
                return 'YES'
            else:
                return 'NO'
                
        return 'YES'

    else:
        return 'NO'