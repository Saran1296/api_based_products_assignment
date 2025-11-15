"""
token_bucket.py
Implementation of Token Bucket Rate Limiter.
"""

import time

class TokenBucket:
    """
    Token Bucket Rate Limiter
    Attributes:
        capacity (int): Maximum number of tokens in the bucket.
        tokens (float): Current number of tokens available.
        refill_rate (float): Tokens added per second.
        last_refill (float): Timestamp of last token refill.
    """

    def __init__(self, capacity: int, refill_rate: float):
        """
        Initialize the Token Bucket.
        Args:
            capacity (int): Maximum number of tokens in the bucket.
            refill_rate (float): Number of tokens added per second.
        """
        self.capacity = capacity
        self.tokens = capacity  # Start full
        self.refill_rate = refill_rate
        self.last_refill = time.time()

    def allow_request(self, cost: int = 1) -> bool:
        """
        Determines if a request can be allowed.
        Args:
            cost (int): Number of tokens this request costs. Default is 1.
        Returns:
            bool: True if request is allowed, False otherwise.
        """
        now = time.time()
        elapsed = now - self.last_refill
        # Refill tokens based on elapsed time
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
        self.last_refill = now

        if self.tokens >= cost:
            self.tokens -= cost
            return True
        return False
