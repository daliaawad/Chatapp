# Python Chat Program

This is a multi-client chat program implemented in Python, utilizing multithreading for handling multiple simultaneous clients. The program enables clients to connect to a server and communicate with each other in various ways. The server supports functionalities such as individual messaging, broadcast messaging, group creation and joining, and file sharing. Each client is assigned a unique ID upon connecting to the server, allowing the server to maintain a list of all connected clients.

## Features

- *Multiple Simultaneous Clients*: The server can handle multiple clients connecting simultaneously, facilitating concurrent communication among them.

- *List of Connected Clients*: Clients can request a list of all other connected clients from the server, enabling them to see who else is currently online.

- *Individual Messaging*: Clients can send messages to specific individual clients by specifying the recipient's ID, ensuring private conversations.

- *Broadcast Messaging*: Clients can send messages that are broadcasted to all online clients, enabling global announcements or public discussions.

- *Group Functionality*: Clients can create and join groups tracked by the server. Messages sent to a group are delivered to all clients within that group, fostering collaborative conversations.

- *File Sharing*: Clients have the capability to send files to other clients, allowing the exchange of documents, images, or any other file type.
