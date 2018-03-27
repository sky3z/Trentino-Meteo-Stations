from cx_Freeze import setup, Executable
import os, sys

base = 'Win32GUI' if sys.platform=="win32" else None

os.environ['TCL_LIBRARY'] = "C:\\Program Files (x86)\\Python\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Program Files (x86)\\Python\\tcl\\tk8.6"
executables = [Executable("GUIMain.py", base=base, icon="favicon.ico")]

packages = ["idna", "Log_Bot_xls", "crea__staz_inDir", "idd_str", "idd_down", "template_pdf"]
favicon = ["favicon.ico", "stazioni_meteo.csv","num.txt","Meta-logo.jpg", "C:\\Program Files (x86)\\Python\\DLLs\\tcl86t.dll", "C:\\Program Files (x86)\\Python\\DLLs\\tk86t.dll", "chromedriver.exe", "Log_Bot_xls.py", "crea__staz_inDir.py" ]
modu = ["crea__staz_inDir", "Log_Bot_xls", "idd_str", "idd_down", "template_pdf"]
options = {
    'build_exe': {
        'packages':packages,
		'include_files':favicon,
		'includes': modu
    },
}

setup(
    name = "Stazioni Meteo Trentino",
    options = options,
    version = "1.0",
    description = 'Trentino Meteo Stations',
    executables = executables
)
