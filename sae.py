#!/usr/bin/env python3
from argparse import ArgumentParser
from precise.util import activate_notify
from precise_runner import PreciseEngine, PreciseRunner
from threading import Event
import speech_to_text

def sae():
    activate_notify()
    # print("sae function activated")
    speech_to_text.main()

def on_prediction(prob):
    print("" if prob > 0.5 else '', end='' ,flush=False)


def main():

    engine = PreciseEngine('/home/harbad/mycroft-precise/.venv/bin/precise-engine', 'hey-sae.pb')
    runner = PreciseRunner(engine, on_prediction=on_prediction,on_activation=sae, trigger_level=0).start()
    # runner.start()
    Event().wait()
    print("Goodbye")

if __name__ == '__main__':
    main()
