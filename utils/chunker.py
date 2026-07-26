def make_chunks(cleansed_text, chunk_size=1000):
    words = cleansed_text.split()
    chunk_list = []

    for i in range(0, len(words), chunk_size):
        chunk_words = words[i:i + chunk_size]
        chunk_text = " ".join(chunk_words)
        chunk_list.append(chunk_text)

    return chunk_list