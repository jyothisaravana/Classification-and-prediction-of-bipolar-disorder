import sys
import warnings
import numpy as np
from flask import Flask, url_for,render_template,request,jsonify
import pickle
import re

if not sys.warnoptions:
    warnings.simplefilter("ignore")


app = Flask(__name__)
model = pickle.load(open('rf.pkl','rb'))


@app.route('/')
def index():
	return render_template('form.html')


def check_input(ci,ca):
   try:
       int(ci)
       int(ca)
       return True
   except (ValueError) as e:
       return False
    
    
def check_boundary(w,s):
    try:
        if re.match('[0-9]{2}:[0-9]{2}$', w) and re.match('[0-9]{2}:[0-9]{2}$', s):
            return True
    except (ValueError) as e:
        return False
    
@app.route('/process', methods=['POST'])
def process():
    patient = request.form.get('name')
    mood = request.form.get('mood')
    motivation = request.form.get('motivation')
    attention = request.form.get('attention')
    irritability = request.form.get('irritability')
    anxiety = request.form.get('anxiety')
    sleep_quantity = request.form.get('sleep_quantity')
    cigarettes = request.form.get('cig')
    caffeine = request.form.get('caf')
    wake = request.form.get('wake')
    sleep = request.form.get('sleep')
    
    if patient and mood and motivation and attention and irritability and anxiety and sleep_quantity and cigarettes and caffeine and wake and sleep:
       
        if check_input(cigarettes, caffeine):
            
            if check_boundary(wake, sleep):
                
                wake = int(wake.replace(':',''))
            
                sleep = int(sleep.replace(':',''))
                
                if sleep < wake:
                   sleep += 2400
           
                active_time = abs(wake-sleep)
                features = [mood,motivation,attention,irritability,anxiety,sleep_quantity,cigarettes,caffeine,active_time]
                data = [int(i) for i in features]
                test = np.array(data).reshape(1,-1)
                prediction = model.predict(test)
                output = prediction[0]
        
                if output == 'D':
            
                   return jsonify({'prediction' : 'The patient could be tending towards a DEPRESSION episode'})
        
                elif output == 'M':
            
                   return jsonify({'prediction' : 'The patient could be tending towards a MANIA episode'})
        
                else:
                   return jsonify({'prediction' : 'The patient is staying in a EUTHYMIC state'})
              
    return jsonify({'error' : 'Missing Data or incorrect format please recheck!'}) 

if __name__ == '__main__':
	app.run(debug=True)
