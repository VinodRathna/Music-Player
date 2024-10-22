from cx_Freeze import *
from cx_Freeze import sys

includefiles = ["7.ico"]
excludes = []
packages = []
base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "Music Player",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]\Music Player.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     "TARGETDIR",  # WkDir
     )
]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}
setup(
    version="2.6",
    description="Music Player developed by Konda Sai Sri Vinod Rathna",
    author="Konda Sai Sri Vinod Rathna",
    name="Music Player",
    options={'build_exe': {'include_files': includefiles}, "bdist_msi": bdist_msi_options, },
    executables=[
        Executable(
            script="Music Player.py",
            base=base,
            icon='7.ico',
        )
    ]
)
