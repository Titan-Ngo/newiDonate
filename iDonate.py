#WebApp coding
import os
from flask import Flask, url_for, render_template, request
from flask import Session

app = Flask(__name__)
#http://127.0.0.1:5000/
app.secret_key='w98fw9ef8hwe98fhwee'


@app.route('/') #home page
def render_main():
    return render_template('home.html')

@app.route('/questionaire')
def render_questionaire():
    return render_template('questionaire.html')

@app.route('/eligibility') #displays if eligible or not
def render_eligibility():
    donationValues = questionaireMessage(request.args['q2'],request.args['q3'],request.args['q4'],request.args['q5'],request.args['q6'],request.args['q7'],request.args['q8'])
    return render_template('eligibility.html',statement = donationValues[0],eligibilty = donationValues[1])


@app.route('/procedures') 
def render_procedure():
    return render_template('procedures.html')


@app.route('/appointment')
def render_appointment():
    return render_template('appointment.html')

@app.route('/overview')
def render_overview():
    return render_template('overview.html')

@app.route('/notifications')
def render_notifications():
    return render_template('notifications.html')

@app.route('/hydrationtest')
def render_hydrationtest():
    return render_template('hydrationtest.html')

#functions
def questionaireMessage(q2,q3,q4,q5,q6,q7,q8):
    '''determines the messsage output based on their responses'''
    statementNotEligible = "Sorry, but you are not eligible to donate blood at this time. Please contact American Red Cross directly if you have further questions."
    statementEligible = "Congraulations! You are eligible to donate blood!"
    statementMaybeEligible = "You may still be able to donate. Please check the American Red Cross Website to see if your specific medication  is eligible."
    if "yes" in {q2, q3, q5, q7}:
        statement = statementNotEligible
        eligible = "no"
        return [statement, eligible]

    elif "no" in {q4, q6}:
        statement = statementNotEligible
        eligible = "no"
        return [statement, eligible]

    elif q8 == "yes":
        statement = statementMaybeEligible
        eligible = "yes"
        return [statement, eligible]
    
    else:
        statement = statementEligible
        eligible = "yes"
        return [statement, eligible]

def procedureRecommendation(q1,q10,q11):
    procedure1 = ""
    procedure2 = ""
    procedure3 = ""
    procedure4 = ""
    if q1 == "yes" and q10 in {'O-','O+','A-', 'B-'}:
        procedure1 = "(Recommended)"
        procedure2 = "(Highly Recommended if Height & Weight Met)"
        return [procedure1, procedure2, procedure3, procedure4]
        
    elif q11 == "no":
        procedure1 = "(Recommended)"
        return [procedure1, procedure2, procedure3, procedure4]
    
    elif q10 in {'O-','O+','A-', 'B-'}:
        procedure1 = "(Recommended)"
        procedure2 = "(Highly Recommended)"
        return [procedure1, procedure2, procedure3, procedure4]
    
    elif q10 in {'A+', 'B+'}:
        procedure1 = "(Recommended)"
        procedure3 = "(Highly Recommended)"
        return [procedure1, procedure2, procedure3, procedure4]
    
    elif q10 in {'AB+','AB-'}:
        procedure1 = "(Recommended)"
        procedure3 = "(Highly Recommended)"
        procedure4 = "(Highly Recommended)"
        return [procedure1, procedure2, procedure3, procedure4]

if __name__== "__main__":
    app.run(debug=False)

