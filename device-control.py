import subprocess
import speech_recognition as sr

def control_usb_port(action):
    # Replace <location> and <port> with actual values from uhubctl output
    location = "2-1"  # Example location, change as needed
    port = "3"        # Example port number, change as needed
    command = ["sudo", "uhubctl", "-l", location, "-p", port, "-a", action]

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)  # Print the output from the command
    except subprocess.CalledProcessError as e:
        print(f"Error controlling USB port: {e.stderr}")

def listen_for_commands():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")

            if "turn on" in command:
                control_usb_port("on")
            elif "turn off" in command:
                control_usb_port("off")
            else:
                print("Unrecognized command. Please say 'turn on' or 'turn off'.")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    listen_for_commands()
## Ensure you have uhubctl installed (sudo apt-get install uhubctl)
## use command ***sudo uhubctl*** to list the ports of your system
## or use command (lsusb) to find out the ports
## change the port and location as per your need


