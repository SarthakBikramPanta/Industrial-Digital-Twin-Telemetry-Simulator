# Technical Mapping: Python Digital Twin to Siemens TIA Portal

This document provides a cross-reference between the Python implementation of the Conveyor Simulator and the equivalent concepts within the **Siemens SIMATIC TIA Portal** environment. This mapping demonstrates how high-level software engineering translates to Industrial Automation (OT) standards.

| Python Code Element | Siemens TIA Portal Equivalent | Industrial Logic Concept | Functional Description |
| :--- | :--- | :--- | :--- |
| `class SiemensConveyorSim:` | **FB (Function Block)** | **Encapsulation** | In TIA Portal, an FB is a block with its own memory (Instance DB). The Python class acts as the "blueprint" for the machine logic. |
| `__init__(self):` | **Instance DB (IDB)** | **Static Memory** | This initializes the internal state of the block. In a PLC, this is where the static variables for that specific motor are stored. |
| `self.motor_speed`, `self.temp` | **DB Tags (Data Block)** | **Global/Static Variables** | These variables represent the memory addresses (e.g., `%DB10.DBD2`) where sensor values are stored for HMI/SCADA polling. |
| `get_plc_data(self):` | **Cyclic Execution (OB1)** | **Scan Cycle** | This function simulates the continuous "Read -> Process -> Write" cycle of a PLC CPU. |
| `random.uniform(...)` | **Peripheral Inputs (IW/ID)** | **Analog Signal Processing** | Simulates the 4-20mA or 0-10V analog signals coming from physical sensors into an Analog Input Module (SM 1231/1531). |
| `if self.temp > 75:` | **Comparator (CMP >)** | **Safety Interlock** | Equivalent to a Ladder Logic "Greater Than" block used to trigger a trip or an alarm bit. |
| `self.status = "CRITICAL"` | **Bit Set/Coil (S)** | **Alarm Handling** | Sets a status word or an alarm bit that would typically be visualized on a Comfort Panel or WinCC HMI. |
| `round(value, 2)` | **NORM_X / SCALE_X** | **Signal Scaling** | In TIA Portal, raw integer data from sensors (0-27648) must be normalized and scaled to engineering units (°C, RPM). |
| `time.sleep(1)` | **CPU Scan Time** | **Determinism** | While a real PLC scans in milliseconds, this simulates the constant interval at which data is refreshed for external systems. |

## Architectural Flow Comparison

### 1. Python Simulation Flow
`Class Instance` -> `Method Call` -> `Logic Evaluation` -> `Dictionary Output`

### 2. Siemens TIA Portal Flow
`Process Image Partition` -> `Call FB10, DB10` -> `Network Evaluation` -> `Update Output Image`

---
*Note: This mapping is intended to demonstrate architectural proficiency for roles involving Industry 4.0, IIoT, and Siemens PLC integration.*
