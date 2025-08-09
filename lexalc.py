import lexal
import lexal.update as lexal
import subprocess

def doit():
    lexal.directory = "C:\\Users\\user\\Downloads\\pratyushs_files\\VS_code\\frogassemblyc"
    
    lexal.compile()
    
    subprocess.run(["run.bat"])