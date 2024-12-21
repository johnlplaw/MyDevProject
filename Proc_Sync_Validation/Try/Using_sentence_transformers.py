from sentence_transformers import SentenceTransformer, util

# Load a multilingual model
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# Example English and Tamil texts
english_texts = [
    "I love programming.",
    "The weather is nice today.",
    "How are you?",
    "This is an example sentence.",
    "We are learning multilingual embeddings."
]

tamil_texts = [
    "நான் நிரலாக்கத்தை நேசிக்கிறேன்.",
    "இன்று வானிலை நன்றாக இருக்கிறது.",
    "நீங்கள் எப்படி இருக்கிறீர்கள்?",
    "இது ஒரு எடுத்துக்காட்டு வாக்கியம்.",
    "நாம் பல மொழி கற்றுக்கொள்கிறோம்."
]

# Compute embeddings for English and Tamil texts
english_embeddings = model.encode(english_texts, convert_to_tensor=True)
tamil_embeddings = model.encode(tamil_texts, convert_to_tensor=True)

# Compute cosine similarities
cosine_similarities = util.cos_sim(english_embeddings, tamil_embeddings)

# Print the cosine similarity matrix
print("Cosine Similarity Matrix:")
print(cosine_similarities)

# If you want to print one-to-one similarity (diagonal of the matrix)
print("\nOne-to-One Similarities (English-Tamil):")
for i, similarity in enumerate(cosine_similarities.diag()):
    print(f"Text Pair {i + 1}: {similarity.item():.4f}")
