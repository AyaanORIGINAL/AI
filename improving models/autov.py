class AutonomousVehicle:
    def __init__(self):
        self.training_data = ["sunny", "rainy", "cloudy"]
        self.system_status = "Online"

    def navigate(self, environment):
        try:
            if environment not in self.system_status:
               return f"Navigating safely in {environment}" 
            
            else:
                raise ValueError("Critical! Unknown environment detected.")
        except ValueError as e:
            self.system_status = "Offline"
            return str(e)
        
    def patch_system(self, new_conditions):
        self.training_data.update(new_conditions)
        self.system_status = "Online"
        print("Patch deployed. System is back online.")

teslamodelx = AutonomousVehicle()
road_conditions = ["rainy", "foggy", "snowy"]
failures = []
print("starting road test sequence")
for weather in road_conditions:
    result = teslamodelx.navigate(weather)
    print(result)
    if "Critical" in result:
        failures.append(weather)
    if failures:
        print(f"\n Diagnostics report: {len(failures)} failures detected.")
        teslamodelx.patch_system(failures)

        print("\n Rerunning diagnostics")
        print(teslamodelx.navigate("snowy"))