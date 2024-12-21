from bert_score import score

# Example data
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

# Compute BERTScore (batch processing)
P, R, F1 = score(cands=tamil_texts, refs=english_texts, lang="en", verbose=True)

# Print the BERTScore results
print("BERTScore Results (One-to-One English-Tamil):")
for i in range(len(english_texts)):
    print(f"Text Pair {i + 1} - Precision: {P[i]:.4f}, Recall: {R[i]:.4f}, F1: {F1[i]:.4f}")
