class InventoryError(Exception):
    """Base exception for inventory application errors."""


class NotFoundError(InventoryError):
    """Raised when a requested record does not exist."""


class DuplicateError(InventoryError):
    """Raised when a unique constraint would be violated."""


class ValidationError(InventoryError):
    """Raised when input validation fails."""
