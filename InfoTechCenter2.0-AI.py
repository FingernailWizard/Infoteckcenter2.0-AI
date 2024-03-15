import time

def print_loading_message(message, duration):
    dots = 0
    for _ in range(duration):
        dots = (dots + 1) % 4
        if dots == 0:
            loading_str = "dot dot dot"
        else:
            loading_str = "dot " * dots
        print(f"{message} {loading_str}", end='\r', flush=True)
        time.sleep(0.5)

def main():
    welcome_message = "\n\nWelcome to Info Tech Center version 1.0\n"
    loading_message = "Info Tech Center Operating System Grimacing"
    completion_message = "\n\nOperating System Has Grimaced Up - Retina Scanned - Access Granted"

    print(welcome_message)
    time.sleep(1)
    print_loading_message(loading_message, duration=20)
    print(completion_message)

if __name__ == "__main__":
    main()
    
