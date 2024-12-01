# 🧱 CharCraft 🧱
### Open-Source, Tiny , Very Lite Minecraft 2D with Characters !

![image](https://github.com/user-attachments/assets/2e58dc13-5ac5-45d9-9ed8-3b376e2c7857)

> [!NOTE]
> The game control are for AZERTY keyboard, you can change your keyboard settings to an AZERTY so you can play it!

## Features :
- You can play with your friend Online !
- It's just a Python Code, You can execute it anywhere !
- Online ? Just host the server in you home with simple steps !
- Have Fun !

## How to run the game ?
1. Download the code `charcraft.py` from this Github Repo
2. Install Python3 in your system !
3. Open the terminal / cmd and then execute this command :
```
pip install keyboard requests
```
4. Then navigate to the Folder that contains the `charcraft.py` by doing :
```
cd folder/to/the/charcraft.py/file
```
4. Then you need to execute the code by doing :
```
sudo python3 charcraft_server.py
```
or (if it didn't work)
```
sudo python charcraft_server.py
```
> [!NOTE]
> `sudo` in Linux and MacOS is needed to run the code because the `keyboard` library must have the superuser access.

## GAME CONTROL KEYS

|     | Z |  E | 
|-----|---|----|
| Q   | S | D  |
- Z = Forward  
- S = Backward
- Q = Left     
- D = Right    
- E = Place a Block

## You want to play Online ?
- There Some IPs of a servers !
```
Comming Soon !
```
### If you to play online in your own server, This is a Step-by Step guide to show you how !
1. Download the code `charcraft_server.py` from this Github Repo
2. Install Python3 in your system !
3. Create a File called `config.json` at the same folder that contains the `charcraft_server.py`
4. Write this text into the `config.json` File:
```json
{
    "name":"NAME SERVER",
    "owner":"OWNER NAME",
    "desc":"THIS IS A DESCRIPTION",
    "port":5000,
    "size":[X,Y]
}
```
- You can modify the json like this example :
```json
{
    "name":"My Server",
    "owner":"DJOPRO_YT",
    "desc":"This is the best server ever",
    "port":5000,
    "size":[50,50]
}
```
5. Go to the directory that contains the `charcraft_server.py` File and then open the terminal/cmd at this folder
```
cd folder/to/the/charcraft_server.py/file
```
6. Then you need to execute the code by doing :
```
python3 charcraft_server.py
```
or (if it didn't work)
```
python charcraft_server.py
```
