# Import
import time

from userInterface import UserInterface
# Settings
filename = 'audio.wav'
# Functions

# Instances
ui = UserInterface(filename)
# Main
if __name__ == '__main__':
    print('Language teacher start')
    ui.run()

