import sys
from cx_Freeze import setup,Executable
application_title="Youtube Downloader"
main_python_file='YTD.py'
base=None
if sys.platform=='win32':
    base='win32GUI'
includes=["atexit","re"]
setup(
    name = application_title,
    version = '1.0',
    description="An Youtube Downloader",
    options={"build_exe":{"includes":includes}},
    executables = [Executable(main_python_file,base = base)]

)