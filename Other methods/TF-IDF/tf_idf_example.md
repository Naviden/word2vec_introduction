# Understanding TF-IDF with an Example

## Introduction

TF-IDF (Term Frequency-Inverse Document Frequency) is a statistical measure used to evaluate how important a word is in a document relative to a collection of documents (corpus). It is widely used in information retrieval, text mining, and search engines.

TF-IDF consists of two main components:

1. **Term Frequency (TF)**: Measures how often a term appears in a document.
   $$
   TF = \frac{\text{Number of times the term appears in the document}}{\text{Total number of terms in the document}}
   $$

2. **Inverse Document Frequency (IDF)**: Measures how unique a term is across all documents.
   $$
   IDF = \log \left(\frac{\text{Total number of documents}}{\text{Number of documents containing the term}} \right)
   $$

The final **TF-IDF Score** is computed as:

$$
TF\text{-}IDF = TF \times IDF
$$

## Numerical Example

### Given Corpus:

1. **Document 1**: "The cat sat on the mat."
2. **Document 2**: "The dog barked at the cat."
3. **Document 3**: "The cat and the dog are friends."

### Step 1: Compute Term Frequency (TF)

For **Document 1**, let's compute TF for the word **"cat"**:

- Total words in Document 1: 6 ("The", "cat", "sat", "on", "the", "mat")
- "cat" appears **1 time**
- **TF("cat", Document 1) = \( \frac{1}{6} = 0.1667 \)**

### Step 2: Compute Inverse Document Frequency (IDF)

- The word "cat" appears in **all 3 documents**.
- Total documents = **3**
- **IDF("cat") = \( \log \left( \frac{3}{3} \right) = \log(1) = 0 \)**

### Step 3: Compute TF-IDF

$$
TF\text{-}IDF("cat", Document 1) = 0.1667 \times 0 = 0
$$

Since the word "cat" appears in every document, its **IDF is 0**, making its **TF-IDF score 0**. This means "cat" is not useful in distinguishing between documents.

### A More Interesting Case: "mat"

For the word **"mat"** in Document 1:

1. **TF("mat", Document 1) = \( \frac{1}{6} = 0.1667 \)**.
2. "mat" appears **only in Document 1**:
   $$
   IDF("mat") = \log \left( \frac{3}{1} \right) = \log(3) = 1.0986
   $$
3. **TF-IDF("mat", Document 1)**:
   $$
   TF\text{-}IDF("mat", Document 1) = 0.1667 \times 1.0986 = 0.1831
   $$

Since "mat" is unique to Document 1, it has a **higher TF-IDF score**, indicating it is more relevant.