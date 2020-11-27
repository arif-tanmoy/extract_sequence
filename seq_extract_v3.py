#!/usr/bin/env python
'''
Extract sequences from FASTA file using ID query.
use: python seq_extract_v3.py --fasta FASTA_FILE --query ID_FILE --output OUTPUT_FILE
author: Arif Mohammad Tanmoy (arif.tanmoy@gmail.com)
'''

import sys
from Bio import SeqIO
from argparse import (ArgumentParser, FileType)

def parse_args():
	"Parse the input arguments, use '-h' for help"
	commands = ArgumentParser(description='Sequence extraction by query ID.')
	commands.add_argument('--fasta', type=str, required=True, help='Fasta sequence.\n')
	commands.add_argument('--query', type=str, required=True, help='query IDs.\n')
	commands.add_argument('--output', type=str, required=False, default='Extracted_Seq.fasta', help='Location & name of output file.\n')
	return commands.parse_args()
args = parse_args()

idd = []
seq = []
for rec in SeqIO.parse(open(args.fasta,"r"), 'fasta'):
	idd.append(str(rec.id))
	seq.append(str(rec.seq))
	

query = []
for line in open(args.query,"r"):
	query.append(line.rstrip())

output = open(args.output,"w")
for i in range(0, len(query)):
	if str(query[i]) in idd:
		j = idd.index(str(query[i]))
		result = ">" + str(idd[j]) + '\n' + str(seq[j])+ '\n'
		output.write(result)
	else:
		print str(query[i])

