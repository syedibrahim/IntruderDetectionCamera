# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'PASTE_ACCOUNT_SID_HERE'
auth_token = 'PASTE_AUTH_TOKEN_HERE'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Unkown person detected!! Alert!!!",
                     from_='PASTE_TWILIO_NUMBER_HERE',
                     to='PASTE_RECIEPIENT_NUMBER_HERE'
                 )

print(message.sid)
