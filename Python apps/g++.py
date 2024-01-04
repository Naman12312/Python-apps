# import PyInstaller
# import subprocess
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--a", type=str, default="", help="Enter name of file")
args1 = parser.parse_args()

with open("Main.py", "rb") as f:
    print(type(f))
def main(args):
    import os
    import PyInstaller.__main__
    PyInstaller.__main__.run([
        f'{args.a}',
        '--onefile'
    ])
    
    # import shutil
    # import os
    # shutil.move(f"Dist\\{args.a}", f"{os.getcwd()}")
main(args1)