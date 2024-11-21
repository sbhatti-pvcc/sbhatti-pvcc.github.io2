## overview
Our proposed project is software that can generate a random string, or "key", encrypt a given message using that key, and decrypt a message given a key and the message encoded with that key.
The problem that our project adresses is one of security. Encryption allows you to make the viewing of certain pieces of data conditional on having both the data and a key, which is an essential piece of technology in scenarios where the interception of messages is a posibility. 
## Analysis
## Algorithm
prompt: do you want to decode or encode a message?

if(decode):

 prompt:what is your message?
 message = input

 prompt:what is your key?

 key = input

 message = decodingAlgorithm(message,key)

 print(message)

else if (encode):

 prompt:what message do you want to decode?

 message = input

 key = generateKey()

 print("your key is" + key)

 encodedMessage = encodingAlgorithm(message,key)

 print("your encoded message is" + encodedMessage)
 
