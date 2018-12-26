# 太阳黑子
# 数据文件获取地址 ftp://ftp.swpc.noaa.gov/pub/weekly/Predict.txt
from urllib.request import urlopen
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF, renderSVG

# 采集并处理数据
url = 'ftp://ftp.swpc.noaa.gov/pub/weekly/Predict.txt'
comment_chars = '#:'
data = []
for line in urlopen(url).readlines():
    line = line.decode()
    if not line.isspace() and line[0] not in comment_chars:
        data.append([float(n) for n in line.split()])
pred = [row[2] for row in data]
high = [row[3] for row in data]
low = [row[4] for row in data]
times = [row[0] + row[1] / 12.0 for row in data]

# 绘图
#   绘制对话框
drawing = Drawing()  # 绘制图像400x200的对话框
lp = LinePlot()  #
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [
    list(zip(times, pred)),
    list(zip(times, high)),
    list(zip(times, low))
]
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green
drawing.add(lp)
drawing.add(String(250, 150, 'Sunspots', fontSize=14, fillColor=colors.black))
renderPDF.drawToFile(drawing, 'report.pdf', '文件标题')  # 写到文件中
"""
其它可绘图包
PYX
Matplotlib/pylab
"""
