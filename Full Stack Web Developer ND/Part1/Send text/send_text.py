from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC896ae38d11b5134395a03cf328a3b11d"
auth_token = "272b683ef911d6487e52a611b3dfb8f7"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
	body="My name is Nan MENG ?",
	to="+85255175498",          # Replace with your phone number
	from_="+12053584196 ")      # Replace with your Twilio number
print message.sid