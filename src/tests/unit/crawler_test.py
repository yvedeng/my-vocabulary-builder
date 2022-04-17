from tools.crawler import get_audios


def test_getting_audios():
    with open('word_found.html', 'r', encoding='utf-8') as f:
        text = f.read()
        audios = get_audios(text)
        assert len(audios) == 1

test_getting_audios()