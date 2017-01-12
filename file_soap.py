""" Find all instances of words in all files in the current
file tree. Searches all files and subdirectories for words in the 
file "word_list.txt" and reports the file name and line number

Also finds the word in in a path. Note that this does not find the word
in a document if it appears as part of another word.

For example, a list of obscene words can be found at 
github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words
"""

import os

def clean_files():
	# Import the list of words to find
	cwd = os.getcwd()
	word_list_path = os.path.join(cwd, 'word_list.txt')
	with open(word_list_path, 'r') as word_list_file:
		word_list = word_list_file.read().splitlines()
	clean_current_directory(word_list)

def clean_current_directory(word_list):
	# Current working directory
	cwd = os.getcwd()
	cwd_contents = os.listdir()
	for content in cwd_contents:
		file_path = os.path.join(cwd, content)
		# If content is a directory, recursively apply
		if os.path.isdir(file_path):
			# Change directory and recursively apply
			os.chdir(file_path)
			clean_current_directory(word_list)
		else:
			if content != 'word_list.txt':
				# Make sure the path does not contain any of the words
				for word in word_list:
					# Check if a word is in the path
					if find_word(file_path, os.pathsep + word + os.pathsep):
						print("%s was found in %s" % (word, file_path))
				# Check the contents of the file
				with open(file_path, 'r') as file:
					try:
						lines = file.readlines()
						for line_num, line in enumerate(lines):
							# Convert everything to upper case so we will find word
							# regardless of case
							for word in word_list:
								if find_word(line, " " + word + " "):
									# Word has been found. Return the line number
									print("%s was found in %s on line %d" %(
												word, file_path, line_num))
					except:
						# Non-text file being read. Skip to the next file.
						pass

def find_word(string, word):
	""" Find word in string regardless of case
	"""
	word = word.upper()
	return string.upper().find(word) >= 0


# Run as executable
if __name__ == "__main__":
	clean_files()
