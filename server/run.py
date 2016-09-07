from server.server import Server
from common.command import Command

from server.handlers import handler_map, check_state
from server.handlers import unknown_handler, invalid_handler

def handle_message(serv, usr, data):
	try:
		msg = Command(data)
		(state, handler) = handler_map[msg.command]
		if check_state(serv, usr, state):
			handler(serv, usr, *msg.arguments)

	except KeyError:
		unknown_handler(serv, usr, msg.command)

	except TypeError:
		invalid_handler(serv, usr, msg.command)

serv = Server()
serv.start('127.0.0.1', 7000, lambda usr, data:
	handle_message(serv, usr, data)
)
