import random
import time

class SiemensConveyorSim:
    def __init__(self):
        self.motor_speed = 1500  # RPM
        self.temp = 45.0         # Celsius
        self.vibration = 0.02    # mm/s
        self.status = "RUNNING"

    def get_plc_data(self):
        """Simulates reading tags from a Siemens DB (Data Block)"""
        self.temp += random.uniform(-0.5, 0.7)
        self.vibration = random.uniform(0.01, 0.05)
        
        if self.temp > 75:
            self.status = "CRITICAL - OVERHEATING"
        elif self.temp > 60:
            self.status = "WARNING"
        
        return {
            "Tag_Motor_RPM": round(self.motor_speed, 2),
            "Tag_Bearing_Temp": round(self.temp, 2),
            "Tag_Vibration": round(self.vibration, 4),
            "PLC_Status": self.status
        }

def run_simulation():
    plc = SiemensConveyorSim()
    print("--- Siemens S7-1500 Digital Twin Simulation ---")
    print("Connecting to Virtual Data Block (DB10)... Connected.\n")
    
    try:
        for i in range(15):  # Run for 15 cycles
            data = plc.get_plc_data()
            
            print(f"Cycle {i+1} | Status: {data['PLC_Status']}")
            print(f" >> Temp: {data['Tag_Bearing_Temp']}°C | Vib: {data['Tag_Vibration']} mm/s")
            
            if data['PLC_Status'] != "RUNNING":
                print("!!! ALERT: Maintenance Required !!!")
            
            print("-" * 40)
            time.sleep(1) 
            
    except KeyboardInterrupt:
        print("Simulation Stopped.")

if __name__ == "__main__":
    run_simulation()