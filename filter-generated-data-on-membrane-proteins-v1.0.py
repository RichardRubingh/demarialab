#!/usr/bin/python3
'''
Name Script : filter-generated-data-on-membrane-proteins-v1.0.py
Name Author : Richard Rubingh
Date		: 11-25-2016

DESCRIPTION
	This script removes genes from a csv file that are non-protein coding.
	The scrip writes a new csv file containing membrane coding genes and
	adds the gene name. 


'''

#importing module(s)

import re 
import argparse


class RNAseqNonMembraneProteinCodingGeneRemover:
	""" Using Databases """
	def __init__(self):
		

		try:
			self.input_target_file,self.output_target_file,self.info_target_file	= self.parseCLI()
			self.set_input_and_output()
			self.write_membrane_protein_coding_genes()


		except Exception as e:
			self.usage(e)
				


	def usage(self, errorMessage):
		''' This function is a short usage for errorhandling.'''
		print(__doc__)
		print("Something went wrong!\nPlease re-try.\nError: {}".format(errorMessage))



	def set_input_and_output(self):
		self.genes_for_protein_membrane_filtering = open(self.input_target_file)
		self.membrane_protein_out 				  = open(self.output_target_file,"w")
		self.info                                 = open(self.info_target_file)




	def write_membrane_protein_coding_genes(self):
		'''Add the first line to the csv file containing the header, and
		write the csv file with the membrane genes'''

		for header in self.genes_for_protein_membrane_filtering:
			self.membrane_protein_out.write(header.strip() + ',"GeneName"\n')
			print(header.strip() + ',"GeneName"\n')
			break




		for row in self.genes_for_protein_membrane_filtering:
			gene = row.split(",")[0].replace("\"","")
			
			for info_row in self.info :
				if gene in info_row:
					if "embrane" in info_row:
						if len(gene) >= 2 : 
							
							GeneName = info_row.split("\t")[2]
							print(GeneName)
							self.membrane_protein_out.write(row.strip() + ',"' + GeneName + '"\n' )


		self.membrane_protein_out.close()
		print(self.membrane_protein_out)





	def parseCLI(self):
		'''
		this function parses the command-line input of the user and returns 
		a string which represents the path to the file which is used in the 
		program. And the string which is used for output target location.
		----------

		-g	:	gene information file location
		-i	:	input csv file
		-o 	:	output csv file 


		Returns
		-------
		info_target_file :	string
		The location of the info file
	

		input_target_file :	string
		The location of the input file 
		
		output_target_file :	string
		The location of the output file 
		'''


		parser = argparse.ArgumentParser(description="This program requiers -i <input file path> -o <output file path>")
		parser.add_argument("-g",required=True ,help="Gene info file path")
		parser.add_argument("-i",required=True ,help="Input file")
		parser.add_argument("-o",required=True ,help="Output file")
		

		args = parser.parse_args()
		info_target_file 		= args.g
		input_target_file  		= args.i
		output_target_file 		= args.o
		


		return input_target_file,output_target_file,info_target_file




def main():

	run = RNAseqNonMembraneProteinCodingGeneRemover()

if __name__ == '__main__':
	
	
    main()




