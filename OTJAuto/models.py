from datetime import datetime, timedelta

class Activity:
    def __init__(self, date: str, start_time: str, duration: int, description: str, module_names: list, ksbs: list):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.start_time = datetime.strptime(start_time, "%H:%M").time()
        self.duration = duration
        self.description = description
        self.module_names = module_names
        self.ksbs = ksbs
        self.end_time = self.calculate_end_time()
        
    def calculate_end_time(self):
        end_datetime = datetime.combine(self.date, self.start_time) + timedelta(hours=self.duration)
        return end_datetime.time().strftime("%H:%M")
    
    def __str__(self):
        return (f"Date: {self.date.strftime('%Y-%m-%d')}, Start: {self.start_time.strftime('%H:%M')}, "
                f"Duration: {self.duration} hrs, Module: {self.module_names}, KSBs: {', '.join(self.ksbs)}, "
                f"Description: {self.description}, End: {self.end_time}")