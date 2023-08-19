class WaterOverflowException(Exception):
    def __init__(self, message, remaining_water):
        self.message = message
        self.remaining_water = remaining_water
        super(WaterOverflowException, self).__init__(message, remaining_water)
