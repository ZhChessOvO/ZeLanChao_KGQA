#!/usr/bin/env python3
# coding: utf-8
# File: chatbot_graph.py

from medicine.qs.question_classifier import *
from medicine.qs.question_parser import *
from medicine.qs.answer_search import *

'''问答类'''


class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = '这个问题超出机器人的知识范围了呢！不妨换个说法再问问？'
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return answer
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)


if __name__ == '__main__':
    handler = ChatBotGraph()
    while 1:
        question = input('用户:')
        answer = handler.chat_main(question)
        print('BOT:', answer)
