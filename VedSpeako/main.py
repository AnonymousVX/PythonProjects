import os
if __name__ == '__main__':
    print("Welcome to VedSpeako 1.0 Created by Vedant")
    while True:
        x = input("Enter what you want me to speak/ Press q to exit: ")
        if x == "q":
            print("Goodbye")
            exit_cmd = f'powershell -Command "Add-Type -AssemblyName System.Speech; ' \
                  f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Goodbye\')"'
            os.system(exit_cmd)
            break
        speak_cmd = f'powershell -Command "Add-Type -AssemblyName System.Speech; ' \
                  f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
        os.system(speak_cmd)

