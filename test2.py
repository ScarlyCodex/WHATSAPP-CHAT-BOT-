from twilio.rest import Client

account_sid = 'AC32f6bcd8852a5135fb1df7a67c97d80a'
auth_token = '787e57aabf74d21ffaea675a17ec3517'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  to='whatsapp:+5215548737138'
)

print(message.sid)