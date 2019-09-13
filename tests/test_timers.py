from time_profile_logger.time_profiler_logging import TimeProfilerLogger
from time_profile_logger.timers import TimerContext, timer_decorator

import sys
from io import StringIO

logger = TimeProfilerLogger.getInstance()

class TestTimeProfiler():

    def test_if_dict_is_empty_with_decorator(self):

        @timer_decorator(show_time_elapsed=False, logger=logger)
        def function_to_time():

            for i in range(10):
                continue

        number_of_executions = 4
        for _ in range(number_of_executions):
            function_to_time()

        assert logger.times


    def test_if_dict_is_empty_with_context(self):

        with TimerContext(name="test_context", show_time_when_exit=False, logger=logger):

            for _ in range(100):
                continue

        assert logger.times

    def test_if_output_printed(self):

        out = StringIO()
        sys.stdout = out

        # action
        logger.show_times()

        output = out.getvalue().strip()
        assert output






