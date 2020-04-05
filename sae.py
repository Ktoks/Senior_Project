#!/usr/bin/env python3
from argparse import ArgumentParser
from precise.util import activate_notify
from precise_runner import PreciseEngine, PreciseRunner
from threading import Event
import speech_to_text

"""don't forget to source .venv/bin/activate"""

import signal
import sys

def signal_handler(sig, frame):
    print('You may have to press ctrl+c again to exit the second thread')
    sys.exit(0)

def sae():
    activate_notify()
    # print("sae function activated")
    speech_to_text.main()

def on_prediction(prob):
    print("" if prob > 0.7 else '', end='' ,flush=False)


def main():

    engine = PreciseEngine('/home/harbad/mycroft-precise/.venv/bin/precise-engine', 'hey-sae.pb')
    runner = PreciseRunner(engine, on_prediction=on_prediction,on_activation=sae, trigger_level=0).start()
    # runner.start()
    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C to exit')
    signal.pause()
    # try:
    #     Event().wait()
    # except:
    #     print("Goodbye")
    #     sys.exit(0)

if __name__ == '__main__':
    main()
