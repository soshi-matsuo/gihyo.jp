import MeCab

def mecab_split(text):
    poses = ['名詞', '動詞', '形容詞', '感動詞', '連体詞']
    tokens = []
    t = MeCab.Tagger()
    t.parse('')  # parse empty to avoid error related with encoding
    node = t.parseToNode(text)
    while node:
        if node.feature.split(',')[0] in poses:
            tokens.append(node.feature.split(',')[6])  # use original form
        node = node.next
    return tokens