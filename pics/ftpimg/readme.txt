I recently run into this question in my work place so I think I should say something more here. I will use image to explain how the FTP works as an additional source for previous answer.

Active mode:

<act.png>

.....................................................................................................................

Passive mode:

<passv.png>

.....................................................................................................................

In an active mode configuration, the server will attempt to connect to a random client-side port. So chances are, that port wouldn't be one of those predefined ports. As a result, an attempt to connect to it will be blocked by the firewall and no connection will be established.

<fwall.png>

.....................................................................................................................

A passive configuration will not have this problem since the client will be the one initiating the connection. Of course, it's possible for the server side to have a firewall too. However, since the server is expected to receive a greater number of connection requests compared to a client, then it would be but logical for the server admin to adapt to the situation and open up a selection of ports to satisfy passive mode configurations.

So it would be best for you to configure server to support passive mode FTP. However, passive mode would make your system vulnerable to attacks because clients are supposed to connect to random server ports. Thus, to support this mode, not only should your server have to have multiple ports available, your firewall should also allow connections to all those ports to pass through!

To mitigate the risks, a good solution would be to specify a range of ports on your server and then to allow only that range of ports on your firewall.

For more information, please read the official document.