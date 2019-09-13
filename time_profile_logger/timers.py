import time

from functools import wraps

from time_profile_logger.validator import Validator
from time_profile_logger.time_profiler_logging import TimeProfilerLogger

class TimerContext:

    def __init__(self, name, show_time_when_exit=True, logger=None):

        Validator.check_type(name, str)
        Validator.check_type(show_time_when_exit, bool)

        if logger is not None:
            Validator.check_type(logger, TimeProfilerLogger)

        self.name = name
        self.show_time_when_exit = show_time_when_exit
        self.logger = logger

    def __enter__(self):

        self.start_time = time.time()
        return self

    def __exit__(self, *args):

        elapsed_time = time.time() - self.start_time
        if self.logger is not None:
            self.logger.add_time(self.name, elapsed_time)

        if self.show_time_when_exit:
            print('Method: %s | Elapsed time: %0.2fs' % (self.name, time.time() - self.start_time))

    def elapsed_time(self):

        elapsed_time = time.time() - self.start_time

        return elapsed_time


class timer_decorator(object):

    def __init__(self, show_time_elapsed=True, logger=None):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print("Inside __init__()")
        self.show_time_elapsed = show_time_elapsed
        self.logger = logger

    def __call__(self, function):

        def wrapped_function(*args, **kwargs):

            start_time = time.time()
            result = function(*args, **kwargs)
            end_time = time.time()

            elapsed_time = end_time - start_time
            if self.show_time_elapsed:
                print('Method: %s | Elapsed time: %0.2fs' % (function.__name__, elapsed_time))

            print("in wrapped function")
            if self.logger is not None:
                self.logger.add_time(function.__name__, elapsed_time)

            return result

        return wrapped_function


