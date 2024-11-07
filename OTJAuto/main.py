import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from tkinter import ttk
from services import ActivityService, MODULE_KSBS
from datetime import datetime, timedelta

class ActivityLoggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Activity Logger")

        self.service = ActivityService()

        self.title_label = tk.Label(root, text="Apprenticeship Activity Logger", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.add_activity_button = tk.Button(root, text="Add Activity", command=self.add_activity)
        self.add_activity_button.pack(pady=5)

        self.list_activities_button = tk.Button(root, text="List Activities", command=self.list_activities)
        self.list_activities_button.pack(pady=5)

        self.generate_report_button = tk.Button(root, text="Generate Report", command=self.generate_report)
        self.generate_report_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(pady=5)

    def add_activity(self):
        date_window = tk.Toplevel(self.root)
        date_window.title("Select Date(s)")
        date_window.geometry("400x400") 

        tk.Label(date_window, text="Select one or more dates for activities:").pack(pady=5)

        calendar = Calendar(date_window, selectmode='day', year=2024, month=1, day=1)
        calendar.pack(pady=10, padx=10, expand=True, fill=tk.BOTH) 

        selected_dates = [] 

        def date_click(event):
            selected_date = calendar.get_date() 
            selected_date_obj = datetime.strptime(selected_date, "%m/%d/%y").date() 
            if selected_date_obj not in selected_dates:
                selected_dates.append(selected_date_obj)
                calendar.calevent_create(selected_date_obj, selected_date_obj, 'selected')  
            else:
                selected_dates.remove(selected_date_obj)
                calendar.calevent_remove(selected_date_obj)  
            print("Selected Dates:", selected_dates)

        calendar.bind("<<CalendarSelected>>", date_click) 

        def apply_dates():
            if not selected_dates:
                messagebox.showwarning("No Date Selected", "Please select at least one date.")
                return

            date_window.destroy()
            self.enter_activity_details(selected_dates)

        apply_button = tk.Button(date_window, text="Apply", command=apply_dates)
        apply_button.pack(pady=10)

    def enter_activity_details(self, selected_dates):
        self.selected_dates = selected_dates
        self.current_index = 0  
        self.prompt_for_activity_details(self.selected_dates[self.current_index])

    def prompt_for_activity_details(self, activity_date):
        activity_window = tk.Toplevel(self.root)
        activity_window.title(f"Activity on {activity_date.strftime('%A, %d-%m-%Y')}")
        tk.Label(activity_window, text=f"Enter start time for {activity_date.strftime('%A, %d-%m-%Y')}:").pack(pady=5)
        
        time_frame = tk.Frame(activity_window)
        time_frame.pack(pady=5)
        hours = [f"{i:02d}" for i in range(24)] 
        minutes = [f"{i:02d}" for i in range(0, 60, 5)]  

        hour_combobox = ttk.Combobox(time_frame, values=hours, width=5)
        minute_combobox = ttk.Combobox(time_frame, values=minutes, width=5)
        hour_combobox.set("09") 
        minute_combobox.set("00")  
        hour_combobox.pack(side=tk.LEFT, padx=5)
        minute_combobox.pack(side=tk.LEFT, padx=5)

        tk.Label(activity_window, text="Enter duration (in hours):").pack(pady=5)
        duration_entry = tk.Entry(activity_window)
        duration_entry.pack(pady=5)

        tk.Label(activity_window, text="Enter description:").pack(pady=5)
        description_text = tk.Text(activity_window, height=5, width=40)  
        description_text.pack(pady=5)

        tk.Label(activity_window, text="Choose modules:").pack(pady=5)

        self.module_checkbuttons = {}
        for module in MODULE_KSBS.keys():
            var = tk.BooleanVar()
            checkbutton = tk.Checkbutton(activity_window, text=module, variable=var)
            checkbutton.pack(anchor="w")
            self.module_checkbuttons[module] = var

        def submit_activity():
            start_time = f"{hour_combobox.get()}:{minute_combobox.get()}"
            duration = int(duration_entry.get())
            description = description_text.get("1.0", "end-1c") 
            
            selected_modules = [module for module, var in self.module_checkbuttons.items() if var.get()] 

            start_date_formatted = activity_date.strftime('%Y-%m-%d')  
            
            self.service.add_activity(start_date_formatted, start_time, duration, description, selected_modules)
            activity_window.destroy()

            self.current_index += 1
            if self.current_index < len(self.selected_dates):
                next_date = self.selected_dates[self.current_index]
                self.prompt_for_activity_details(next_date)

        submit_button = tk.Button(activity_window, text="Submit Activity", command=submit_activity)
        submit_button.pack(pady=10)

    def list_activities(self):
        activities = self.service.activities
        if not activities:
            messagebox.showinfo("No Activities", "No activities to display.")
            return
        
        list_window = tk.Toplevel(self.root)
        list_window.title("Activities List")

        for activity in activities:
            tk.Label(list_window, text=str(activity)).pack(pady=5)

    def generate_report(self):
        self.service.generate_report()
        messagebox.showinfo("Report Generated", "The report has been generated successfully!")

def main():
    root = tk.Tk()
    app = ActivityLoggerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()