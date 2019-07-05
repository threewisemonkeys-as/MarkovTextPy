#! /usr/bin/env python3.7

__author__ = "Atharv Sonwane"

import argparse
from markov import MarkovModel

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