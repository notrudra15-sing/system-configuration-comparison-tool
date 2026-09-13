import psutil
import platform
import subprocess


def get_system_info():

    # Detecting the operating system
    os = platform.system()
    OS_Version = platform.version()
    Architecture = platform.machine()



    # Detecting CPU information
    cpu_freq = psutil.cpu_freq()
    Physical_Cores = psutil.cpu_count(logical=False)
    Logical_Cores = psutil.cpu_count(logical=True)

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



    # Detecting storage
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



    # Detecting GPU
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



    # Storing all system information
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

    return system_info


#We added a comparison function that takes two system information dictionaries as input and compares their values. The function returns a dictionary that contains the comparison results for each key in the input dictionaries. If the values match, it returns "Match". If the values are numeric and different, it returns the difference. If the values are different and not numeric, it returns a mismatch message with the values from both systems. If a key is not found in one of the systems, it returns "Not found in System B".
def compare_systems(system_a, system_b):

    comparison = {}

    for key in system_a:

        if key in system_b:

            if system_a[key] == system_b[key]:
                comparison[key] = "Match"

            elif isinstance(system_a[key], (int, float)) and isinstance(system_b[key], (int, float)):
                difference = round(system_b[key] - system_a[key], 2)
                comparison[key] = f"Difference = {difference}"

            else:
                comparison[key] = (
                    f"Mismatch "
                    f"(System A: {system_a[key]}, "
                    f"System B: {system_b[key]})"
                )

        else:
            comparison[key] = "Not found in System B"

    return comparison



