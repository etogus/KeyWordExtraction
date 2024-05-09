import re
from collections import defaultdict

import nltk
from lxml import etree
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')


def remove_punctuation(word):
    return re.sub(r'[^\w\s-]', '', word)


def is_punctuation(word):
    return bool(re.match(r'^[\W_]+$', word))


vectorizer = TfidfVectorizer()

tree = etree.parse("C:\\Users\\gusey\\Downloads\\news.xml")

root = tree.getroot()

dic = defaultdict(list)

news_collection = []

for news in root[0]:
    headline = ""
    news_text = ""
    for n in news:
        if n.get("name") == "head":
            headline = n.text
        elif n.get("name") == "text":
            news_text = n.text
    tokenized_news = word_tokenize(news_text.lower())

    index = 0
    while index < len(tokenized_news):
        if (tokenized_news[index].startswith("'") or
                tokenized_news[index] in stopwords.words("english") or
                is_punctuation(tokenized_news[index]) or
                len(tokenized_news[index]) < 2):
            del tokenized_news[index]
        else:
            tokenized_news[index] = remove_punctuation(tokenized_news[index])
            tokenized_news[index] = WordNetLemmatizer().lemmatize(tokenized_news[index], "n")
            index += 1
    tagged_news = []
    for t in tokenized_news:
        tagged_news.append(nltk.pos_tag([t]))
    tagged_tokenized = []
    for t in tagged_news:
        if t[0][1] == 'NN':
            tagged_tokenized.append(t[0][0])
    news_collection.append(' '.join(tagged_tokenized))
    dic[headline] = []

tfidf_matrix = vectorizer.fit_transform(news_collection)

index = 0
for k, v in dic.items():
    doc = tfidf_matrix[index].toarray()
    terms = vectorizer.get_feature_names_out()
    scores = [(doc[j][m], terms[m]) for j in range(len(doc)) for m in range(len(doc[j]))]
    scores = sorted(scores, reverse=True, key=lambda tup: (tup[0], tup[1]))
    dic[k] = scores
    index += 1

for k, v in dic.items():
    print(f"{k}:")
    values = ""
    for i in range(5):
        values = values + v[i][1] + " "
    print(f"{values}")
