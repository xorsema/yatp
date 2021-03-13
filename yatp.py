from twitchbot import BaseBot, Message, Command
import python_server

input_table = { "A" : False, "B":True, "down":False, "right":False, "select":False, "start":False, "up":False }

@Command('jump')
async def jump_cmd(msg, *args):
    global input_table
    input_table["A"] = True
    for i in range(1,60):
        python_server.joypad.write(1, input_table)
    input_table["A"] = False

@Command('right')
async def jump_cmd(msg, *args):
    global input_table
    input_table["right"] = True
    for i in range(1,60):
        python_server.joypad.write(1, input_table)
    input_table["right"] = False

@Command('left')
async def jump_cmd(msg, *args):
    global input_table
    input_table["left"] = True
    for i in range(1,60):
        python_server.joypad.write(1, input_table)
    input_table["left"] = False

@Command('down')
async def jump_cmd(msg, *args):
    global input_table
    input_table["down"] = True
    for i in range(1,60):
        python_server.joypad.write(1, input_table)
    input_table["down"] = False

@Command('commands')
async def commands_cmd(msg, *args):
    await msg.reply('Use !<direction> and !jump to move Mario!')
    
if __name__ == "__main__":
    python_server.waitForConnection()
    BaseBot().run()

