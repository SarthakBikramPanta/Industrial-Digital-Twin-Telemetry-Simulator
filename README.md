# Industrial-Digital-Twin-Telemetry-Simulator
Developed a Python-based simulation of a Siemens S7-1500 PLC environment to monitor conveyor belt health.

## 📌 Project Overview
This project is a **Digital Twin Simulation** of a Siemens S7-1500 PLC controlling an industrial conveyor system. It bridges the gap between low-level automation logic and high-level Python analytics. 

Since physical PLC hardware (S7-1200/1500) and TIA Portal licenses are often inaccessible in cloud-native development environments, this project simulates the **Data Block (DB)** structures and **Cyclic Scan** behavior of a real Siemens controller.

## 🛠️ Technical Features
* **PLC Tag Simulation:** Mimics real-time sensor data for Motor RPM, Bearing Temperature, and Vibration levels.
* **Deterministic Logic:** Implements industrial threshold monitoring (Warning/Critical states) similar to Ladder Logic or SCL.
* **Virtual Data Blocks:** Organizes data in a class-based structure that mirrors Siemens DB organization.
* **Zero-Dependency Execution:** Designed to run in any standard Python IDE without requiring specialized drivers like `snap7` or `python-snap7`.

## 🚀 How It Works
The script operates on a simulated **Scan Cycle**. In every iteration:
1.  **Input Image:** The script "reads" virtual sensors.
2.  **Program Logic:** It evaluates the values against safety thresholds (e.g., Temperature > 60°C).
3.  **Output Image:** It updates the "PLC_Status" tag and triggers alerts if maintenance is required.

## 📋 How to Run
1.  Open any Python IDE (Offline or Online like Replit/Online-Python).
2.  Copy the contents of `main.py` into the editor.
3.  Run the script.
4.  Observe the terminal; it outputs a real-time telemetry feed formatted for a SCADA/HMI operator view.

## 📈 Industry 4.0 Applications
This project demonstrates skills relevant to modern Siemens automation roles, specifically:
* **Predictive Maintenance:** Using sensor data to predict mechanical failure.
* **Digital Twin Development:** Creating software representations of physical assets.
* **IIoT Ready:** The data structure is prepared for MQTT or OPC UA integration to push PLC data to the cloud (AWS/Azure).
