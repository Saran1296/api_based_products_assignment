"""
leaky_bucket.py
Implementation of Leaky Bucket Rate Limiter.
"""
import time

class LeakyBucket:
    """
    Leaky Bucket Rate Limiter
    Attributes:
        capacity (int): Maximum bucket size (requests it can hold at once).
        leak_rate (float): Number of requests processed per second.
        water (float): Current 'water level' in the bucket.
        last_check (float): Timestamp of last leak calculation.
    """

    def __init__(self, capacity: int, leak_rate: float):
        """
        Initialize the Leaky Bucket.
        Args:
            capacity (int): Maximum requests the bucket can hold.
            leak_rate (float): Requests processed per second.
        """
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.water = 0
        self.last_check = time.time()

    def allow_request(self, cost: int = 1) -> bool:
        """
        Determines if a request can be allowed.
        Args:
            cost (int): Size of request to add to the bucket. Default is 1.
        Returns:
            bool: True if request is allowed, False if bucket would overflow.
        """
        now = time.time()
        elapsed = now - self.last_check
        # Leak water according to elapsed time
        leaked = elapsed * self.leak_rate
        self.water = max(0, self.water - leaked)
        self.last_check = now

        if self.water + cost <= self.capacity:
            self.water += cost
            return True
        return False
