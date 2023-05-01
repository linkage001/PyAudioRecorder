from tkinter import *
from audioRecorder import AudioRecorder

class UserInterface:
    """A class to create a visual interface for recording audio."""

    def __init__(self, filename):
        """Initialize the user interface with the given filename."""
        self.filename = filename  # the name of the wav file to save
        self.recorder = AudioRecorder(self.filename)  # create an audio recorder object
        self.recording = False  # a flag to indicate if recording is on or off
        self.root = Tk()  # create a root window
        self.root.title("Audio Recorder")  # set the title of the window
        self.root.geometry("300x100")  # set the size of the window

        # Device dropdown

        self.devices = []  # a list to store the devices that have input channels
        self.device_var = StringVar(self.root)  # a string variable to store the selected device index
        self.device_var.set(None)  # set its initial value to None
        self.create_device_menu()  # create a dropdown menu for selecting devices

        # Start Record
        self.button = Button(
            self.root, text="Start Recording", command=self.toggle_recording
        )  # create a button to start or stop recording
        self.button.pack(padx=10, pady=10)  # pack the button in the window

    def toggle_recording(self):
        """Toggle the recording state and update the button text."""
        if self.recording:  # if recording is on
            self.recorder.stop()  # stop recording and save file
            self.recording = False  # set the flag to false
            self.button.config(text="Start Recording")  # change the button text
        else:  # if recording is off
            self.recorder.start()  # start recording
            self.recording = True  # set the flag to true
            self.button.config(text="Stop Recording")  # change the button text

    def create_device_menu(self):
        """Create a dropdown menu for selecting devices from a list of available devices."""
        info = (
            self.recorder.audio.get_host_api_info_by_index(0)
        )  # get information about the host API
        numdevices = info.get("deviceCount")  # get the number of devices

        for i in range(0, numdevices):
            device_info = self.recorder.audio.get_device_info_by_host_api_device_index(
                0, i
            )  # get information about each device
            if device_info.get("maxInputChannels") > 0:  # check if the device has input channels
                self.devices.append(
                    (i, device_info.get("name"))
                )  # append the device index and name to the list

        if len(self.devices) == 0:  # if no devices have input channels
            print("No input devices available.")  # print an error message and exit the method
            return
        else:  # if more than one device has input channels
            self.device_menu = OptionMenu(
                self.root, self.device_var, *self.devices, command=self.set_device_index
            )  # create an OptionMenu widget with the devices list and a command function
            self.device_menu.pack()  # pack the widget in the window

    def set_device_index(self, value):
        """Set the device index of the audio recorder to the selected value."""
        self.recorder.device_index = value[0]  # set the device index to the first element of the value tuple
        print(f"Using {value[1]}")  # print the device name

    def run(self):
        """Run the main loop of the user interface."""
        self.root.mainloop() # run the main loop of the window
