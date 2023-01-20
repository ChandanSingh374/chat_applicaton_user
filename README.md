# Chat Server

This is a simple chat server that allows clients to connect, register their name, and send and receive messages.

### Requirements

- Python 3.7 or later
- websockets (can be installed via pip)

### Running the server

1. Clone the repository or download the source code
2. Open a terminal and navigate to the directory where the code is located
3. Run the command `pip install websockets` to install the required dependency
4. Run the command `python3 chat_server.py` to start the server
5. The server will be listening on `localhost:6789`

### Connecting to the server

Clients can connect to the server using a WebSocket library in their preferred language. Once connected, the client should send a message with the following format to register their name:
```
    {
        "type": "register_name",
        "message": "client_name"
    }
```


After registering their name, clients can send and receive messages.

- To send a broadcast message:
```
    {
        "type": "broadcast_message",
        "message": "Hello, World!"
    }
```



- To send a private message:
```
    {
        "type": "private_message",
        "recipient": "recipient_name",
        "message": "Hello, recipient!"
    }
```



- To get the list of online clients:
```
    {
        "type": "online_clients_query"
    }
```



- To get online clients list as response:
```
    {
        "type": "online_clients_response",
        "clients": ["client1", "client2"]
    }
```

The server will broadcast messages when a client joins or leaves the chat.