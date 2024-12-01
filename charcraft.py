import keyboard as k
import requests
import json
import os
import time 
import random
import sys

debug = False
last_y = 0
last_x = 0
pos_x = 0
pos_y = 0
id_plr = random.randint(10000000000,999999999999)
char_plr = "(._.)"
def cursor_off():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def normal_game():
    global pos_x
    global pos_y
    global x
    global y
    global last_x
    global last_y
    global debug
    global char_plr
    cursor_off()
    clear()
    print("Loading ...")
    print(f"SCREEN-SIZE:{x}x{y}")

    blocks = []
    
    pos_y = int(y/2)
    pos_x = int(x/2)

    time.sleep(1)
    clear()
    upd_plr()
    
    while True:
        

        if k.is_pressed("z"):
            move = True
            for i in blocks:
                if i[0] == pos_x and i[1] == pos_y - 1:
                    move = False
                    break
                if i[1] == pos_y - 1 and pos_x < i[0] < pos_x + len(char_plr):
                    move = False
                    break

            if move and not pos_y <= 1:
                last_x = pos_x
                last_y = pos_y
                pos_y = pos_y - 1
                upd_plr()
        # while k.is_pressed("z"):
                time.sleep(0.1)
        elif k.is_pressed("s"):

            move = True
            for i in blocks:
                if i[0] == pos_x and i[1] == pos_y + 1:
                    move = False
                    break
                if i[1] == pos_y + 1 and pos_x < i[0] < pos_x + len(char_plr):
                    move = False
                    break

            if move and not pos_y >= y:
                last_x = pos_x
                last_y = pos_y
                pos_y = pos_y + 1
                upd_plr()
                time.sleep(0.1)
        elif k.is_pressed("q"):

            move = True
            for i in blocks:
                if i[0] == pos_x - 1 and i[1] == pos_y:
                    move = False
                    break
            if move and not pos_x <= 1:
                last_x = pos_x
                last_y = pos_y
                pos_x = pos_x - 1
                upd_plr()
                time.sleep(0.1)
        elif k.is_pressed("d"):
            move = True
            for i in blocks:
                if i[0] == pos_x + len(char_plr) and i[1] == pos_y:
                    move = False
                    break
            if move and not pos_x >= x:
                last_x = pos_x
                last_y = pos_y
                pos_x = pos_x + 1
                upd_plr()
                time.sleep(0.1)
        elif k.is_pressed("e"):
            move = True
            for i in blocks:
                if i[0] == pos_x + len(char_plr) and i[1] == pos_y:
                    move = False
                    break
            if move and not pos_x >= x:
                last_x = pos_x
                last_y = pos_y
                pos_x = pos_x + 1
                upd_plr()
                print(f"\033[{last_y};{last_x}H▢", end="", flush=True)
                blocks.append([last_x,last_y])
                while k.is_pressed("e"):
                    time.sleep(0.01)

def online_game(ip,data):
    global pos_x
    global pos_y
    global x
    global y
    global id_plr
    global debug
    global char_plr
    cursor_off()
    rq_i = requests.get(f"http://{ip}")
    if rq_i.ok:
        data_ = json.loads(rq_i.text)
        print(" > ---- INFO ABOUT THE SERVER ---- <")
        print(f"| Name : {data_['server_name']}")
        print(f"| Owner : {data_['owner']}")
        print(f"| Description : {data_['desc']}")
        print(f"| Size MAP : {data_['size'][0]}x{data_['size'][1]}")
        print(f"| Players : {data_['players']}")
        print(f"| Blocks : {data_['blocks']}")

    print(f"SCREEN-SIZE:{x}x{y}")

    blocks = json.loads(data)["blocks"]

    for b in blocks:
        print(f"\033[{b[0]};{b[1]}H▢", end="", flush=True)

    for plr in json.loads(data)["players"]:
        print(f"\033[{plr[1]};{plr[2]}H{plr[0]}", end="", flush=True)
    
    time.sleep(1)
    clear()
    
    while True:

        if k.is_pressed("z"):
                rq_m = requests.get(f"http://{ip}/change_pos/{id_plr}/forward")
                if rq_m.ok:
                    json_ = json.loads(rq_m.text)
                    pos_x = json_["x"]
                    pos_y = json_["y"]
                
                time.sleep(0.1)
        elif k.is_pressed("s"):

            rq_m = requests.get(f"http://{ip}/change_pos/{id_plr}/backward")
            if rq_m.ok:
                json_ = json.loads(rq_m.text)
                pos_x = json_["x"]
                pos_y = json_["y"]
                
            time.sleep(0.1)
        elif k.is_pressed("q"):

            rq_m = requests.get(f"http://{ip}/change_pos/{id_plr}/left")
            if rq_m.ok:
                json_ = json.loads(rq_m.text)
                pos_x = json_["x"]
                pos_y = json_["y"]
                
            time.sleep(0.1)
        elif k.is_pressed("d"):
            rq_m = requests.get(f"http://{ip}/change_pos/{id_plr}/right")
            if rq_m.ok:
                json_ = json.loads(rq_m.text)
                pos_x = json_["x"]
                pos_y = json_["y"]
                
            time.sleep(0.1)
        elif k.is_pressed("e"):
            rq_m = requests.get(f"http://{ip}/add_block/{id_plr}")
            if rq_m.ok:
                json_ = json.loads(rq_m.text)
                pos_x = json_["x"]
                pos_y = json_["y"]
                blocks = json_["blocks"]
                
            time.sleep(0.1)
        
        # REFRESHER
        r0 = requests.get(f"http://{ip}/refresh/{id_plr}")
        blocks = json.loads(r0.text)["blocks"]
        if r0.ok:
            clear()
            for b in blocks:
                print(f"\033[{b[1]};{b[0]}H▢", end="", flush=True)

            for plr in json.loads(r0.text)["players"]:
                print(f"\033[{plr[2]};{plr[1]}H{plr[0]}", end="", flush=True)
            
            upd_plr()
            
            time.sleep(0.25)



def typing_effect(text:str,delay:int):
    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(delay)

def logo():
    print("""
 ___                      ___                __
/     |     __    __     /       __    __   /  \\  _|_
|     |__  |__| |/  \\    |     |/  \\  |__| _|_     |
\\___  |  | |  | |        \\___  |      |  |  |      |  \n""")

    typing_effect("-- FULL OFFICIAL VERSION --\n\n",0.05)

def upd_plr():
    if debug:
        print(f"\033[{1};{1}H CURRENT-CHAR-POS: \n X:{pos_x} Y:{pos_y}", end="", flush=True)
        print(f"\033[{3};{1}H LAST-CHAR-POS: \n X:{last_x} Y:{last_y}", end="", flush=True)
    spaces = ""
    for i in range(len(char_plr)):
        spaces = spaces + " "
    print(f"\033[{last_y};{last_x}H{spaces}", end="", flush=True)
    print(f"\033[{pos_y};{pos_x}H{char_plr}", end="", flush=True)

x,y = os.get_terminal_size()
def clear():
    if os.name == "nt": #windows
        os.system('cls')
    else:
        os.system('clear')

def choose_function():
    global char_plr
    # GAME STARTS
    clear()
    logo()

    if debug:
        print("DEBUG-MODE-ENABLED")


    print("""
1. New Game
2. Play Online
3. Change Skin
""")
    choose = int(input("Choose > "))
    if not 0 < choose < 4:
        print("[!] WRONG INPUT")
        exit()
    else:
        if choose == 1:
            normal_game()
        elif choose == 2:
            clear()
            logo()
            ip = input("IP:PORT Server : ")
            clear()
            print("[*] Connecting to the server.")
            ip = ip.replace("http://","")
            ip = ip.replace("https://","")
            
            if requests.get(f"http://{ip}").ok:
                print("[OK] Connected to the server.")
                print("[*] Joining the game.")
                r1 = requests.get(f"http://{ip}/join/{id_plr}/{char_plr}")
                if r1.ok:
                    online_game(ip,r1.text)
        elif choose == 3:
            clear()
            logo()
            new_skin = input("Write your skin with chars (you can only use it now): ")
            if not 0 < len(new_skin) < 8:
                print("[!] Skin must be between 1 - 7 characters.")
                exit()
            else:
               char_plr = new_skin
               time.sleep(2)
               choose_function()

choose_function()