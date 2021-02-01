### <u> Setting up </u>

**Step 1.** Connect to K-State VPN  

**Step 2.** Install Terminal emulator and SFTP client  
    Windows: MobaXterm or Cyberduck   
    macOS: Cyberduck  
    
**Step 3.** Connect to IMSE servers  
    In terminal type "ssh krishwera@ServerIP" and password  
    Open Cyberduck, selct SFTP (SSH File Transfer Protocol) and fill in ServerIP and password  
    now server is ready and Cyberduck lets you transfer files with local machine and server.  
    
**Step 4.** [HUE](https://gethue.com/the-hue-4-user-interface-in-detail/) login  
    Go to http://serverIP:8888  
    Set up an account and remember to check "Create home directory"
    
#### A2

1. Transfer basket.txt to server from local machine via Cyberduck.  
2. put it in HDFS  
`hadoop fs -put /home/krishwera/basket.txt /user/krishwera`
3. Use a hadoop command to examine file content outside the HDFS.  
`hadoop fs -cat file:///home/krishwera/basket.txt.`
4. Make a directory called inputfiles in HDFS  
`hadoop fs -mkdir /user/krishwera/inputfiles`
5. In in HDFS, move the basket.txt to inputfiles directory  
`hadoop fs -mv /user/krishwera/basket.txt /user/krishwera/inputfiles`





    
    
    
    
    
