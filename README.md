<!-- README.md -->

# ⚠️ Warning *

### **Do not change anything in this repository unless you have the knowledge or permission. Please focus on your assigned tasks.**
Project is combintion of software and hardware and Video Call Website will be live on Meet.risg.in
# Video Call Intercom System with Sensors and SOS ALerts

This project aims to create an accessible video call intercom system for Deaf individuals, utilizing an analog/IP-based communication system with integrated vibration sensors. The system facilitates communication in environments like offices, homes, and businesses without relying on voice-based communication methods.

## Features.

- **Video Communication**: Facilitates communication using video, making it ideal for sign language users.
- **Vibration Alerts**: Integrated vibration sensors notify the user of incoming calls or messages.
- **Analog/IP System**: Offers flexibility in deployment across different infrastructures, from older analog systems to modern IP networks.
- **User-Friendly Interface**: Designed with simplicity in mind, allowing easy use by individuals who are Deaf or have hearing impairments.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Description

The Smart India Hackathon project aims to create an interactive hand gesture recognition system. This system leverages computer vision and machine learning to detect hand gestures using a webcam and provides real-time feedback. The project consists of several components:

1. **Python Script**: Detects and interprets hand gestures.
2. **Arduino Script**: Interfaces with the Python script for additional functionalities.
3. **Website Content**: Provides a web-based interface to interact with the system.

## Features

- Real-time hand gesture recognition using a webcam.
- Support for recognizing multiple hand gestures (e.g., A, B, C, D, E, F, G).
- Integration with Arduino for extended functionality.
- Web interface for user interaction.

## Technologies

- **Python**: For gesture recognition using OpenCV and MediaPipe.
- **Arduino**: For interfacing and additional functionalities.
- **HTML/CSS**: For creating the web interface.
- **OpenCV**: For image processing.
- **MediaPipe**: For hand landmark detection.

## Installation

### Prerequisites

- Python 3.x
- OpenCV
- MediaPipe
- Arduino IDE

### Python Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/erpranjalmishra/helixom.git
    ```

2. Navigate to the project directory:
    ```bash
    cd helixom
    ```

3. Install the required Python libraries:
    ```bash
    pip install opencv-python mediapipe
    ```

4. Run the Python script:
    ```bash
    python Python Script/main.py
    ```

### Arduino Setup

1. Open the Arduino IDE and upload the provided Arduino script located in the `Arduino Script` folder.

2. Ensure that the Arduino board is properly connected to your computer.

### Website Setup

1. Open the `Website Content/Index.html` file in a web browser to view the web interface.

## Usage

1. **Running the Python Script**: Execute the Python script to start the hand gesture recognition system. The detected gestures will be displayed on the video feed from your webcam.

2. **Arduino Integration**: The Arduino script will interact with the Python script, providing additional functionalities such as controlling external hardware based on detected gestures.

3. **Web Interface**: Access the `Index.html` file to interact with the system via a web-based interface.

## Contributing

We welcome contributions to this project! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Open a pull request with a clear description of your changes.

## License

This project is licensed under the GNU LESSER GENERAL PUBLIC LICENSE
Version 2.1, February 1999 . See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or further information, please contact:

- **Project Owner**: Team-V
- x@risg.in
