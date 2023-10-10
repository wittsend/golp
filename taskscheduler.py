import time

# Used to time when a task should run

class TaskScheduler:
    def __init__(self, frequency_hz:float):
        self._set_interval_ns(frequency_hz)
        self.next_run_time_ns = 0
        self.task_start_time_ns = 0
        self.task_end_time_ns = 0
        self.last_run_duration_ns = 0

    def _set_interval_ns(self, frequency_hz:float):
        if frequency_hz == 0: 
            self.interval_ns = 0
        else:
            self.interval_ns = (int)(10**9/frequency_hz)

    def it_is_time(self):
        current_time_ns = time.time_ns()
        
        if self.interval_ns == 0:
            self.task_start_time_ns = current_time_ns 
            return True
        
        if current_time_ns >= self.next_run_time_ns:
            self.next_run_time_ns = current_time_ns + self.interval_ns
            self.task_start_time_ns = current_time_ns
            return True
        else:
            return False
    
    def finished(self):
        self.task_end_time_ns = time.time_ns()
        self.last_run_duration_ns += self.task_end_time_ns - self.task_start_time_ns
        return self.last_run_duration_ns
    
    def get_run_time(self):
        output = self.last_run_duration_ns
        self.last_run_duration_ns = 0
        return output
    
    def get_run_time_pct(self, total_time_ns:int):
        return self.get_run_time()*100.0/total_time_ns
