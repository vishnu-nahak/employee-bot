from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk import Action
from rasa_sdk.events import (SlotSet,AllSlotsReset)
import requests as reqs 
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime
from datetime import date
import re
import pytest
from datetime import time, date, timedelta, datetime
from dateutil import parser
from dateutil.tz import tzlocal
from rasa_sdk.events import Restarted


class EmployeeDetailsForm(FormAction):
    def name(self):
        return "employee_details_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["employeeid"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return { "employeeid":[self.from_text()] }
    @staticmethod
    def sample_flight_platform_for_booking_tickets() -> List[Text]:
        """ Database of Supported Station"""
        return ["EMP 001","EMP 002","EMP 003","EMP 004","EMP 005","EMP 006"]
    def validate_employeeid(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:
        if value in self.sample_flight_platform_for_booking_tickets():
            return {'employeeid': value}
        else:
            dispatcher.utter_message(template="utter_wrong_input_for_platform_response")
            return{'employeeid': None}

    def submit(self,dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(template="utter_employee_id_confirmation")
        return[]         

class EmployeeFirstName(Action):
    """This class is for checking Employee First Name"""

    def name(self):
        return "action_employee_firstname"

    def run(self, dispatcher, tracker, domain):
        print("action_employee_firstname is running inside class EmployeeFirstName")
        try:
            EmployeeID = str(tracker.get_slot('employeeid'))
            print("Inside action_employee_firstname Employee ID is: ", EmployeeID)

            url = 'http://localhost:3000/employees'

            response = reqs.get(url)  

            input = EmployeeID
            EmployeeFirstName = ""
            if response.status_code != 200:
                print("Response Status Code Error: ",response.status_code)
            else:
                json_data = response.json()
                for each in json_data:
                    if str(each['id']) == input:
                        EmployeeFirstName = str(each["first_name"])   
                        print("Employee first name is ", EmployeeFirstName) 

            dispatcher.utter_template(
                "utter_employee_firstname_template", tracker, variableforemployeefirstname=EmployeeFirstName
            )
            print(
                "utter_employee_firstname_template template is working successfully through which we are executing variableforemployeefirstname from actions.py file."
            )

        except Exception as e:
            dispatcher.utter_message("No data is available")
            print("Exception: ",e)
        return []

class EmployeeLastName(Action):
    """This class is for checking Employee Last Name"""

    def name(self):
        return "action_employee_lastname"

    def run(self, dispatcher, tracker, domain):
        print("action_employee_lastname is running inside class EmployeeLastName")
        try:
            EmployeeID = str(tracker.get_slot('employeeid'))
            print("Inside action_employee_firstname Employee ID is: ", EmployeeID)

            url = 'http://localhost:3000/employees'

            response = reqs.get(url)  

            input = EmployeeID
            EmployeeLastName = ""
            if response.status_code != 200:
                print("Response Status Code Error: ",response.status_code)
            else:
                json_data = response.json()
                for each in json_data:
                    if str(each['id']) == input:
                        EmployeeLastName = str(each["last_name"])   
                        print("Employee last name is ", EmployeeLastName) 

            dispatcher.utter_template(
                "utter_employee_lastname_template", tracker, variableforemployeelastname=EmployeeLastName
            )
            print(
                "utter_employee_lastname_template template is working successfully through which we are executing variableforemployeelastname from actions.py file."
            )

        except Exception as e:
            dispatcher.utter_message("No data is available")
            print("Exception: ",e)
        return []        

class EmployeeDesignation(Action):
    """This class is for checking Employee Designation"""

    def name(self):
        return "action_employee_designation"

    def run(self, dispatcher, tracker, domain):
        print("action_employee_designation is running inside class EmployeeDesignation")
        try:
            EmployeeID = str(tracker.get_slot('employeeid'))
            print("Inside action_employee_designation Employee ID is: ", EmployeeID)

            url = 'http://localhost:3000/employees'

            response = reqs.get(url)  

            input = EmployeeID
            EmployeeDesignation = ""
            if response.status_code != 200:
                print("Response Status Code Error: ",response.status_code)
            else:
                json_data = response.json()
                for each in json_data:
                    if str(each['id']) == input:
                        EmployeeDesignation = str(each["designation"])
                        print("Employee designation is ", EmployeeDesignation) 

            dispatcher.utter_template(
                "utter_employee_designation_template", tracker, variableforemployeedesignation=EmployeeDesignation
                
            )
            print(
                "utter_employee_designation_template template is working successfully through which we are executing variableforemployeedesignation from actions.py file."
            )

        except Exception as e:
            dispatcher.utter_message("No data is available")
            print("Exception: ",e)
        return []        

class EmployeeEmailID(Action):
    """This class is for checking Employee EmailID"""

    def name(self):
        return "action_employee_emailid"

    def run(self, dispatcher, tracker, domain):
        print("action_employee_emailid is running inside class EmployeeEmailID")
        try:
            EmployeeID = str(tracker.get_slot('employeeid'))
            print("Inside action_employee_emailid Employee ID is: ", EmployeeID)

            url = 'http://localhost:3000/employees'

            response = reqs.get(url)  

            input = EmployeeID
            EmployeeEmailID = ""
            if response.status_code != 200:
                print("Response Status Code Error: ",response.status_code)
            else:
                json_data = response.json()
                for each in json_data:
                    if str(each['id']) == input:
                        EmployeeEmailID = str(each["email_id"])
                        print("Employee email id is ", EmployeeEmailID) 

            dispatcher.utter_template(
                "utter_employee_emailid_template", tracker, variableforemployeeemailid=EmployeeEmailID
                
            )
            print(
                "utter_employee_emailid_template template is working successfully through which we are executing variableforemployeeemailid from actions.py file."
            )

        except Exception as e:
            dispatcher.utter_message("No data is available")
            print("Exception: ",e)
        return []     

class EmployeeDOB(Action):
    """This class is for checking Employee DOB"""

    def name(self):
        return "action_employee_dob"

    def run(self, dispatcher, tracker, domain):
        print("action_employee_dob is running inside class EmployeeDOB")
        try:
            EmployeeID = str(tracker.get_slot('employeeid'))
            print("Inside action_employee_dob Employee ID is: ", EmployeeID)

            url = 'http://localhost:3000/employees'

            response = reqs.get(url)  

            input = EmployeeID
            EmployeeDOB = ""
            if response.status_code != 200:
                print("Response Status Code Error: ",response.status_code)
            else:
                json_data = response.json()
                for each in json_data:
                    if str(each['id']) == input:
                        EmployeeDOB = str(each["dob"])
                        print("Employee date of birth is ", EmployeeDOB) 

            dispatcher.utter_template(
                "utter_employee_dob_template", tracker, variableforemployeedob=EmployeeDOB
                
            )
            print(
                "utter_employee_dob_template template is working successfully through which we are executing variableforemployeedob from actions.py file."
            )

        except Exception as e:
            dispatcher.utter_message("No data is available")
            print("Exception: ",e)
        return []             


class EmployeeIdEntity(Action):
    def name(self):
        return 'action_employee_id_designation'
    def run(self, dispatcher, tracker, domain):
        print("EmployeeIdEntity")
        employeeidentity = (next(tracker.get_latest_entity_values("empid"), None))
        # employeeidentity = str(employeeidentity).upper()
        print("Employee ID from entity extraction: ",employeeidentity)    

        if employeeidentity is None:    
            dispatcher.utter_template("utter_ask_employeeid",tracker)
        else:
            try:
                print("Inside action_employee_designation Employee ID is: ", employeeidentity)
                url = 'http://localhost:3000/employees'
                response = reqs.get(url) 
                input = employeeidentity
                EmployeeDesignation = ""
                if response.status_code != 200:
                    print("Response Status Code Error: ",response.status_code)
                else:
                    json_data = response.json()
                    for each in json_data:
                        if str(each['id']) == input:
                            EmployeeDesignation = str(each["designation"])
                            print("Employee designation is ", EmployeeDesignation) 
                dispatcher.utter_template("utter_employee_designation_template", tracker, variableforemployeedesignation=EmployeeDesignation)
                print("utter_employee_designation_template template is working successfully through which we are executing variableforemployeedesignation from actions.py file.")
            except Exception as e:
                dispatcher.utter_message("No data is available")
                print("Exception: ",e)
                dispatcher.utter_template("utter_ask_employeeid",tracker)
        return []
        # return [SlotSet("employeeid",None)]

class EmployeeIdEntityFirstName(Action):
    def name(self):
        return 'action_employee_id_firstname'
    def run(self, dispatcher, tracker, domain):
        print("EmployeeIdEntity")
        employeeidentity = (next(tracker.get_latest_entity_values("empid"), None))
        # employeeidentity = str(employeeidentity).upper()
        print("Employee ID from entity extraction: ",employeeidentity)    

        if employeeidentity is None:    
            dispatcher.utter_template("utter_ask_employeeid",tracker)
        else:
            try:
                print("Inside action_employee_id_entity_firstname Employee ID is: ", employeeidentity)
                url = 'http://localhost:3000/employees'
                response = reqs.get(url)  
                input = employeeidentity
                EmployeeFirstName = ""
                if response.status_code != 200:
                    print("Response Status Code Error: ",response.status_code)
                else:
                    json_data = response.json()
                    for each in json_data:
                        if str(each['id']) == input:
                            EmployeeFirstName = str(each["first_name"])
                            print("Employee firstname is ", EmployeeFirstName) 
                dispatcher.utter_template("utter_employee_firstname_template", tracker, variableforemployeefirstname=EmployeeFirstName)
                print("utter_employee_firstname_template template is working successfully through which we are executing variableforemployeefirstname from actions.py file.")
            except Exception as e:
                dispatcher.utter_message("No data is available")
                print("Exception: ",e)
                dispatcher.utter_template("utter_ask_employeeid",tracker)
        return []
        # return [SlotSet("employeeid",None)]


class EmployeeIdEntityLastName(Action):
    def name(self):
        return 'action_employee_id_lastname'
    def run(self, dispatcher, tracker, domain):
        print("EmployeeIdEntity")
        employeeidentity = (next(tracker.get_latest_entity_values("empid"), None))
        # employeeidentity = str(employeeidentity).upper()
        print("Employee ID from entity extraction: ",employeeidentity)    

        if employeeidentity is None:    
            dispatcher.utter_template("utter_ask_employeeid",tracker)
        else:
            try:
                print("Inside action_employee_id_lastname Employee ID is: ", employeeidentity)
                url = 'http://localhost:3000/employees'
                response = reqs.get(url)  
                input = employeeidentity
                EmployeeLastName = ""
                if response.status_code != 200:
                    print("Response Status Code Error: ",response.status_code)
                else:
                    json_data = response.json()
                    for each in json_data:
                        if str(each['id']) == input:
                            EmployeeLastName = str(each["last_name"])
                            print("Employee lastname is ", EmployeeLastName) 
                dispatcher.utter_template("utter_employee_lastname_template", tracker, variableforemployeelastname=EmployeeLastName)
                print("utter_employee_lastname_template template is working successfully through which we are executing variableforemployeelastname from actions.py file.")
            except Exception as e:
                dispatcher.utter_message("No data is available")
                print("Exception: ",e)
                dispatcher.utter_template("utter_ask_employeeid",tracker)
        return []
        # return [SlotSet("employeeid",None)]

class EmployeeIdEntityEmailId(Action):
    def name(self):
        return 'action_employee_id_emailid'
    def run(self, dispatcher, tracker, domain):
        print("EmployeeIdEntity")
        employeeidentity = (next(tracker.get_latest_entity_values("empid"), None))
        # employeeidentity = str(employeeidentity).upper()
        print("Employee ID from entity extraction: ",employeeidentity)    

        if employeeidentity is None:    
            dispatcher.utter_template("utter_ask_employeeid",tracker)
        else:
            try:
                print("Inside action_employee_id_emailid Employee ID is: ", employeeidentity)
                url = 'http://localhost:3000/employees'
                response = reqs.get(url)  
                input = employeeidentity
                EmployeeEmailId = ""
                if response.status_code != 200:
                    print("Response Status Code Error: ",response.status_code)
                else:
                    json_data = response.json()
                    for each in json_data:
                        if str(each['id']) == input:
                            EmployeeEmailId = str(each["email_id"])
                            print("Employee email id is ", EmployeeEmailId) 
                dispatcher.utter_template("utter_employee_emailid_template", tracker, variableforemployeeemailid=EmployeeEmailId)
                print("utter_employee_emailid_template template is working successfully through which we are executing variableforemployeeemailid from actions.py file.")
            except Exception as e:
                dispatcher.utter_message("No data is available")
                print("Exception: ",e)
                dispatcher.utter_template("utter_ask_employeeid",tracker)
        return []
        # return [SlotSet("employeeid",None)]        

class EmployeeIdEntityDOB(Action):
    def name(self):
        return 'action_employee_id_dob'
    def run(self, dispatcher, tracker, domain):
        print("EmployeeIdEntity")
        employeeidentity = (next(tracker.get_latest_entity_values("empid"), None))
        # employeeidentity = str(employeeidentity).upper()
        print("Employee ID from entity extraction: ",employeeidentity)    

        if employeeidentity is None:    
            dispatcher.utter_template("utter_ask_employeeid",tracker)
        else:
            try:
                print("Inside action_employee_id_dob Employee ID is: ", employeeidentity)
                url = 'http://localhost:3000/employees'
                response = reqs.get(url)
                input = employeeidentity
                EmployeeDOB = ""
                if response.status_code != 200:
                    print("Response Status Code Error: ",response.status_code)
                else:
                    json_data = response.json()
                    for each in json_data:
                        if str(each['id']) == input:
                            EmployeeDOB = str(each["dob"])
                            print("Employee date of birth id is ", EmployeeDOB) 
                dispatcher.utter_template("utter_employee_dob_template", tracker, variableforemployeedob=EmployeeDOB)
                print("utter_employee_dob_template template is working successfully through which we are executing variableforemployeedob from actions.py file.")
            except Exception as e:
                dispatcher.utter_message("No data is available")
                print("Exception: ",e)
                dispatcher.utter_template("utter_ask_employeeid",tracker)
        return []
        # return [SlotSet("employeeid",None)]        