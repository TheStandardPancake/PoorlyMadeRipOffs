import cx_Freeze

executables = [cx_Freeze.Executable("Play.py")]

import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

cx_Freeze.setup(
    name="Dollal Simulator Simulator",
    options={"build_exe": {"packages": ["pygame"], "include_files": ["buy.png", "dot.png","grid.png","sell.png","whiteBox.png"]}},
    executables = executables
    )
