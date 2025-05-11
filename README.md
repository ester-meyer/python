# BusNoSun

**BusNoSun** is a small application designed to help people choose the best place to sit on a bus or vehicle during a trip,
ensuring they stay in the shade as much as possible. The app takes the user's departure and destination addresses, 
calculates the angle of the sun in relation to the direction of travel, and recommends the best place to sit for shade.

## How It Works

1. **Input the source and destination addresses**: The user inputs the departure and destination addresses.
2. **Convert to latitude and longitude**: Using the `geopy` library, the app converts the address information into geographic coordinates (latitude and longitude).
3. **Calculate travel angle**: The app calculates the direction of travel (relative to the North) based on the coordinates.
4. **Calculate the sun's angle**: Using the `astral` library, the app calculates the sun's angle at the time of travel.
5. **Shade recommendation**: The app calculates the direction where the sun will be most of the time, based on the direction of travel, and recommends where to sit.

## Requirements

Before running the project, make sure to install the required libraries:

Running the Project
Once the dependencies are installed, you can run the code by executing the main file of the project. Here’s how to run it:

Make sure you're in the project directory.

Run the code by executing:

python main.py
The system will prompt you to enter the source and destination addresses and will calculate the sun's angle relative to the direction of travel.

How It Works (Detailed Explanation)
The Nominatim function from the geopy.geocoders library receives the city name and returns the latitude and longitude of the source and destination. After that, using the sun function from the astral library, we obtain the sun’s angle at the time of the trip.

The system calculates the travel angle relative to North and computes the direction where the sun will be most of the time during the journey.

Future Improvements
This project is simple and small, but it can be extended with features like:

Support for different times of the day.

Real-time data usage for more accurate calculations.

Improving the user interface and turning it into a GUI-based application.

Contributions
If you'd like to contribute to the project, please feel free to open an issue or submit a pull request.

Thank you for using the project!
