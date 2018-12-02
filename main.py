from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
correct_ans = ['7', '8', '9', '6']
requests = {}

@app.route('/')
def main_page(name=None):
    return render_template('main_page.html')

@app.route('/results')
def results():
    overall = 0
    less = 0
    if request.args:
        overall += 1
        n_corr_ans = 0
        for i in range(1, 5):
            if request.args['question_' + str(i)] == correct_ans[i - 1]:
                n_corr_ans += 1
        if n_corr_ans in requests:
            requests[n_corr_ans] += 1
        else:
            requests[n_corr_ans] = 0
        for i in requests: 
            if i < n_corr_ans:
                less += requests[i]
        perc = less / overall
        if n_corr_ans == '1':
            wordform = 'название'
        elif n_corr_ans == 2 or n_corr_ans == 3 or n_corr_ans == 4:
            wordform = 'названия'
        else:
            wordform = 'названий'
    return render_template('result_page.html', n_corr_ans = n_corr_ans, perc = perc, wordform = wordform)

if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
