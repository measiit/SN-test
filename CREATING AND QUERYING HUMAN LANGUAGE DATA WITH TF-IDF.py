import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud

# Sample documents
docs = [
    "Artificial intelligence is transforming the world with new technology and innovation",
    "Data privacy is important in the age of artificial intelligence and digital technology",
    "Artificial intelligence and privacy concerns are growing with modern technology systems"
]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(docs)

# Convert to DataFrame
df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# 1. Top keywords
top_keywords = df.sum().nlargest(10)
print("\nTop Keywords:\n", top_keywords)

# 2. Documents containing specific keywords
kw = ['artificial', 'privacy']
selected_docs = df[(df[kw[0]] > 0) & (df[kw[1]] > 0)].index.tolist()
print("\nDocuments containing 'artificial' and 'privacy':", selected_docs)

# 3. WordCloud (from all documents combined)
word_freq = df.sum()
wc = WordCloud(width=800, height=400, background_color='white')
wc.generate_from_frequencies(word_freq)

plt.imshow(wc)
plt.axis("off")
plt.title("WordCloud of Keywords")
plt.show()

# 4. Full TF-IDF table
print("\nTF-IDF Table:\n", df)

# 5. Common keywords across all documents
common_keywords = df.columns[df.min() > 0].tolist()
print("\nCommon Keywords in All Documents:", common_keywords)
