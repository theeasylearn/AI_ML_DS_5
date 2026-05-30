import spacy
from pathlib import Path

# Load the best trained model
nlp = spacy.load("./output/model-best")

# Save to a permanent directory
save_path = Path("my_course_extractor")
nlp.to_disk(save_path)

print(f"Model saved to: {save_path}")

# # Verify what was saved
# for item in save_path.iterdir():
#     print(f"  {item.name}")