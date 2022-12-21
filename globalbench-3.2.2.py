#!/usr/bin/python3

import time
import platform  # System info
import os
import signal
from multiprocessing import Process
import subprocess  # Necesario para usar el sistema y sus funciones

global integer
global fp

version = "3.2.2"
nucleos = "1"
stresstest = "0"
rangobucle = 30900900

clear = lambda: subprocess.call('cls||clear', shell=True)  # Llamada al sistema


def test(stresstest, numeronucleos):
    # Operaciones por proceso de ejecución------------------------------------------------------------------------------
    def op1(stresstest):
        while stresstest == "1":
            resultado = 10 * 10 + 10 - 10 / 10 - 10 + 10 * 10

    for i in range(numeronucleos):
        p = Process(target=op1, args=stresstest)
        p.start()
        pid = p.pid
        globals()[f'n{i}'] = pid

    input("Running test... (Enter any key to stop): ")

    for i in range(numeronucleos):
        os.kill(globals()[f'n{i}'], signal.SIGTERM)

    clear()


def punt():
    global integer
    global fp

    puntmax = 1000000

    intinteger = float(integer)
    intfp = float(fp)

    puntint = puntmax / intinteger
    puntfp = puntmax / intfp

    print()
    print("Integer score:", round(puntint))
    print("FP score:", round(puntfp))


def algoint(nucleos, rangobucle):
    global integer

    # Operaciones por proceso de ejecución------------------------------------------------------------------------------
    def op1():
        # print('process id:', os.getpid())
        for x in range(rangobucle):
            resultado = 10 * x

    def op2():
        for x in range(rangobucle):
            resultado = 10 + x

    def op3():
        for x in range(rangobucle):
            resultado = 10 - x

    def op4():
        for x in range(rangobucle):
            resultado = x * x

    def op5():
        for x in range(rangobucle):
            resultado = x + x

    def op6():
        for x in range(rangobucle):
            resultado = x - x

    def op7():
        for x in range(rangobucle):
            resultado = x * x + x - x

    def op8():
        for x in range(rangobucle):
            resultado = x - x + x * x

    # Ejecución operaciones---------------------------------------------------------------------------------------------
    if nucleos == "0":
        start_time = time.time()
        for x in range(rangobucle):  # Cuarenta millones
            resultado = 10 * x
            resultado = 10 + x
            resultado = 10 - x
            resultado = x * x
            resultado = x + x
            resultado = x - x
            resultado = x * x + x - x
            resultado = x - x + x * x
    else:
        start_time = time.time()

        p = Process(target=op1)
        p.start()
        p2 = Process(target=op2)
        p2.start()
        p3 = Process(target=op3)
        p3.start()
        p4 = Process(target=op4)
        p4.start()
        p5 = Process(target=op5)
        p5.start()
        p6 = Process(target=op6)
        p6.start()
        p7 = Process(target=op7)
        p7.start()
        p8 = Process(target=op8)
        p8.start()

        p.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()

    # Fin operaciones---------------------------------------------------------------------------------------------------
    integer = ("%s" % (time.time() - start_time))
    stop_time = time.time()

    print("---",integer+"s ---")


def algoflp(nucleos, rangobucle):
    global fp

    # Operaciones por proceso de ejecución------------------------------------------------------------------------------
    def op1():
        for x in range(rangobucle):
            resultado = 10 / 0x5F3759DF * (1 + x)

    def op2():
        for x in range(rangobucle):
            resultado = 3.141592653589793 / (1 + x)

    def op3():
        for x in range(rangobucle):
            resultado = 10 / 0x5F3759DF * (1 + x)

    def op4():
        for x in range(rangobucle):
            resultado = 3.141592653589793 / (1 + x)

    def op5():
        for x in range(rangobucle):
            resultado = 10 / 0x5F3759DF * (1 + x)

    def op6():
        for x in range(rangobucle):
            resultado = 3.141592653589793 / (1 + x)

    def op7():
        for x in range(rangobucle):
            resultado = 10 / 0x5F3759DF * (1 + x)

    def op8():
        for x in range(rangobucle):
            resultado = 3.141592653589793 / (1 + x)

    # Ejecución operaciones---------------------------------------------------------------------------------------------
    if nucleos == "0":
        start_time = time.time()
        for x in range(rangobucle):  # Treinta millones
            resultado = 10 / 0x5F3759DF * (1 + x)
            resultado = 3.141592653589793 / (1 + x)
            resultado = 10 / 0x5F3759DF * (1 + x)
            resultado = 3.141592653589793 / (1 + x)
            resultado = 10 / 0x5F3759DF * (1 + x)
            resultado = 3.141592653589793 / (1 + x)
            resultado = 10 / 0x5F3759DF * (1 + x)
            resultado = 3.141592653589793 / (1 + x)

    else:
        start_time = time.time()
        p = Process(target=op1)
        p.start()
        p2 = Process(target=op2)
        p2.start()
        p3 = Process(target=op3)
        p3.start()
        p4 = Process(target=op4)
        p4.start()
        p5 = Process(target=op5)
        p5.start()
        p6 = Process(target=op6)
        p6.start()
        p7 = Process(target=op7)
        p7.start()
        p8 = Process(target=op8)
        p8.start()

        p.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()

    # Fin operaciones---------------------------------------------------------------------------------------------------
    fp = ("%s" % (time.time() - start_time))
    stop_time = time.time()

    print("---", fp + "s ---")


if __name__ == '__main__':
    principal = 1
    while principal == 1:
        clear()
        print("Globalbench v" + version)
        print()

        if platform.processor() == "":
            print("CPU:", "ARM")
        else:
            print("CPU:", platform.processor())
        print("System:", platform.system(), platform.version())
        print("Python:", platform.python_version())
        print("Compiler:", platform.python_compiler())

        print()
        print("- Single-Core Benchmark  (0)")
        if platform.system() != "Windows":
            print("- Multi-Core Benchmark   (1)")
            print("- Stress test            (2)")
        print("- Exit                   (3)")
        print()
        if platform.system() == "Windows":
            respuesta = input("Choose Option: ")
        else:
            respuesta = input("Choose Single-Core (0), Multi-Core (1) or Stress Test (2): ")
        if platform.system() == "Windows" and respuesta == "1" or respuesta == "2":
            respuesta = "0"
        print()

        if respuesta == "0": nucleos = "0"
        if respuesta == "1": nucleos = "1"
        if respuesta == "2":
            numeronucleos = input("Choose the amount of cores to test: ")
            print()
            numeronucleos = int(numeronucleos)
            stresstest = "1"
            test(stresstest, numeronucleos)
        if respuesta == "3": exit()
        if nucleos == "0": print("Single-Core benchmark:")
        if nucleos != "0": print("Multi-Core benchmark:")

        while stresstest == "0":
            print()
            print("Integer Benchmark...")
            algoint(nucleos, rangobucle)
            print("FP Benchmark...")
            algoflp(nucleos, rangobucle)
            punt()
            print()
            input("Press any key to continue: ")
            clear()
            stresstest = "1"  # Salida del bucle

        stresstest = "0"  # Reinicio variable
