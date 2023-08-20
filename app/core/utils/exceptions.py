class UnsolvableException(Exception):
    """Triggered when can't be solved."""
    def __init__(self, message):
        self.message = message
        super(UnsolvableException, self).__init__(message)
