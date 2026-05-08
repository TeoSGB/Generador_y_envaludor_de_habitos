class SimulatedInternalError(Exception):
    """Raised when a service needs to simulate an internal failure."""

    def __init__(self, message: str = "A simulated internal error occurred.") -> None:
        self.message = message
        super().__init__(message)

