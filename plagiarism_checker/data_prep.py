import pandas as pd
from utils import calculate_cosine_similarity

# Simulated training data
# data = [
#     ("This is the original sentence.", "This is the original sentence.", 1),
#     ("The sky is blue and beautiful.", "The sky is blue.", 1),
#     ("Machine learning is fun.", "I like pizza.", 0),
#     ("Python is a great language.", "I use Java for backend.", 0),
# ]

# Simulated training data
data = [
    # Clearly plagiarized (identical or nearly identical)
    ("This is the original sentence.", "This is the original sentence.", 1),
    ("Artificial intelligence is transforming industries across the world.", "Artificial intelligence is changing industries all over the world.", 1),
    ("The sky is blue and beautiful.", "The sky is blue.", 1),
    ("Climate change is a major global concern.", "Climate change is a big global concern.", 1),
    ("Python is a popular programming language.", "Python is a popular programming language.", 1),
    ("Machine learning helps systems improve automatically.", "Machine learning helps systems improve by themselves.", 1),

    # Partially similar (should be near threshold)
    ("Deep learning models need large datasets.", "Deep learning requires a huge amount of data.", 1),
    ("The car is fast and efficient.", "The car is speedy and fuel efficient.", 1),
    ("The movie was interesting and thrilling.", "The film was exciting and engaging.", 1),

    # Clearly different (non-plagiarized)
    ("Machine learning is fun.", "I like pizza.", 0),
    ("Python is a great language.", "I use Java for backend.", 0),
    ("The sky is blue and beautiful.", "Mountains are tall and rocky.", 0),
    ("Dogs are loyal animals.", "Computers execute programs quickly.", 0),
    ("He loves playing cricket.", "She enjoys cooking pasta.", 0),
    ("The economy is growing steadily.", "Birds are migrating to warmer regions.", 0),
    ("Reading books improves vocabulary.", "Running daily boosts stamina.", 0),
]

# Compute similarity and label
rows = []
for original, submission, label in data:
    sim = calculate_cosine_similarity(original, submission)
    rows.append([original, submission, sim, label])

df = pd.DataFrame(rows, columns=["Original", "Submission", "Similarity", "Label"])
df.to_csv("plagiarism_dataset.csv", index=False)
