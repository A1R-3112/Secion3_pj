import pickle
import sqlite3
import pandas as pd
import os
from flask import Flask, render_template, request

app = Flask(__name__)

path = os.path.join(os.getcwd(), 'database/monitor.db')
path_model = os.path.join(os.getcwd(), 'model/monitor_score.pkl')
path_le = os.path.join(os.getcwd(), 'model/labelencoding.pkl')


conn = sqlite3.connect(path)
cur = conn.cursor()

query = "SELECT * FROM Monitor_score"
df = pd.read_sql(query, conn).drop('index', axis = 1)

pipe = None
le = None

with open(path_model, 'rb') as file:
    pipe = pickle.load(file)

with open(path_le, 'rb') as file:
    le = pickle.load(file)



@app.route('/', methods = ['POST', 'GET'])
def home():

    return render_template('test.html')


@app.route('/test', methods = ['POST', 'GET'])
def main():
    insert = pd.DataFrame(columns = ['화면크기', '최대 해상도', '최대 주사율', '패널', '곡면형', '응답속도'])

    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']

    X_test = [data1, data2, int(data3), data4, data5, float(data6)]

    for i in range(6):
        insert.loc[0, insert.columns[i]] = X_test[i]
        
    y_pred = pipe.predict([insert.iloc[0]])
    score = le.inverse_transform(y_pred)[0]
    max_star = df[(df['성능점수'] == score) & (df['화면크기'] == X_test[0]) & (df['최대 해상도'] == X_test[1]) & (df['최대 주사율'] == X_test[2]) & (df['패널'] == X_test[3]) & (df['곡면형'] == X_test[4]) & (df['응답속도'] == X_test[5])]['별점'].max()
        
    recommend = df[(df['성능점수'] == score) & (df['별점'] == max_star) & (df['화면크기'] == X_test[0]) & (df['최대 해상도'] == X_test[1]) & (df['최대 주사율'] == X_test[2]) & (df['패널'] == X_test[3]) & (df['곡면형'] == X_test[4])].상품명.to_list()
    
    return render_template('after.html', data = recommend)	

"""
@app.route('/home/test', methods = ['POST'])
def test():

    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']

    arr = np.array([[data1, data2, data3, data4]])
    pred = model.predict(arr)
   
    return render_template('after.html', data=pred)
"""



if __name__ == '__main__':
    app.run(debug = True)


