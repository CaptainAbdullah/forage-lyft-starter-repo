from battery import Battery

class nubbin_battery(Battery):
    def __init__(self,last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    def needs_service(self):
        #logic here