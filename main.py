import os, requests
import time
os.system("title Auto MC Server Creator")
def get_version(version):
    if version == "1.8.8":
        download(8)
    if version == "1.12.2":
        download(122)
    if version == "1.14.4":
        download(144)
    if version == "1.15.2":
        download(152)
    if version == "1.16.5":
        download(165)
    if version == "1.17.1":
        download(171)
    if version == "1.18.2":
        download(182)
    if version == "1.19":
        download(19)

def download(wanted_version):
    if wanted_version == 8:
        os.system("cls")
        print("This step could take a bit depending on your internet connection so please wait while we download the file for you!")
        print("\nAlso warning! Use this version at your own risk!")
        print("\nThis version is known to contain an RCE vulnerability! Read more about this exploit here https://purpurmc.org/docs/Log4j")
        print("\nI will now install an plugin which fixes this vulnerability, but it still recommended to not use this version!")
        print("\nTo enable this plugin on your server you have to drag it into the plugins folder")
        print("(before dragging it into the plugins folder make sure your server is fully started and running!) and after putting it into the plugins folder you have to restart your server!")
        print("\nBy pressing any key you are acknowledging and agreeing that I am in no fault if anything happens to your server!")
        os.system("pause")
        response = requests.get(f"https://www.spigotmc.org/resources/log4jexploit-fix.98243/download?version=432636")
        open("Log4JExploitFix-1.3.3.jar", "wb").write(response.content)
        response = requests.get(f"https://download1648.mediafire.com/hp2tafakq9ug/ihorhd4u34g3oqh/server.jar")
        open("server.jar", "wb").write(response.content)
    if wanted_version == 122:
        os.system("cls")
        print("This step could take a bit depending on your internet connection so please wait while we download the file for you!")
        print("\nAlso warning! Use this version at your own risk!")
        print("\nThis version is known to contain an RCE vulnerability! Read more about this exploit here https://purpurmc.org/docs/Log4j")
        print("\nI will now install an plugin which fixes this vulnerability, but it still recommended to not use this version!")
        print("\nTo enable this plugin on your server you have to drag it into the plugins folder")
        print("(before dragging it into the plugins folder make sure your server is fully started and running!) and after putting it into the plugins folder you have to restart your server!")
        print("\nBy pressing any key you are acknowledging and agreeing that I am in no fault if anything happens to your server!")
        os.system("pause")
        response = requests.get(f"https://www.spigotmc.org/resources/log4jexploit-fix.98243/download?version=432636")
        open("Log4JExploitFix-1.3.3.jar", "wb").write(response.content)
        response = requests.get(f"https://ucarecdn.com/005ee9b9-d9a7-4e98-8233-3ed0fc378a70/")
        open("server.jar", "wb").write(response.content)
    if wanted_version == 144:
        os.system("cls")
        print("This step could take a bit depending on your internet connection so please wait while we download the file for you!")
        print("\nAlso warning! Use this version at your own risk!")
        print("\nThis version is known to contain an RCE vulnerability! Read more about this exploit here https://purpurmc.org/docs/Log4j")
        print("\nI will now install an plugin which fixes this vulnerability, but it still recommended to not use this version!")
        print("\nTo enable this plugin on your server you have to drag it into the plugins folder")
        print("(before dragging it into the plugins folder make sure your server is fully started and running!) and after putting it into the plugins folder you have to restart your server!")
        print("\nBy pressing any key you are acknowledging and agreeing that I am in no fault if anything happens to your server!")
        os.system("pause")
        response = requests.get(f"https://www.spigotmc.org/resources/log4jexploit-fix.98243/download?version=432636")
        open("Log4JExploitFix-1.3.3.jar", "wb").write(response.content)
        response = requests.get(f"https://download1528.mediafire.com/6ih4d24tbrug/odui4x8idph13pf/server.jar")
        open("server.jar", "wb").write(response.content)
    if wanted_version == 152:
        os.system("cls")
        print("This step could take a bit depending on your internet connection so please wait while we download the file for you!")
        print("\nAlso warning! Use this version at your own risk!")
        print("\nThis version is known to contain an RCE vulnerability! Read more about this exploit here https://purpurmc.org/docs/Log4j")
        print("\nI will now install an plugin which fixes this vulnerability, but it still recommended to not use this version!")
        print("\nTo enable this plugin on your server you have to drag it into the plugins folder")
        print("(before dragging it into the plugins folder make sure your server is fully started and running!) and after putting it into the plugins folder you have to restart your server!")
        print("\nBy pressing any key you are acknowledging and agreeing that I am in no fault if anything happens to your server!")
        os.system("pause")
        response = requests.get(f"https://www.spigotmc.org/resources/log4jexploit-fix.98243/download?version=432636")
        open("Log4JExploitFix-1.3.3.jar", "wb").write(response.content)
        response = requests.get(f"https://ucarecdn.com/848e9e35-da67-425d-b7a6-bf9ca304c94f/")
        open("server.jar", "wb").write(response.content)
    if wanted_version == 165:
        os.system("cls")
        print("This step could take a bit depending on your internet connection so please wait while we download the file for you!")
        print("\nAlso warning! Use this version at your own risk!")
        print("\nThis version is known to contain an RCE vulnerability! Read more about this exploit here https://purpurmc.org/docs/Log4j")
        print("\nI will now install an plugin which fixes this vulnerability, but it still recommended to not use this version!")
        print("\nTo enable this plugin on your server you have to drag it into the plugins folder")
        print("(before dragging it into the plugins folder make sure your server is fully started and running!) and after putting it into the plugins folder you have to restart your server!")
        print("\nBy pressing any key you are acknowledging and agreeing that I am in no fault if anything happens to your server!")
        os.system("pause")
        response = requests.get(f"https://www.spigotmc.org/resources/log4jexploit-fix.98243/download?version=432636")
        open("Log4JExploitFix-1.3.3.jar", "wb").write(response.content)
        response = requests.get(f"https://api.purpurmc.org/v2/purpur/1.16.5/latest/download")
        open("server.jar", "wb").write(response.content)
    if wanted_version == 171:
        os.system("cls")
        print("This step could take a bit depending on your internet connection so please wait while we download the file for you!")
        print("\nAlso warning! Use this version at your own risk!")
        print("\nThis version is known to contain an RCE vulnerability! Read more about this exploit here https://purpurmc.org/docs/Log4j/")
        print("\nI will now install an plugin which fixes this vulnerability, but it still recommended to not use this version!")
        print("\nTo enable this plugin on your server you have to drag it into the plugins folder")
        print("(before dragging it into the plugins folder make sure your server is fully started and running!) and after putting it into the plugins folder you have to restart your server!")
        print("\nBy pressing any key you are acknowledging and agreeing that I am in no fault if anything happens to your server!")
        os.system("pause")
        response = requests.get(f"https://www.spigotmc.org/resources/log4jexploit-fix.98243/download?version=432636")
        open("Log4JExploitFix-1.3.3.jar", "wb").write(response.content)
        response = requests.get(f"https://api.purpurmc.org/v2/purpur/1.17.1/latest/download")
        open("server.jar", "wb").write(response.content)
    if wanted_version == 182:
        os.system("cls")
        print("This step could take a bit depending on your internet connection so please wait while we download the file for you!")
        response = requests.get(f"https://api.purpurmc.org/v2/purpur/1.18.2/latest/download")
        open("server.jar", "wb").write(response.content)
    elif wanted_version == 19:
        os.system("cls")
        print("This step could take a bit depending on your internet connection so please wait while we download the file for you!")
        response = requests.get(f"https://api.purpurmc.org/v2/purpur/1.19/latest/download")
        open("server.jar", "wb").write(response.content)
        
def setup_server(ram):
    ram = int(ram)
    os.system("cls")
    print("Seting up everything for you...")
    start_server(ram)
    os.system("cls")
    print("Agreeing the MC eula for you...")
    with open('eula.txt', 'w') as f:
        f.write('eula=true')
        f.close()
    write_start_file(ram)
    start_server(ram)

def start_server(ram):
    os.system(f"java -Xmx{ram}G -Xms{ram}G -jar server.jar nogui PAUSE")

def write_start_file(ram):
    with open('start_server.bat', 'w') as f:
        f.write(f'java -Xmx{ram}G -Xms{ram}G -jar server.jar nogui PAUSE')
        f.close()

def main():
    os.system("cls")
    print("\nWhat version should your minecraft server be? Make sure you type the version exactly as it's shown!")
    print("""
##############
#   1.8.8    #
#   1.12.2   #
#   1.14.4   #
#   1.15.2   #
#   1.16.5   #
#   1.17.1   #
#   1.18.2   #
#   1.19     #  
##############  
""")
    version = input("> ")
    get_version(version)
    os.system("cls")
    print("How much ram should the server have? (Selecting half of your PC ram is mostly recommended, example: if you have 8GB then select 4GB and if you have 4GB select 2GB)")
    print("""
##############
#    1 GB    #
#    2 GB    #
#    4 GB    #
#    8 GB    #
#    16 GB   #
#    32 GB   #
##############
""")
    ram = input("> ")
    setup_server(ram)
main()
