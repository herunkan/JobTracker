import datetime
from enum import Enum
import sys

class ApplicationStatus(Enum):
    APPLIED = "Applied"
    OA = "OA"
    INTERVIEW = "Interview"
    FINAL_ROUND = "Final Round"
    REJECTED = "Rejected"
    OFFER = "Offer"
    
class JobApplication:
    def __init__(self,
                 company:str,
                 role:str,
                 status:ApplicationStatus = ApplicationStatus.APPLIED,
                 apply_date:datetime.date|None = None,
                 job_url:str|None = None,
                 location:str|None = None,
                 pay:str|None = None,
                 job_description:str|None = None
                 ) -> None:
        
        if apply_date is None:
            self.apply_date = datetime.date.today()
        else:    
            self.apply_date = apply_date
        
        self.company = company
        self.role = role
        self.status = status
        self.job_url = job_url
        self.location = location
        self.pay = pay
        self.job_description = job_description
    
    def __str__(self) -> str:
        return f"Applied to {self.role} at {self.company} on {self.apply_date}"
    
    def details(self) -> None:
        print(f"""company: {self.company}
              role: {self.role}
              status: {self.status.value}
              application-date: {self.apply_date}
              job_url: {self.job_url}
              location: {self.location}
              pay: {self.pay}
              job_description: {self.job_description}
              """
              )

applications = []

def track_job():
    print("Please type in your application details!")
    company = input("Company: ")
    role = input("Role: ")
    statuses = list(ApplicationStatus)
    while True:
        try:
            status_num = int(input("""Choose Status based on number:
                                   
                            1. Applied
                            2. OA
                            3. Interview
                            4. Final Round
                            5. Rejected
                            6. Offer
                            
                            Enter number: """
                            )) - 1
            if 0<= status_num < len(statuses):
                break
            print(f"Number has to be between 1 to {len(statuses)}\n")
        
        except ValueError:
            print("Choose a number, not text\n")
            
    status = statuses[status_num]        
    job_url = input("Job URL (optional): ") or None
    location = input("Location (optional): ") or None
    pay = input("Pay (optional): ") or None
    job_description = input("Job Description (optional): ") or None
        
    
    job = JobApplication(company= company, 
                            role= role, 
                            status= status, 
                            job_url= job_url, 
                            location= location,
                            pay= pay,
                            job_description= job_description) 
    
    applications.append(job)
    
    print("Application Saved!\n")

def view_job():
    if not applications:
        print("There is no applications yet, add some now!\n")
        return
    
    for i, job in enumerate(applications, start=1):
        print(f"{i}, {job}")
    
    while True:
        try:
            job_num = int(input("Which job would you like to see? Type in the corresponding number to view the job.")) - 1
            
            if 0 <= job_num <len(applications):
                break
            
            print("choose a numeber from the list\n")
        except ValueError:
            print("Please choose a number\n")
            
    applications[job_num].details()



def main():
    while True:
        try:
            action = int(input("""Welcome to the Job Application Tracker!
                What can I do for you today?
                
                1. Add application
                2. View applications
                3. Exit
                
                Choose a number: \n"""
            ))
            
            if action == 1: 
                track_job()
            elif action == 2:
                view_job()
            elif action == 3:
                print("Goodbye!")
                sys.exit()
            else:    
                print("Choose a number between 1 and 3\n")
            
        except ValueError:
            print("Choose a number, not text\n")
    

main()