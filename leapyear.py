def IsLeapYear(year):
    if(year % 4) == 0:
        if( year % 100) == 0:
            return 'NO'
        
        return 'YES'

    else:
        return 'NO'