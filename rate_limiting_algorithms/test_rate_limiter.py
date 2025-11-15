# ================>Steady test<================
"""
test_rate_limiter.py

Test script for Token Bucket and Leaky Bucket rate limiters.
"""

from token_bucket import TokenBucket
from leaky_bucket import LeakyBucket
import time

def test_token_bucket():
    """Simulate requests for Token Bucket and print results."""
    print("=== Token Bucket Test ===")
    bucket = TokenBucket(capacity=5, refill_rate=1)  # 5 tokens max, 1 token/sec

    for i in range(10):
        allowed = bucket.allow_request()
        print(f"Request {i+1}: {'Allowed' if allowed else 'Denied'} (Tokens left: {bucket.tokens:.2f})")
        time.sleep(0.5)  # simulate requests every 0.5 second

def test_leaky_bucket():
    """Simulate requests for Leaky Bucket and print results."""
    print("\n=== Leaky Bucket Test ===")
    bucket = LeakyBucket(capacity=5, leak_rate=1)  # 5 requests max, 1 processed/sec

    for i in range(10):
        allowed = bucket.allow_request()
        print(f"Request {i+1}: {'Allowed' if allowed else 'Denied'} (Water level: {bucket.water:.2f})")
        time.sleep(0.5)

if __name__ == "__main__":
    test_token_bucket()
    test_leaky_bucket()



# ================>Burst test<================
# """
# test_rate_limiter_burst.py

# Simulate bursts of requests to demonstrate
# Token Bucket and Leaky Bucket rate limiting algorithms.
# """

# from token_bucket import TokenBucket
# from leaky_bucket import LeakyBucket
# import time

# def simulate_burst_token_bucket():
#     """
#     Simulate a burst of requests for Token Bucket.
#     Shows how bursty traffic is allowed until tokens run out.
#     """
#     print("=== Token Bucket Burst Test ===")
#     bucket = TokenBucket(capacity=5, refill_rate=1)  # 5 tokens max, 1 token/sec

#     # Simulate 15 rapid requests
#     for i in range(15):
#         allowed = bucket.allow_request()
#         print(f"Request {i+1}: {'Allowed' if allowed else 'Denied'} (Tokens left: {bucket.tokens:.2f})")
#         # Very short interval to simulate burst
#         time.sleep(0.1)

# def simulate_burst_leaky_bucket():
#     """
#     Simulate a burst of requests for Leaky Bucket.
#     Shows how the algorithm smooths traffic and rejects requests
#     if bucket overflows.
#     """
#     print("\n=== Leaky Bucket Burst Test ===")
#     bucket = LeakyBucket(capacity=5, leak_rate=1)  # 5 requests max, 1 processed/sec

#     # Simulate 15 rapid requests
#     for i in range(15):
#         allowed = bucket.allow_request()
#         print(f"Request {i+1}: {'Allowed' if allowed else 'Denied'} (Water level: {bucket.water:.2f})")
#         # Very short interval to simulate burst
#         time.sleep(0.1)

# if __name__ == "__main__":
#     simulate_burst_token_bucket()
#     simulate_burst_leaky_bucket()


# ================>Combined (steady + burst test)<================
# """
# Combined Test for Token Bucket and Leaky Bucket Rate Limiters.
# Scenario: Start with steady requests, then send a burst.
# """
# from token_bucket import TokenBucket
# from leaky_bucket import LeakyBucket
# import time

# def combined_test_token_bucket():
#     """Token Bucket: steady + burst requests with mixed allowed/denied in burst."""
#     print("=== Token Bucket Combined Test ===")
#     bucket = TokenBucket(capacity=7, refill_rate=1)  # max 7 tokens, refill 1/sec

#     print("\n-- Steady requests --")
#     for i in range(3):
#         allowed = bucket.allow_request()
#         print(f"Request {i+1}: {'Allowed' if allowed else 'Denied'} (Tokens left: {bucket.tokens:.2f})")
#         time.sleep(0.5)  # steady requests

#     # Partially refill tokens slightly to simulate realistic burst
#     bucket.tokens += 1  

#     print("\n-- Burst requests --")
#     for i in range(10):  # rapid burst
#         allowed = bucket.allow_request()
#         print(f"Burst Request {i+1}: {'Allowed' if allowed else 'Denied'} (Tokens left: {bucket.tokens:.2f})")
#         time.sleep(0.05)  # very short interval to allow partial refill

# def combined_test_leaky_bucket():
#     """Leaky Bucket: steady + burst requests with mixed allowed/denied in burst."""
#     print("\n=== Leaky Bucket Combined Test ===")
#     bucket = LeakyBucket(capacity=7, leak_rate=1)  # max 7, leak 1/sec

#     print("\n-- Steady requests --")
#     for i in range(3):
#         allowed = bucket.allow_request()
#         print(f"Request {i+1}: {'Allowed' if allowed else 'Denied'} (Water level: {bucket.water:.2f})")
#         time.sleep(0.5)

#     # Reduce water slightly to allow some burst requests
#     bucket.water -= 0.5  

#     print("\n-- Burst requests --")
#     for i in range(10):
#         allowed = bucket.allow_request()
#         print(f"Burst Request {i+1}: {'Allowed' if allowed else 'Denied'} (Water level: {bucket.water:.2f})")
#         time.sleep(0.05)  # very short interval for burst

# if __name__ == "__main__":
#     combined_test_token_bucket()
#     combined_test_leaky_bucket()