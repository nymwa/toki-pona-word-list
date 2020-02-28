import sys

head = '''\\documentclass[a4paper,10pt]{article}
\\usepackage[top=3mm,bottom=3mm, left=6mm,right=6mm]{geometry}
\\usepackage{graphics}
\\usepackage{framed}
\\usepackage{multicol}
\\usepackage{xltxtra}
\\usepackage{zxjatype}
\\setjamainfont{Noto Sans CJK JP}
\\usepackage{lscape}
\\pagestyle{empty}
\\begin{document}
\\begin{landscape}
\\centering
\\scalebox{0.97}{
\\begin{tabular}{|c|c||c|c||c|c|}'''

tail = '''\\hline
\\end{tabular}
}
\\end{landscape}
\\end{document}'''

if __name__ == '__main__':
	lines = sys.stdin.read().splitlines()
	column_len = len(lines) // 3
	arr = [lines[column_len * i : column_len * (i+1)] for i in range(3)]
	arr = list(zip(*arr))
	print(head)
	for row in arr:
		tmp = []
		for x in row:
			word, defi = x.split('\t')
			defi = defi.replace(',', ' \\ ')
			tmp.append('{} & {}'.format(word, defi))
		tmp = ' & '.join(tmp)
		tmp = '\\hline ' + tmp + ' \\\\'
		print(tmp)
	print(tail)

