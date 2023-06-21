class TrainingErrorException(Exception):
    def __init__(self, error="Invalid data") -> None:
        super().__init__(error)
