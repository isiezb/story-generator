def count_words(text):
    """Count the number of words in a text."""
    return len(text.split())

def estimate_reading_time(text, words_per_minute=200):
    """Estimate reading time in minutes based on word count."""
    word_count = count_words(text)
    reading_time = word_count / words_per_minute
    return round(reading_time, 1) 