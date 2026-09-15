from cc import chart
from flask import Flask, render_template, request,send_file
import openpyxl as xl
import random
def get_sheet_names(file_path):
  wb = xl.load_workbook(file_path)
  sheet_names = wb.sheetnames
  return sheet_names
keys=get_sheet_names('time.xlsx')
app = Flask(__name__)

@app.route('/download', methods=['GET', 'POST'])
def download():
  return send_file('out.pdf',as_attachment=True)
  
@app.route('/', methods=['GET', 'POST'])
def index():
    global keys
    if request.method == 'POST':
      nos = request.form['countInput']
      mList=[]
      for i in range(int(nos)):
        mList.append(request.form[f'option{i+1}'])
      chart(mList)
      return render_template('Chart.html')
    return render_template('index.html', options=keys)

if __name__ == '__main__':
    app.run(
		host='0.0.0.0',
		port=random.randint(2000,9000)
	)
