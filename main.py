import subprocess
while True:
    try: import distro
    except ModuleNotFoundError: subprocess.Popen('pip install tabulate distro --break-system', shell=True)
    finally:
        import time, psutil, os, platform, distro
        break
time.sleep(0.2)

# split
s = subprocess
p = psutil
on = distro.id().title() + ' Linux'

# ram 
ram = p.virtual_memory()
total_ram = str(ram.total / (1024 ** 3))
used_ram = str(ram.used / (1024 ** 3))
free_ram = str(ram.free / (1024 ** 3))


# - if u want hide one of settings
print("Cutie:", os.getlogin(), ":3")
print("OS:", on, ":3")
print("Ram: ", used_ram[:4], "/", total_ram[:4], f"({free_ram[:4]} free) :3")
