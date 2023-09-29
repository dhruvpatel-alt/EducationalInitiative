# Smart Home System

The Smart Home System is a simulation that allows users to control different smart devices such as lights, thermostats, and door locks via a central hub. Users can set schedules, automate tasks, and view the status of each device.

## Features

- Initialize the Smart Home System with different devices, each having a unique ID and type (light, thermostat, door lock).
- Turn devices on/off.
- Schedule devices to turn on/off at a specific time.
- Automate tasks based on triggers (e.g., turning off lights when the thermostat reaches a certain temperature).

### New Functionalities

#### Trigger System

The Smart Home System now includes a Trigger System that allows users to define conditions and actions for automating tasks. Here's how it works:

- Users can add triggers based on conditions and specify actions.
- Conditions can include temperature thresholds for thermostats and other custom conditions.
- Actions can include turning devices on or off.

#### Thermostat Trigger

The Thermostat device now has the ability to trigger actions on other devices based on temperature conditions. For example, when the thermostat temperature exceeds a certain threshold, you can automate actions like turning off lights.

### Getting Started

Follow these instructions to set up and run the Smart Home System simulation on your local machine.

#### Prerequisites

- Python 3.x
- [schedule](https://pypi.org/project/schedule/) library

#### Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip`:

```bash
pip install schedule
