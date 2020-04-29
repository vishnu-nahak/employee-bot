## happy path
* greet
  - utter_greet_response
* mood_great
  - utter_happy_response
## sad path 1
* greet
  - utter_greet_response
* mood_unhappy
  - utter_cheer_up_response
  - utter_did_that_help_response
* affirm
  - utter_happy_response
## sad path 2
* greet
  - utter_greet_response
* mood_unhappy
  - utter_cheer_up_response
  - utter_did_that_help_response
* deny
  - utter_goodbye_response
## say goodbye
* goodbye
  - utter_goodbye_response
## bot challenge
* bot_challenge
  - utter_iamabot_response

## interactive_story_1
* greet
    - utter_greet_response
* employee_firstname
    - utter_employee_firstname
    - employee_details_form
    - form{"name": "employee_details_form"}
    - slot{"requested_slot": "employeeid"}
* form: empid
    - form: employee_details_form
    - slot{"employeeid": "EMP 001"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_employee_firstname
* employee_designation
    - action_employee_designation
* employee_lastname
    - action_employee_lastname               
* employee_emailid
    - action_employee_emailid        
* employee_dob
    - action_employee_dob       


## interactive_story_2
* greet
    - utter_greet_response
* employee_id
    - utter_employee_firstname
    - employee_details_form
    - form{"name": "employee_details_form"}
    - slot{"requested_slot": "employeeid"}
* form: empid
    - form: employee_details_form
    - slot{"employeeid": "EMP 001"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_employee_designation
* employee_firstname
    - action_employee_firstname              
* employee_lastname
    - action_employee_lastname               
* employee_emailid
    - action_employee_emailid        
* employee_dob
    - action_employee_dob         
    
## interactive_story_1
* employee_id_designation{"empid": "EMP 001"}
    - action_employee_id_designation
* employee_id_designation{"empid": "EMP 005"}
    - action_employee_id_designation


## interactive_firstname_story_1
* employee_id_firstname{"empid": "EMP 001"}
    - action_employee_id_firstname
* employee_id_firstname{"empid": "EMP 005"}
    - action_employee_id_firstname

## interactive_lastname_story_1
* employee_id_lastname{"empid": "EMP 001"}
    - action_employee_id_lastname
* employee_id_lastname{"empid": "EMP 005"}
    - action_employee_id_lastname

## interactive_emailid_story_1
* employee_id_emailid{"empid": "EMP 001"}
    - action_employee_id_emailid
* employee_id_emailid{"empid": "EMP 005"}
    - action_employee_id_emailid

## interactive_dob_story_1
* employee_id_dob{"empid": "EMP 001"}
    - action_employee_id_dob
* employee_id_dob{"empid": "EMP 005"}
    - action_employee_id_dob
