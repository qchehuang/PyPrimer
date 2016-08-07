import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.transforms as mtransforms
import matplotlib.text as mtext

from mmap import mmap,ACCESS_READ
from xlrd import open_workbook

class MyExcel():
    def __init__(self,file_name):
        self.file_name = file_name

    def open_excel(self):
        
	#with open(file_name,'rb') as f:
        #print open_workbook(
        #	file_contents=mmap(f.fileno(),0,access=ACCESS_READ)
        #)
        aString = open(self.file_name,'rb').read()
        wb = open_workbook(file_contents=aString)
        return wb

class MyLine(lines.Line2D):
    def __init__(self, *args, **kwargs):
        # we'll update the position when the line data is set
        self.text = mtext.Text(0, 0, '')
        lines.Line2D.__init__(self, *args, **kwargs)

        # we can't access the label attr until *after* the line is
        # inited
        self.text.set_text(self.get_label())

    def set_figure(self, figure):
        self.text.set_figure(figure)
        lines.Line2D.set_figure(self, figure)

    def set_axes(self, axes):
        self.text.set_axes(axes)
        lines.Line2D.set_axes(self, axes)

    def set_transform(self, transform):
        # 2 pixel offset
        texttrans = transform + mtransforms.Affine2D().translate(2, 2)
        self.text.set_transform(texttrans)
        lines.Line2D.set_transform(self, transform)

    def set_data(self, x, y):
        if len(x):
            self.text.set_position((x[-1], y[-1]))

        lines.Line2D.set_data(self, x, y)

    def draw(self, renderer):
        # draw my label at the end of the line with 2 pixel offset
        lines.Line2D.draw(self, renderer)
        self.text.draw(renderer)

fig, ax = plt.subplots()
x, y = np.random.rand(2, 10)
print x
print y

x = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
y = np.array([0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1])

myExcel = MyExcel('test.xlsx')
wb = myExcel.open_excel()

#aString = open('test.xlsx','rb').read()
#wb = open_workbook(file_contents=aString)

i = 1
for s in wb.sheets():
    #print 'Sheet:',s.name
    for row in range(s.ncols):
        values = []
        i = i+1
	for col in range(2,s.nrows):
		values.append(s.cell(col,row).value)
	#print values
	print i
	if (i == 3):
		x = np.array(values)
		print x
	if (i == 4):
		y = np.array(values)
		print y 
    print 

line = MyLine(x, y, mfc='green', ms=12, label='line label')

line.text.set_color('red')
line.text.set_fontsize(16)
ax.add_line(line)

plt.show()
