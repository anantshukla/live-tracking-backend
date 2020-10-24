from flask import Flask, jsonify, request
from Backend import app,db,mail
from Backend.models import User, Location, Locationdetails, locationDetailsSchemas, nextLocationDetailsSchemas
import datetime, time
import pytz

from flask_cors import CORS, cross_origin
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/api", methods=["GET"])
@cross_origin()
def apiTest():
    return jsonify({'status':True, 'message':'Server Works.'})

###################### API for signup ############################
@app.route("/signup", methods=["POST"])
@cross_origin()
def signup():
    ###################### API Validation #########################
    if User.query.filter_by(email = request.form.get('email')).first():
        return jsonify({'status':False, 'message': 'Username already exist! Please choose another username.'})

    if User.query.filter_by(phoneno = request.form.get('mobile')).first():
        return jsonify({'status':False, 'message':'Mobile no already exist!'})

    ##################### Logic for sign up ############################
    if request.form.get('password') == request.form.get('confirmpassword'):
        dob = datetime.datetime.strptime(request.form.get('dob'), '%d/%m/%Y').date()
        user = User(email=request.form.get('email'), password=request.form.get('password'), name=request.form.get('name'), phoneno=request.form.get('mobile'), dob=dob, sex=request.form.get('sex'))
        db.session.add(user)
        db.session.commit()
        return jsonify({'status':True, 'message':f"Successfully Registered {request.form.get('email')}."})

    else:
        return jsonify({'status':False, 'message':'Password is mismatch!!!'})


################### API for Login #########################
@app.route('/login',methods=["POST"])
@cross_origin()
def login():
    if User.query.filter_by(email=request.form.get('email'), password=request.form.get('password')).first():
        user = User.query.filter_by(email=request.form.get('email')).first()
        return jsonify({'status':True, 'message':'Login success.','name':user.name,'id':user.empID})

    else:
        return jsonify({'status':False, 'message':'Authentication failed!! Please check your credential'})

################### API for changing password #####################
@app.route('/changepassword',methods=['POST'])
@cross_origin()
def changepassword():
    user = User.query.filter_by(email=request.form.get('email')).first()
    if user:
        if user.email==request.form.get('email') and user.password==request.form.get('password'):
            if request.form.get('newpassword') == request.form.get('reenterpassword'):
                user.password = request.form.get('newpassword')
                db.session.commit()
                return jsonify({'status':True,'message':'Password updated successfully.'})

            return jsonify({'status':False,'message':"Password didn't match"})

        return jsonify({'status':False,'message':'Please enter correct password'})

    return jsonify({'status':False,'message':f"No user with {request.form.get('email')} exist"})



##################### API for forget password #######################
@app.route('/forgetpassword', methods=['POST'])
@cross_origin()
def forgetpassword():
    if session.get(request.form.get('email')) and request.form.get('otp'):
        if int(request.form.get('otp'))==session[request.form.get('email')]:
            session.pop(request.form.get('email'),None)
            return jsonify({'status':True, 'message':'OTP matched'})

        return jsonify({'status':False, 'message':'Wrong OTP!'})

    elif request.form.get('match'):
        if request.form.get('newpassword')==request.form.get('confirmpassword'):
                user = User.query.filter_by(email=request.form.get('email')).first()
                user.password = request.form.get('newpassword')
                db.session.commit()
                return jsonify({'status':True, 'message':'Password changed.'})

        return jsonify({'status':False, 'message':'Password is mismatch!!!'})
    else:
        if User.query.filter_by(email=request.form.get('email')).first():
            user = User.query.filter_by(email=request.form.get('email')).first()
            otp = random.randint(111111,999999)
            session[request.form.get('email')]=otp
            msg = Message(
                "OTP for password recovery.",
                recipients = [user.email]
            )
            msg.body = f'Hi {user.name} OTP for password recovery is "{otp}"'
            mail.send(msg)
            return jsonify({'status':True, 'message':'Please check your mail for OTP.'})
        else:
            return jsonify({'status':False, 'message':f"No user with {request.form.get('email')}"})



@app.route('/getlocation',methods=['POST'])
@cross_origin()
def getlocation():
    start_time = time.time()
    location = Locationdetails.query.all()
    serializeLocation = locationDetailsSchemas.dump(location)
    finalData = dict()
    for item in serializeLocation:
        empID = item['empID']
        del(item['empID'])
        loc = item['CurrentLocation']
        #test
        x = loc.split(", ")
        loc_lat = float(x[0]) - 0.04
        loc_long = float(x[1]) - 0.04
        # print(type(loc_lat))
        #float(x)
        #test
        del(item['CurrentLocation'])
        item['routes']=[[loc_lat, loc_long, '09:30', 'Sample Address 1']]
        item['distance'] = 1
        finalData[empID] = item

    return jsonify({'status':True,'time_to_process':time.time()-start_time,'drivers':finalData})


@app.route('/getnextlocation',methods=['POST'])
@cross_origin()
def getnextlocation():
    start_time = time.time()
    location = Locationdetails.query.all()
    serializeLocation = nextLocationDetailsSchemas.dump(location)
    finalData = dict()
    for item in serializeLocation:
        empID = item['empID']
        del(item['empID'])
        item['NextDeliveryLocation'] = item['CurrentLocation']
        item['eta_nextlocation'] = "08:00" #temp
        item['NextDeliveryAddress'] = "Sample Address 1" #temp
        now = datetime.datetime.now()
        item['current_time'] = str(now.hour)+':'+str(now.minute)
        finalData[empID] = item

    return jsonify({'status':True,'time_to_process':time.time()-start_time,'drivers':finalData})



@app.route('/setlocation',methods=['POST'])
@cross_origin()
def setlocation():
    if request.form.get('empID'):
        if Location.query.filter_by(empID=int(request.form.get('empID'))).first():
            locationData = Location.query.filter_by(empID=int(request.form.get('empID'))).first()
            locationData.CurrentLocation = request.form.get('location')
            locationData.LastUpdated = datetime.datetime.now(pytz.timezone('Asia/Calcutta'))
            locationData.BatteryStatus = int(request.form.get('battery'))
            db.session.commit()
            return jsonify({'status':True,'message':'Location updated successfully'})

        else:
            location = Location(CurrentLocation = request.form.get('location'),LastUpdated=datetime.datetime.now(),BatteryStatus=int(request.form.get('battery')),empID=int(request.form.get('empID')))
            db.session.add(location)
            db.session.commit()
            return jsonify({'status':True,'message':'Location updated succesfully'})

    return jsonify({'status':False,'message':'Employee id is needed!!'})
