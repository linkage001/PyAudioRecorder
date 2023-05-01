import threading, pyaudio, wave

class AudioRecorder:
    """A class to record audio from microphone and save it as a wav file."""

    def __init__(self, filename, format=pyaudio.paInt16, channels=1, rate=44100, frames_per_buffer=1024):
        """Initialize the audio recorder with the given parameters."""
        self.filename = filename # the name of the wav file to save
        self.format = format # the format of the audio data
        self.channels = channels # the number of audio channels
        self.rate = rate # the sampling rate in Hz
        self.frames_per_buffer = frames_per_buffer # the number of frames per buffer
        self.audio = pyaudio.PyAudio() # create a PyAudio object
        self.stream = None # the stream object for recording
        self.frames = [] # a list to store the recorded frames
        self.device_index = None # the index of the input device to use
        self.select_device() # prompt the user to select an input device
        self.running = False # a flag to indicate if recording is on or off
        self.thread = None # a thread object for running the loop

    def stop(self):
        """Stop recording audio and save it as a wav file."""
        print("Done recording.")
        self.running = False # set the flag to false
        self.thread.join() # wait for the thread to finish
        self.stream.stop_stream() # stop the stream
        self.stream.close() # close the stream
        self.audio.terminate() # terminate the PyAudio object
        self.save() # save the recorded audio as a wav file

    def save(self):
        """Save the recorded audio as a wav file."""
        wf = wave.open(self.filename, "wb") # open a wav file in write mode
        wf.setnchannels(self.channels) # set the number of channels
        wf.setsampwidth(self.audio.get_sample_size(self.format)) # set the sample width
        wf.setframerate(self.rate) # set the frame rate
        wf.writeframes(b"".join(self.frames)) # write the frames as binary data
        wf.close() # close the file
        print(f"Saved {self.filename}")

    def capture_audio(self):
        """Capture audio from microphone and store it in a list of frames."""
        data = self.stream.read(self.frames_per_buffer) # read a chunk of data from the stream
        # print(data) # print the data
        self.frames.append(data) # append it to the list of frames
        # print(len(self.frames)) # print the length of the frames list

    def loop(self):
        """Run a loop to capture audio until stopped."""
        while self.running: # loop until stopped
            try: # try to capture audio
                self.capture_audio() # capture audio from microphone
            except Exception as e: # if any exception occurs
                print(e) # print the exception and exit the loop
                break

    def select_device(self):
        """Select an input device from a list of available devices."""
        info = self.audio.get_host_api_info_by_index(0)  # get information about the host API
        numdevices = info.get("deviceCount")  # get the number of devices
        devices = []  # a list to store the devices that have input channels
        for i in range(0, numdevices):
            device_info = self.audio.get_device_info_by_host_api_device_index(
                0, i
            )  # get information about each device
            if device_info.get("maxInputChannels") > 0:  # check if the device has input channels
                devices.append((i, device_info.get("name")))  # append the device index and name to the list

        if len(devices) == 0:  # if no devices have input channels
            print("No input devices available.")  # print an error message and exit the method
            return
        elif len(devices) == 1:  # if only one device has input channels
            print("Only one input device available.")  # print a message
            self.device_index = devices[0][0]  # set the device index to the only option
            print(f"Using {devices[0][1]}")  # print the device name
            return
        else:  # if more than one device has input channels
            lowest_device = min(devices, key=lambda x: x[0])  # find the device with the lowest index
            self.device_index = lowest_device[0]  # set the device index to it
            print(f"Using {lowest_device[1]}")  # print the device name

    def start(self):
        """Start recording audio from microphone and capture it in a loop."""
        if self.device_index is None:  # if no device index is set
            print("No input device selected.")  # print an error message and exit the method
            return
        self.stream = self.audio.open(format=self.format,
                                      channels=self.channels,
                                      rate=self.rate,
                                      input=True,
                                      frames_per_buffer=self.frames_per_buffer,
                                      input_device_index=self.device_index)  # open a stream with the chosen device index
        print("Recording...")
        self.running = True  # set the flag to true
        self.thread = threading.Thread(target=self.loop)  # create a new thread to run the loop
        self.thread.start()  # start the thread



