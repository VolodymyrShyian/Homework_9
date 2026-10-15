def popular_words (text, words):
    text = text.lower()
    list_text = text.split()
    result = {}
    for word in words:
        list_text.count(word)
        result[word] = list_text.count(word)
    return result

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
