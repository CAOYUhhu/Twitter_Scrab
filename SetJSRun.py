#执行操作运行bat文件
import subprocess


def runbat(route, name):
    Quellpfad = route
    Quelldatei = name
    Quelle = Quellpfad + Quelldatei
    subprocess.Popen(Quelle, creationflags=subprocess.CREATE_NEW_CONSOLE)
