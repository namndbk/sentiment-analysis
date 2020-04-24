import ftfy
import re
import string

import numpy as np

negative_emoticons = {':(', '☹', '❌', '👎', '👹', '💀', '🔥', '🤔', '😏', '😐', '😑', '😒', '😓', '😔', '😕', '😖',
                      '😞', '😟', '😠', '😡', '😢', '😣', '😤', '😥', '😧', '😨', '😩', '😪', '😫', '😭', '😰', '😱',
                      '😳', '😵', '😶', '😾', '🙁', '🙏', '🚫', '>:[', ':-(', ':(', ':-c', ':c', ':-<', ':っC', ':<',
                      ':-[', ':[', ':{'}

positive_emoticons = {'=))', 'v', ';)', '^^', '<3', '☀', '☺', '♡', '♥', '✌', '✨', '❣', '❤', '🌝', '🌷', '🌸',
                      '🌺', '🌼', '🍓', '🎈', '🐅', '🐶', '🐾', '👉', '👌', '👍', '👏', '👻', '💃', '💄', '💋',
                      '💌', '💎', '💐', '💓', '💕', '💖', '💗', '💙', '💚', '💛', '💜', '💞', ':-)', ':)', ':D', ':o)',
                      ':]', ':3', ':c)', ':>', '=]', '8)'}


def mapping(text):
    return text


def replace_emoticon(text):
    for emotion in positive_emoticons:
        text.replace(emotion, "posemoticon")
    for emotion in negative_emoticons:
        text.replace(emotion, "negemoticon")
    return text


def remove_duplicate(text):
    text = re.sub(r"([A-Za-z])\1+",lambda m: m.group(1), text)
    return text


def remove_punctation(text):
    table = str.maketrans({key: None for key in string.punctuation})
    text = text.translate(table)
    return text


def normalize_text(text):
    text = ftfy.fix_text(text)
    text = text.replace("\n", " ")
    text = remove_duplicate(text)
    text = mapping(text)
    text = replace_emoticon(text)
    text = remove_punctation(text)
    return text


def normalize(X):
    X_clean = []
    for x in X:
        X_clean.append(normalize_text(x))
    return np.array(X_clean)