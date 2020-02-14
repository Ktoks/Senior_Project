#!/usr/bin/env python3

from precise_runner import PreciseEngine, PreciseRunner
from threading import Event

def main():
    engine = PreciseEngine('/home/harbad/mycroft-precise/.venv/bin/precise-engine', 'hey-sae.pb')
    runner = PreciseRunner(engine, on_activation=lambda: print('\n***************************************\nhello\n'))
    runner.start()
    Event().wait()

if __name__ == '__main__':
    main()
