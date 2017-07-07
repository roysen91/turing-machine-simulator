from Tape import Tape
from ExecuteTM import ExecuteTM
import os
import subprocess

class VisualTM:

	def __init__(self):
		self._viewername = None
		self.styles = "\\tikzstyle{NodeStyle}=[] \n\
\\tikzstyle{EdgeStyle}=[]"
		self.commands = ""
		self.header = '\\documentclass{beamer}\n\
\\usepackage{tikz}\n\
\\usepackage{fp}\n\
\\def \\step{0.5}\n\
% define the bounding box\n\
\\def \\boundb{(-4,-2.5) rectangle (4,2.5)}\n\
\\def \\band{[step=0.5cm](-4,-0.5) grid (4,0)}\n\
\\def \\triangle{(0,0.25) -- (0.5,0.25) -- (0.25,0) -- cycle}\n\
\\def \\state{(0,0.25) rectangle (0.5,0.75)}\n\
\\begin{document}\n'

		self.slide ='\\begin{{frame}}\n\
\\frametitle{{Turingmaschine}}\n\
\\begin{{center}}\n\
\\begin{{tikzpicture}}[trim left=0,trim right=0] \n\
\\draw \\boundb; \n\
\\clip \\boundb; \n\
\\draw \\band; \n\
\\draw \\triangle;\n\
\\draw \\state;\n\
\\node at (0.25,0.5) {{{0}}};\n\
\\node at (-3,2) {{Steps: {1}}};\n\
\\def \\start  {{0.25}}\n\
\\FPeval{{start}}{{start-step*{2}}}\n\
\\foreach \\bit in {3}{{\n\
\\node at (\\start,-0.25) {{\\bit}};\n\
\\FPeval{{start}}{{start+step}}\n\
\\xdef\start{{\start}}% make \\xb global\n\
}}\n\
\\end{{tikzpicture}}\n\
\\end{{center}}\n\
\\end{{frame}}\n'

		self.footer = '\\end{document}\n'


		
	def write_file(self,sequence):
		'''
		create a new slide for each step of DTM 
		'''
		# check if file has been created or create new file
		if not os.path.isfile('out.tex'):
			os.system('touch out.tex')
		with open('out.tex','w') as f:
			f.write(self.header)
			for i,step in enumerate(sequence):
				f.write(self.slide.format('{$'+step[2]+'$}','{'+str(i+1)+'}',str(step[1]),'{'+','.join(bit for bit in step[0])+'}'))
			f.write(self.footer)
		#os.system('/Library/TeX/texbin/pdflatex out.tex')
		os.system('pdflatex out.tex')

	def visualize(self):
		#os.system('cd output')
		
		os.system('open out.pdf')


	def set_viewer(self, viewername):
		self._viewername = viewername
