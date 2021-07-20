from Time_Module import get_hours,get_date
from Output_Module import output
from Database_Module import update_last_seen_date,get_last_seen
from datetime import date
def greet():
    previous_date=get_last_seen()
    today_date =get_date()
    update_last_seen_date(today_date)  

    
    if previous_date==today_date:
        return ('Welcome back, sir')
    else: 
        hour=int (get_hours())
        if hour>=4 and hour<=12:
            return ('Good Morning, sir')

        elif hour>=12 and hour<=16:
            return ('Good After Noon, sir')
        
        else:
            return ('Good Evening, sir')

     
