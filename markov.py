#! /usr/bin/env python3.7

__author__ = "Atharv Sonwane"

import argparse
import numpy as np


class MarkovModel:
	def __init__(self, filename):
		self.filename = filename
		self.build_corpus()
		self.build_dict()

	def build_corpus(self):
		with open(self.filename) as f:
			self.corpus = f.read().split()

	def make_pairs(self):
		for i in range(len(self.corpus) - 1):
			yield self.corpus[i], self.corpus[i + 1]

	def build_dict(self):
		self.word_dict = {}
		for word1, word2 in self.make_pairs():
			if word1 in self.word_dict.keys():
				self.word_dict[word1].append(word2)
			else:
				self.word_dict[word1] = [word2]

	def gen_first_word(self):
		first_word = np.random.choice(self.corpus)
		while first_word[0].islower():
			first_word = np.random.choice(self.corpus)
		return first_word

	def generate_text(self, length):
		chain = [self.gen_first_word()]
		count = 1
		while count < length or chain[-1][-1] != '.':
			chain.append(np.random.choice(self.word_dict[chain[-1]]))
			count += 1

		return ' '.join(chain)


def main():
	parser = argparse.ArgumentParser(description='Markov Chain Generator')
	parser.add_argument("filename", 
						help="path of file containing training text")
	parser.add_argument("-w", "--words", type=int, default=100,
						help="minimum number of words in generated text")
	args = parser.parse_args()

	model = MarkovModel(args.filename)
	gen_text = model.generate_text(args.words)

	print(f"\n{gen_text}\n")


if __name__ == '__main__':
	main()