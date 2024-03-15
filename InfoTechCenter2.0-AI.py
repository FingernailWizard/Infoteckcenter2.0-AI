import time

def print_loading_message(message, duration):
    dots = 0
    for _ in range(duration):
        dots = (dots + 1) % 4  # Increment dots and reset to 0 after reaching 3
        if dots == 0:
            loading_str = "dot dot dot"  # Display "dot dot dot" when dots reach 3
        else:
            loading_str = "dot " * dots  # Otherwise, display "dot" repeated based on the number of dots
        print(f"{message} {loading_str}", end='\r', flush=True)  # Print the loading message with the appropriate dots
        time.sleep(0.5)  # Pause for 0.5 seconds

def main():
    welcome_message = "\n\nWelcome to Info Tech Center version 1.0\n"
    loading_message = "Info Tech Center Operating System Grimacing"
    completion_message = "\n\nOperating System Has Grimaced Up - Retina Scanned - Access Granted"

    print(welcome_message)
    time.sleep(1)
    print_loading_message(loading_message, duration=20)  # Print loading animation for 20 cycles
    print(completion_message)

if __name__ == "__main__":
    main()