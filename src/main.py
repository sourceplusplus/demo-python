from threading import Thread
from time import sleep

from sourceplusplus.SourcePlusPlus import SourcePlusPlus
SourcePlusPlus().attach()


def trigger_add_breakpoint():
    import command.AddBreakpoint
    command.AddBreakpoint.AddBreakpoint.simple_breakpoint()


def execute_demos():
    while True:
        trigger_add_breakpoint()
        sleep(1)


if __name__ == '__main__':
    Thread(target=execute_demos).start()
