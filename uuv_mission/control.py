class PDController:
    def __init__(self, kp: float, kd: float):
        self.kp = kp  # Proportional gain
        self.kd = kd  # Derivative gain

    def set_target(self, target):
        self.target = target

    # Set action at discrete time t for PD controller based on e[t] and e[t-1]
    # error = reference - output (depth) = target - current depth
    def __call__(self, e_t: float, e_prev: float) -> float:
        action = self.kp * e_t + self.kd * (e_t - e_prev)
        return action