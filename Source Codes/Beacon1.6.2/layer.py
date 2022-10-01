import os
import Messages_Declear as Messages_Declear
current_directory = [ ]
all_directory = ["/users", "/vol","/Docs", "/Desktop", "/docs", "/desktop"]
Desktop = [ ]
docs = [ ]
no_action_layer = ['/users', "/vol", "/Desktop"]
def layer_users():
    current_directory.append("/users")
def layer_vol():
    current_directory.append("/vol")
def layer_dsk():
    current_directory.append("/Desktop")
def layer_docs():
    current_directory.append("/Docs")
def create_layer():
    layer_name = str(input("Naming the Layer: "))
    layer_name = [ ]
    current_directory.append(layer_name)
def all_actions():
    layer_users()
    layer_vol()
    layer_dsk()
def layer():
        if current_directory in no_action_layer:
            print("Current Layer: ", " ".join(current_directory))
        else: 
            all_actions()
            print("Current Layer: ", current_directory)
def layer_info():
    print("layer: show current directory")
