from settings import *


class Controller:
    def __init__(self, k_p, k_i, k_d, saturation_limit):
        self.k_p = k_p
        self.k_i = k_i
        self.k_d = k_d

        self.integral = 0
        self.derivative = 0
        self.previous_error = 0
        self.previous_error_time = 0

        self.saturation_limit = saturation_limit
        self.unclamped_signal = 0
        self.clamped_signal = 0

        # flags
        self.integral_on = True

    def set_clamped(self, error, unclamped_signal, clamped_signal):
        self.integral_on = not((unclamped_signal != clamped_signal) and (error*unclamped_signal>0))

    def calculate_actuating_signal(self, error, dt):
        if self.integral_on:
            self.integral += error

        if dt:
            self.derivative = (error - self.previous_error) / dt

        self.unclamped_signal = (error * self.k_p) + (self.integral * self.k_i) + (self.derivative * self.k_d)

        if self.saturation_limit:
            self.clamped_signal = max(0, min(self.unclamped_signal, self.saturation_limit))
            self.set_clamped(error, self.unclamped_signal, self.clamped_signal)

        return self.unclamped_signal