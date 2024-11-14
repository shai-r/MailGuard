from typing import List
import re

suspicious_words = ['hostage', 'explos']


def search_words_in_sentence(words: List[str]):
    return lambda sentence: any(re.search(r'\b' + re.escape(word) + r'\b', sentence) for word in words)


search_suspicious_words_in_sentence = search_words_in_sentence(suspicious_words)


def order_sentences(sentences_list: List[str]):
    suspicious_sentences = list(filter(search_suspicious_words_in_sentence, sentences_list))
    not_suspicious_sentences = list(filter(lambda s: not search_suspicious_words_in_sentence(s), sentences_list))
    return suspicious_sentences + not_suspicious_sentences


def is_word_in_sentence(word: str):
    return lambda sentence: word in sentence

is_hostage_in_sentence = is_word_in_sentence('hostage')
is_explos_in_sentence = is_word_in_sentence('explos')
