#!/usr/bin/python
# -*- coding: utf-8 -*-
# Updated version 08-2023

import operator

def numerological_value(word, letter_numbers):
    """
    Calculate numerological value of a word
    """
    word_value = 0
    for char in word:
        char_value = letter_numbers.get(char.upper())
        if char_value is not None:
            word_value += int(char_value)
    return word_value

def reduce_to_single_digit(num):
    """
    Reduces the number to a single digit or master numbers (11, 22)
    """
    while num > 9 and num != 11 and num != 22:
        num = sum(int(digit) for digit in str(num))
    return num

def calculate_word_values(wordlist, letter_numbers):
    """
    Calculate numerological values of all words in the list
    """
    name_value = {}
    for word in wordlist:
        word_value = numerological_value(word, letter_numbers)
        word_value = reduce_to_single_digit(word_value)
        name_value[word] = word_value
    return name_value

def read_words_from_file(file_path):
    """
    Read words from a file and return as a list
    """
    try:
        with open(file_path, 'r') as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return []

def filter_and_sort_word_values(name_value, chars):
    """
    Filter out words containing specified characters and sort by value
    """
    filtered_sorted_values = sorted((word, value) for word, value in name_value.items()
                                    if not any((c in chars) for c in word))
    return filtered_sorted_values

def display_word_values(word_values):
    """
    Display words and their values
    """
    for word, value in word_values:
        print(f"{word} : {value}")


# Pythagorean numerology letter values
letter_numbers = {  'A': 1, 'J': 1, 'S': 1,
                    'B': 2, 'K': 2, 'T': 2,
                    'C': 3, 'L': 3, 'U': 3,
                    'D': 4, 'M': 4, 'V': 4,
                    'E': 5, 'N': 5, 'W': 5,
                    'F': 6, 'O': 6, 'X': 6,
                    'G': 7, 'P': 7, 'Y': 7,
                    'H': 8, 'Q': 8, 'Z': 8,
                    'I': 9, 'R': 9}

# Read words as a list from file
input_file = 'words.txt'
words = read_words_from_file(input_file)

# Calculate numerological values of all words
name_value = calculate_word_values(words, letter_numbers)

# Characters to ignore in words
chars = set()

# Filter and sort word values
filtered_sorted_values = filter_and_sort_word_values(name_value, chars)

# Display word values
display_word_values(filtered_sorted_values)
