from django.http import HttpResponse
from channels.handler import AsgiHandler

def ws_message(message):
	message.reply_channel.send({
		"text":message.content["text"],
		})

# def http_consumer(message):
# 	response=HttpResponse("Hello!! You asked for %s" % message.content['path'])
# 	# Encode that response into message format (ASGI)
# 	for chunk in AsgiHandler.encode_response(response):
# 		message.reply_channel.send(chunk)




 