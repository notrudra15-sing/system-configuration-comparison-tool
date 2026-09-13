import psutil
import platform
import subprocess
import json

print("System Configuration Generator")
print("------------------------------")

#Most of the code below is similar to main.py, but with some modifications to make it more suitable for generating a configuration file. The code below will detect the operating system, CPU, RAM, storage, and GPU information and store it in a dictionary. Finally, it will save the configuration as a JSON file named "system_b.json".
#the idea was to create a separate script that can be run to generate a configuration file that can be used by the main.py script to compare the system specifications. This way, the user can run this script on their system to generate a configuration file and then use that file to compare their system specifications with another system.



# Detecting the operating system
os = platform.system()
OS_Version = platform.version()
Architecture = platform.machine()



# Detecting CPU information
cpu_freq = psutil.cpu_freq()
Physical_Cores = psutil.cpu_count(logical=False)
Logical_Cores = psutil.cpu_count(logical=True)

# Detecting CPU model name based on the operating system
if os == "Linux":
    with open("/proc/cpuinfo", "r") as file:
        for line in file:
            if "model name" in line:
                CPU_Model = line.split(":")[1].strip()
                break

elif os == "Windows":
    CPU_Model = subprocess.getoutput(
        'wmic cpu get name'
    ).split("\n")[1].strip()

else:
    CPU_Model = "CPU detection not supported on this OS"



# Detecting RAM
ram = psutil.virtual_memory()
Total_RAM = round(ram.total / (1024 ** 3), 2)



# Detecting storage using the same cross platform approach as in main.py. The code below will check the OS and then run the appropriate command to get the storage information.
if os == "Linux":
    disk = psutil.disk_usage("/")

elif os == "Windows":
    disk = psutil.disk_usage("C:\\")

else:
    disk = None

if disk:
    Total_Storage = round(disk.total / (1024 ** 3), 2)
else:
    Total_Storage = "Storage detection not supported on this OS"



# Detecting GPU using the same cross platform approach as in main.py. The code below will check the OS and then run the appropriate command to get the GPU information.
if os == "Linux":
    gpu = subprocess.getoutput(
        "lspci | grep -E 'VGA|3D'"
    )

elif os == "Windows":
    gpu = subprocess.getoutput(
        'wmic path win32_VideoController get name'
    )

else:
    gpu = "GPU detection not supported on this OS"



# Storing all information
system_info = {
    "Operating System": os,
    "OS Version": OS_Version,
    "Architecture": Architecture,
    "CPU Model": CPU_Model,
    "CPU Frequency": round(cpu_freq.current, 2),
    "Physical Cores": Physical_Cores,
    "Logical Cores": Logical_Cores,
    "Total RAM": Total_RAM,
    "Total Storage": Total_Storage,
    "GPU": gpu
}



# Printing the system information
for key, value in system_info.items():
    print(f"{key}: {value}")



# Saving the configuration as JSON
with open("system_b.json", "w") as file:
    json.dump(system_info, file, indent=4)

print("\nSystem configuration saved as system_b.json")