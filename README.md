# employee-bot
# rasa-employee-bot


Hi Please follow the below steps to run rasa-employee-bot in your local system.

Step 1: Please open your visual studio code

Step 2: Please open terminal in visual studio (Hint: Right click on Terminal and click on New Terminal)

Step 3: Please change your folder directory where you have save this project file.

        Ex: cd C:\Users\vishnu\Desktop\rasa-employee-bot
            C:\Users\vishnu\Desktop\rasa-employee-bot

Step 4: Please train rasa-employee-bot in your terminal using below command

        rasa train
        Ex: C:\Users\vishnu\Desktop\rasa-employee-bot>rasa train

Step 5: Please open new terminal to run the json server in your local system.        
        (Hint: Right click on Terminal and click on New Terminal)

Step 6: Please run the json server using below command

        json-server --watch db.json
        Ex: C:\Users\vishnu\Desktop\rasa-employee-bot>json-server --watch db.json


Step 7: Please open new terminal to run the rasa actions.py in your local system.        
        (Hint: Right click on Terminal and click on New Terminal)

Step 8: Please run the rasa actions.py using below command

        rasa run actions --port 5055
        Ex: C:\Users\vishnu\Desktop\rasa-employee-bot>rasa run actions --port 5055


Step 9: Please open new terminal to start ngrok endpoint in your local system.        
        (Hint: Right click on Terminal and click on New Terminal)

Step 10: Please start the ngrok endpoint using below command

        ngrok http 5005
        Ex: C:\Users\vishnu\Desktop\rasa-employee-bot>ngrok http 5005

Step 11: Please open new terminal to run the rasa-employee-bot using ngrok endpoint in your local system.        
        (Hint: Right click on Terminal and click on New Terminal)

Step 12: Please run the rasa-employee-bot using ngrok endpoint using below command

        rasa run --port 5005
        Ex: C:\Users\vishnu\Desktop\rasa-employee-bot>rasa run --port 5005



## Getting twilio Credentials
You first have to create a Twilio app to get credentials. Once you have them you can add these to your credentials.yml.

## How to get the Twilio credentials: 
You need to set up a Twilio account.

Once you have created a Twilio account, you need to create a new project. The basic important product to select here is Programmable SMS.

Once you have created the project, navigate to the Dashboard of Programmable SMS and click on Get Started. Follow the steps to connect a phone number to the project.

Now you can use the Account SID, Auth Token, and the phone number you purchased in your credentials.yml.


## Connecting to WhatsApp
You can deploy a Rasa Open Source assistant to WhatsApp through Twilio. However, to do so, you have to have a WhatsApp Business profile. Associate your Whatsapp Business profile with the phone number you purchased through Twilio to access the Twilio API for WhatsApp.

According to the Twilio API documentation, the phone number you use should be prefixed with whatsapp: in the credentials.yml described below.


## Applying the Credentials
Add the Twilio credentials to your credentials.yml:


twilio:

  account_sid: "ACe83c9eabd049496c6131a51dfe354414"
  
  auth_token: "c5062e9635879b0caa7decebb1939599"
  
  twilio_number: "whatsapp:+14155238886"  # if using WhatsApp: "whatsapp:+440123456789"


## Twilio Sandbox for WhatsApp  

Step 1: After login to twilio account click on Console Dashboard

Step 2: Click on All Product & Services (...)

Step 3: Click on Programmable SMS

Step 4: Click on WhatApp

Step 5: Click on Sandbox

Step 6: You need copy your ngrok endpoit and paste it into Sandbox Configuration

Ex:
## Twilio Sandbox for WhatsApp
## Sandbox Configuration
To send and receive messages from the Sandbox to your Application, configure your endpoint URLs. 

                            __________________________________________________________________________________
WHEN A MESSAGE COMES IN    |     https://a383dab7.ngrok.io/webhooks/twilio/webhook/       |    HTTP Post    v |
                            -----------------------------------------------------------------------------------

Step 7: Click on Save 




## # ############################# To run the rasa-employee-bot without WhatsApp channel
# rasa train
# json-server --watch db.json (Start json server)
# rasa run actions --port 5055 (Start Rasa action)
# rasa run -m models --enable-api --cors "*" --debug (Start the employee bot)


## # #################################  To run the rasa-employee-bot with WhatsApp channel
# rasa train
# json-server --watch db.json (Start json server)
# rasa run actions --port 5055 (Start Rasa action)
# ngrok http 5005
# rasa run --port 5005

                                                        Thank-You
