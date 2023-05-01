Audio Recorder
A Python program that records audio from microphone and saves it as a wav file.

Description
This project is a simple audio recorder that uses PyAudio and wave modules to capture audio from an input device and store it in a list of frames. The user can select an input device from a list of available devices and start or stop recording with a button. The recorded audio is then saved as a wav file with the specified filename.

Installation
To run this program, you need to have Python 3 installed on your system. You also need to install the dependencies listed in the requirements.txt file using pip:

pip install -r requirements.txt
You can clone this repository or download the zip file and extract it. Then navigate to the project folder and run the main.py file:

python main.py
Usage
When you run the program, you will see a window with a dropdown menu and a button. The dropdown menu shows the devices that have input channels. You can select one of them as your input device. The button allows you to start or stop recording. When you start recording, the button text changes to “Stop Recording”. When you stop recording, the button text changes to “Start Recording” and the recorded audio is saved as a wav file with the filename you specified in the userInterface.py file.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
If you want to contribute to this project, please follow these steps:

Fork this repository
Create a new branch with a descriptive name
Make your changes and commit them with clear messages
Push your branch to your forked repository
Open a pull request and explain your changes
Contact
If you have any questions or feedback, please contact me at william@example.com. You can also visit my website at https://william.com.