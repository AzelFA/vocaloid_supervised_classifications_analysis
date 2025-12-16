import re
import string
import nltk
import numpy as np
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer , WordNetLemmatizer
from nltk.corpus import stopwords
import contractions

def cleaningText(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text) # Hapus mentions
    text = re.sub(r'#[A-Za-z0-9]+', '', text) # Hapus hashtag
    text = re.sub(r'RT[\s]', '', text) # Hapus RT
    text = re.sub(r"http\S+", '', text) # Hapus link
    text = re.sub(r'[0-9]+', '', text) # Hapus angka
    text = re.sub(r'[^\w\s]', '', text) # Hapus angka

    text = text.replace('\n', ' ') # ganti kosongan menjadi spasi
    # text = text.translate(str.maketrans('', '', string.punctuation)) # hapus kutipan
    text = text.strip(' ') # hapus spasi dari arah kanan dan kiri dari text
    return text

def casefoldingText(text): # Konversi semua huruf menjadi huruf kecil
    text = text.lower()
    return text

def is_latin(text):
    text = re.sub(r'[^\x00-\x7F]', '', text)
    return text

def decontracted(text):
    text = re.sub(r"'t", "not", text)
    text = re.sub(r"'re", " are", text)
    text = re.sub(r"'s", " is", text)
    text = re.sub(r"'d", " would", text)
    text = re.sub(r"'ll", " will", text)
    text = re.sub(r"'ve", " have", text)
    text = re.sub(r"'m", " am", text)
    contractions.add('id', 'i would')
    text = contractions.fix(text)
    text = contractions.fix(text, slang=False)
    return text

def tokenizingText(text): # Tokenizing atau splitting string, text menjadi list tokens
    text = word_tokenize(text)
    return text

def filteringText(text): # Hapus stopwords di text
    listStopwords = set(stopwords.words('english'))
    filtered = []
    for txt in text:
        if txt not in listStopwords:
            filtered.append(txt)
    text = filtered
    return text

def stemmingText(text): # Stemming text
    # Membuat objek stemmer
    ps = PorterStemmer()

    # Memecah teks menjadi daftar kata
    words = text.split()

    # Menerapkan stemming pada setiap kata dalam daftar
    stemmed_words = [ps.stem(word) for word in words]

    # Menggabungkan kata-kata yang telah distem
    stemmed_text = ' '.join(stemmed_words)

    return stemmed_text

def lemmatizerText(text): # Stemming text
    # Membuat objek stemmer
    lt = WordNetLemmatizer()

    # Memecah teks menjadi daftar kata
    words = text.split()

    # Menerapkan stemming pada setiap kata dalam daftar
    lemmd_words = [lt.lemmatize(word) for word in words]

    # Menggabungkan kata-kata yang telah distem
    lemmed_text = ' '.join(lemmd_words)

    return lemmed_text

def toSentence(list_words): # Konversi list words menjadi sentence
    sentence = ' '.join(word for word in list_words)
    return sentence

slangwords = np.load('abbrevations_dictionary.npy', allow_pickle=True).item()

def fix_slangwords(text): # Mengubah slangwords menjadi kata yang baku
    words = text.split()
    fixed_words = []

    for word in words:
        if word.lower() in slangwords:
            fixed_words.append(slangwords[word.lower()])
        else:
            fixed_words.append(word)

    fixed_text = ' '.join(fixed_words)
    return fixed_text

def remove_emoji(string):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        # u"\U00002702-\U000027B0"
        # u"\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)
