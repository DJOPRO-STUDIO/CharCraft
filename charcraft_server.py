"""
CharCraft Server Setup
by DJSTUDIO

Copyrigth (c) DJSTUDIO 2024

Note1 : This code has auto-setup which installs everything using PIP.
Note2 : This code can overload the computer/PC because of the exausted request attemps. """

import pip
import json

try:
    from flask import *
except ImportError:
    pip.main(["install","flask"])
    from flask import *

app = Flask(__name__)

#### CONFIG ####
try:
    file = open("config.json","r")
    config_server = json.load(file)
except FileNotFoundError:
    print("ERROR : config.json File not Found.")
    exit()

# STATICS VALUES
blocks = []
players = []
players_pos = []

@app.route("/")
@app.route("/status")
def status_home():
    return {"success":1,"server_name":config_server["name"],"desc":config_server["desc"],"owner":config_server["owner"],"players":len(players), "blocks":len(blocks), "size":config_server["size"]}

@app.route("/join/<id>/<char>")
def join(char,id):
    for plr_folder in players:
        if plr_folder[1] == int(id):
            return {"success":1}
    
    players.append([int(id),char])
    players_pos.append([int(id),int(config_server["size"][0] / 2),int(config_server["size"][1] / 2)])
    plr = []
    for i in players:
        for i0 in players_pos:
            if i[0] == i0[0]:
                plr.append([i[1],i0[1],i0[2]])

    return {"success":1,"blocks":blocks,"players":plr}

@app.route("/leave/<id>")
def leave(id):
    for plr_folder in players:
        if plr_folder[1] == int(id):
            players.remove(plr_folder)
            for i in players_pos:
                if i[0] == int(id):
                    players_pos.remove(i)

            return {"success":1}
        
@app.route("/change_pos/<id>/forward")
def change_pos_0(id):
    # avancer
    for plr_pos in players_pos:
        if int(id) == plr_pos[0]:
            print(plr_pos)
            char_plr = ""
            for char in players:
                if int(id) == char[0]:
                    char_plr = char[1]

            pos_x = plr_pos[1]
            pos_y = plr_pos[2]
            move = True

            for i in blocks:
                if i[0] == pos_x and i[1] == pos_y - 1:
                    move = False
                    break
                if i[1] == pos_y - 1 and pos_x < i[0] < pos_x + len(char_plr):
                    move = False
                    break
            if move and not pos_y <= 1:
                plr_pos[2] = plr_pos[2] - 1 #y
                return {"x":plr_pos[1],"y":plr_pos[2]}
            
    return {"error":"not_found"}, 404

@app.route("/change_pos/<id>/backward")
def change_pos_1(id):
    # reculer
    for plr_pos in players_pos:
        if int(id) == plr_pos[0]:
            char_plr = ""
            for char in players:
                if int(id) == char[0]:
                    char_plr = char[1]

            pos_x = plr_pos[1]
            pos_y = plr_pos[2]

            move = True
            for i in blocks:
                if i[0] == pos_x and i[1] == pos_y + 1:
                    move = False
                    break
                if i[1] == pos_y + 1 and pos_x < i[0] < pos_x + len(char_plr):
                    move = False
                    break

            if move and not pos_y >= config_server["size"][1]:
                plr_pos[2] = plr_pos[2] + 1 #y

                return {"x":plr_pos[1],"y":plr_pos[2]}

@app.route("/change_pos/<id>/left")
def change_pos_2(id):
    # reculer
    for plr_pos in players_pos:
        if int(id) == plr_pos[0]:
            char_plr = ""
            for char in players:
                if int(id) == char[0]:
                    char_plr = char[1]

            pos_x = plr_pos[1]
            pos_y = plr_pos[2]

            move = True
            for i in blocks:
                if i[0] == pos_x - 1 and i[1] == pos_y:
                    move = False
                    break
            if move and not pos_x <= 1:
                plr_pos[1] = plr_pos[1] -1 #x

                return {"x":plr_pos[1],"y":plr_pos[2]}

@app.route("/change_pos/<id>/right")
def change_pos_3(id):
    # reculer
    for plr_pos in players_pos:
        if int(id) == plr_pos[0]:
            char_plr = ""
            for char in players:
                if int(id) == char[0]:
                    char_plr = char[1]

            pos_x = plr_pos[1]
            pos_y = plr_pos[2]

            move = True
            for i in blocks:
                if i[0] == pos_x + len(char_plr) and i[1] == pos_y:
                    move = False
                    break
            if move and not pos_x >= config_server["size"][0]:
                plr_pos[1] = plr_pos[1] +1 #x

                return {"x":plr_pos[1],"y":plr_pos[2]}

@app.route("/add_block/<id>")
def add_block(id):
    
    for plr_pos in players_pos:
        if int(id) == plr_pos[0]:
            x = config_server["size"][0]
            y = config_server["size"][1]

            char_plr = ""
            for char in players:
                if int(id) == char[0]:
                    char_plr = char[1]
            
            pos_x = plr_pos[1]
            pos_y = plr_pos[2]

            move = True
            for i in blocks:
                if i[0] == pos_x + len(char_plr) and i[1] == pos_y:
                    move = False
                    break
            if move and not pos_x >= x:
                last_x = pos_x
                last_y = pos_y
                plr_pos[1] = plr_pos[1] + 1
                blocks.append([last_x,last_y])
                return {"x":plr_pos[1],"y":plr_pos[2],"blocks":blocks}
            

    return {"x":plr_pos[1],"y":plr_pos[2],"blocks":blocks}

@app.route("/refresh/<id>")
def blocks_get(id):
    plr = []
    for i in players:
        for i0 in players_pos:
            if i[0] == i0[0] and i[0] != int(id):
                plr.append([i[1],i0[1],i0[2]])

    return {"success":1,"blocks":blocks,"players":plr}

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config_server["port"])