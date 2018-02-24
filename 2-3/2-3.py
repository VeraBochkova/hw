def search_top_words():
    import chardet
    import json

    with open(file_name, 'rb') as f:
        news = f.read()
        result = chardet.detect(news)

    with open(file_name, encoding=result['encoding']) as f:
        json_text = json.load(f)

    news_text = ''
    for value in json_text['rss']['channel']['items']:
        news_text += ' ' + value['description']

    news_text = news_text.lower().split(' ')

    long_words = []
    for word in news_text:
        if len(word) > 6:
            long_words.append(word)

    repeat_words = {}
    for word in long_words:
        repeat_words[word] = long_words.count(word)

    top_words = []
    for value in sorted(repeat_words, key=repeat_words.get, reverse=True):
        top_words.append(value)
    print('10 самых часто встречающихся слов в новостях:')
    for top_word in range(10):
        print(top_words[top_word])


file_name = input('Введите имя файла:')
search_top_words()