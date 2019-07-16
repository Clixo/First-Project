import ctypes

# Grab a handle to the kernel32.dll && User32.dll
k_handle = ctypes.WinDLL("Kernel32.dll")
u_handle = ctypes.WinDLL("User32.dll")

# Access Rights
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)

lpWindowName = ctypes.c_char_p(input("Enter the name of the window to kill: ").encode('utf-8'))

hWnd = u_handle.FindWindowA(None, lpWindowName)

if hWnd == 0:
    print ("[ERROR] Could not grab Handle! Error Code: {0}".format(k_handle.GetLastError()))
    exit(1)
else:
    print("[INFO] Grabed Handle...")
    
lpdwProcessId = ctypes.c_ulong()

response = u_handle.GetWindowThreadProcessId(hWnd, ctypes.byref(lpdwProcessId))

if response == 0:
    print("[ERROR] Could not get Process ID from Handle! Error Code: {0}".format(k_handle.GetLastError()))
else:
    print("[INFO] Found PID...")
    
dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False
dwProcessId = lpdwProcessId

hProcess = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle,dwProcessId)

if hProcess <= 0:
    print("[ERROR] Could not grab privileged Handle! Error Code {0}".format(k_handle.GetLastError()))
else:
    print("[INFO] Priviledged handle opened...")
    
uExitCode = 0x1

response = k_handle.TerminateProcess(hProcess, uExitCode)

if response == 0:
    print("[ERROR] Could not kill process! Error Code: {0}".format(k_handle.GetLastError()))
else:
    print("[INFO] Process Killed...")