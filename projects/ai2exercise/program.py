import xml.etree.ElementTree as ET
import re as RE
from nltk.tokenize import sent_tokenize as SENT_TOKENIZE
from nltk.tokenize import RegexpTokenizer

WORD_TOKENIZER = RegexpTokenizer(r'\w+')

FILE_PATH = 'phoenix_0002.coref.txt'


def part_xml_to_list_sentence_string(text_part):
    """
    Convert (xml_element)text_part to a list[(string)]list of raw sentence
    :param text_part: (xml_element)
    :return: list[(string)]
    """
    # strip off the beginning & ending <TEXT> tag
    text_part = RE.sub('^<TEXT[^>]+>', '', ET.tostring(text_part), 1)
    text_part = RE.sub('</TEXT>$', '', text_part, 1)

    # few methods to help nltk tokenize sentences more correctly
    # - if an entity ends a sentence, make the closing </COREF> come before any punctuation
    # - padding all punctuations with white space
    text_part = RE.sub('([.,!?()]) *(</[^>]+>)', r'\2\1 ', text_part)
    raw_sentences = SENT_TOKENIZE(text_part)
    return raw_sentences


def get_sentence_report(sent):
    """
    for a given (string)sentence return a tuple of {friendly readable sentence, word count, unique entity count}
    :param sent: (string)
    :return: {(string), (int), (int)}
    """
    # create a sentence element
    sentence = ET.fromstring('<sentence>' + sent + '</sentence>')
    # tokenize a natural sentence and count number of words
    read_friendly_sentence = ET.tostring(sentence, encoding='utf8', method='text')
    read_friendly_sentence = RE.sub('\n', '', read_friendly_sentence)
    words = WORD_TOKENIZER.tokenize(read_friendly_sentence)
    if 0 == len(words):
        # no need to continue if this sentence is invalid: has no word
        return '', 0, 0
    #print words

    # extract unique entities
    uniq = set()
    for entity in sentence.findall('COREF'):
        uniq.add(entity.get("ID"))
    #print uniq

    # clean format the readable sentence
    read_friendly_sentence = RE.sub(' *([.,!?()]) *', r'\1 ', read_friendly_sentence)
    return read_friendly_sentence, len(words), len(uniq)


# From file retrieve a list of sentence as raw text
xml = ET.parse(FILE_PATH)
doc_el = xml.getroot()
raw_sentences = []
for text_part in doc_el:
    raw_sentences += part_xml_to_list_sentence_string(text_part)

# For each raw sentence, proceed to obtain word count and unique entity count
valid_sentence_count = 0
max_word_count = 0
total_entity_count = 0
longest_senteces = []
for sent in raw_sentences:
    friendly_sentence, word_count, entity_count = get_sentence_report(sent)
    if 0 == word_count:
        continue

    if word_count > max_word_count:
        longest_senteces = []
        max_word_count = word_count
    if word_count == max_word_count:
        longest_senteces.append(friendly_sentence)
    total_entity_count += entity_count
    valid_sentence_count += 1

# Answer: longest sentence(s)
print "-----------------"
print "=> Longest sentences (" + str(len(longest_senteces)) + "): "
for sent in longest_senteces:
    print "  - " + sent
# Answer: avg count of unique entity per valid sentence
print "-----------------"
print "Sum of unique entity count aggregated by sentence: " + str(total_entity_count)
print "Valid sentence count: " + str(valid_sentence_count)
print "=> Avg unique entity count per sentence: " + str(total_entity_count/float(valid_sentence_count))



