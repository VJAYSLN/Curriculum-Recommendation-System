from flask import Flask, render_template, request,redirect,url_for
import http.client
conn = http.client.HTTPConnection("2factor.in")
from pymongo import MongoClient
from bson.objectid import ObjectId
client=MongoClient('localhost',27017)
db=client.test
collect=db.collect
app = Flask(__name__,static_url_path='/static')
result1=""
Session_Id=""
First_Value=11
Dataset_A=[]
Dataset_I=[]
Dataset_E=[]
Dataset_F=[]
Dataset_S=[]
worA=worI=worE=worF=worS=0
nworA=nworI=nworE=nworF=nworS=0
cyA=cyI=cyE=cyF=cyS=0
cnA=cnI=cnE=cnF=cnS=0
labyA=labyI=labyE=labyF=labyS=0
labnA=labnI=labnE=labnF=labnS=0
@app.route('/Process')
def Process():
  global Dataset_A
  global Dataset_I
  global Dataset_E
  global Dataset_F
  global Dataset_S
  li=[]
  name1=[]
  course1=[]
  client = MongoClient('localhost', 27017)
  db = client['test'] 
  collection1= db["Alumni"]
  collection2= db["Corporate/Industry"]
  collection3= db["Experts"]
  collection4= db["Faculty"]
  collection5= db["Student"]
  result1=collection1.find();
  result2=collection2.find();
  result3=collection3.find();    
  result4=collection4.find();
  result5=collection5.find();
  for doc in result1:
    if(doc['Name'] not in name1 and doc['Course'] not in course1):
      Name=doc['Name']
      Course=doc['Course']
      name1.append(Name)
      course1.append(Course)
      result1a=collection1.find({'Name':Name,'Course':Course})
      for doc2 in result1a:
          li.append(doc2['Answer'])
      Dataset_A.append(li)
  name1=[]
  course1=[]
  for doc in result2:
    if(doc['Name'] not in name1 and doc['Course'] not in course1):
      Name=doc['Name']
      Course=doc['Course']
      name1.append(Name)
      course1.append(Course)
      result1a=collection2.find({'Name':Name,'Course':Course})
      for doc2 in result1a:
          li.append(doc2['Answer'])
      Dataset_I.append(li)    
  name1=[]
  course1=[]    
  for doc in result3:
    if(doc['Name'] not in name1 and doc['Course'] not in course1):
      Name=doc['Name']
      Course=doc['Course']
      name1.append(Name)
      course1.append(Course)
      result1a=collection3.find({'Name':Name,'Course':Course})
      for doc2 in result1a:
          li.append(doc2['Answer'])
      Dataset_E.append(li)  
  name1=[]
  course1=[]
  for doc in result4:
    if(doc['Name'] not in name1 and doc['Course'] not in course1):
      Name=doc['Name']
      Course=doc['Course']
      name1.append(Name)
      course1.append(Course)
      result1a=collection4.find({'Name':Name,'Course':Course})
      for doc2 in result1a:
          li.append(doc2['Answer'])
      Dataset_F.append(li)
  name1=[]
  course1=[]    
  for doc in result5:
    if(doc['Name'] not in name1 and doc['Course'] not in course1):
      Name=doc['Name']
      Course=doc['Course']
      name1.append(Name)
      course1.append(Course)
      result1a=collection5.find({'Name':Name,'Course':Course})
      for doc2 in result1a:
          li.append(doc2['Answer'])
      Dataset_S.append(li)   
  return redirect(url_for('Worth'))
    
@app.route('/')
def Choice():
   return render_template('Home (2).html')
@app.route('/signup')
def Signup():
   return render_template('signup.html')
@app.route('/questionnaire')
def Question():
   return render_template('question.html')

@app.route('/request1')
def request1():
 payload = ""
 mobile_no =  request.args["mobile_no"]
 #db.collect.insert_one({"mobile":mobile_no,"name":mobile_no})
 headers = { 'content-type': "application/x-www-form-urlencoded" }
 conn.request("GET", "/API/V1/fe97a5fe-242c-11e8-a895-0200cd936042/SMS/"+mobile_no+"/AUTOGEN", payload, headers)
 res = conn.getresponse()
 data = res.read()
 result1=data.decode("utf-8")
 print(data.decode("utf-8"))
 a=result1.find("Success")
 if a==-1:
    return "no"
 else:
    global Session_Id
    Session_Id=result1[31:67]
    return "yes"
@app.route('/admin_login')
def admin_login():
    return render_template("admin_login1.html")
@app.route('/edit')
def Edit():
    ID=request.args['Doc']
    id=request.args['id']
    question=request.args['question']
    options=request.args['options']
    type=request.args['type']
    db=client['test']
    collection=db['collection']
    collection.update_one({'_id':ObjectId(id)},{'$set':{'ID':ID,'question':question,'options':options,'type':type}})
    return "Yes"
@app.route("/show")
def Show():
  id =  request.args["id"]
  message="""<style>
  table {
    border-collapse: collapse;
    width: 100%;
  }

  th, td {
    text-align: left;
    padding: 10px;
  } 
  #IN
  {
   text-align:center;
   vertical-align:center;
    padding: 15px;
   }    

  tr:nth-child(even){background-color: #f2f2f2}

  th {
    background-color: #4CAF50;
    color: white;
    font-size:20;
  }
    #IN {
    background-color:#FF3366;
    color: white;
    font-size:20;
    width:200;
    height:50;
  }
      #IN:hover
      {
      
      background-color:#696969;
      }
      
  input[type=text]
      {
       height:50;
       width:250;
       font-size:18;
        }   
      input[type=text]:hover
      {
       border-color:green;
        }   
      .tab2
      {
       height:50;
       width:500;
       font-size:20;
      }
      .tab2:hover
      {
      border-color:#696969;
      }
      input[type=submit]
      {
      width:120;
      height:30;
      font-size:20;
      background-color:#FF3366;
      color:white;
      border-radius:10px;
      }
       input[type=submit]:hover
       {
       color:red;
       background-color:powderblue;
       }
       #I{
       width:150;
      height:40;
      font-size:20;
      background-color:#FF3366;
      color:white;
      border-radius:10px;
       }
       #I:hover
       {
       color:red;
       background-color:powderblue;
       }
      input[type=button]
      {
      width:100;
      height:30;
      font-size:20;
      background-color:	#696969;
      color:powderblue;
      border-radius:10px;
      }
       input[type=button]:hover
       {
       color:white;
       background-color:#FF3366;
       }
    html,body,h1,h2,h3,h4,h5 {font-family: "Raleway", sans-serif}
  </style>"""
  db = client['test'] 
  collection = db["collection"]
  result=collection.find({'_id':ObjectId(id)})
  message = message + """
  <form align="right" name="form1" action="http://127.0.0.1:5000/admin_login">
      <label class="logoutLblPos">
  <input name="submit2" type="submit" id="submit2" value="log out">
  </label>
</form>


  
  <div id="first">
  <table border=1>
  
  <tr>
  <th>ObjectId</th>
  <th>ID</th>
  <th>Question</th> 
  <th>Options</th> 
  <th>Type</th> 
  <th>Select</th> 
  </tr>
  """
  
  for doc in result:
     message = message + """<tr><td>"""
     message = message + """<input type="text" value='"""+id+"""'  id="i" readonly>"""
     message = message +"""</td>"""
     message = message + """<td>"""
     message = message + """<input type="text" value='"""+doc['ID']+"""' id="j" required>"""
     message = message +"""</td>"""
     message = message + """<td>"""
     message = message + """<input type="text" value='"""+doc['question']+"""' id="q" required>"""
     message = message +"""</td>"""
     message = message + """<td>"""
     message = message + """<input type="text" value='"""+doc['options']+"""' id="o" placeholder="Seperated with Comma" required>"""
     message = message +"""</td>"""
     message = message + """<td>"""
     message = message + """<input type="text" value='"""+doc['type']+"""' id="t" required>"""
     message = message +"""</td>"""
     message = message + """<td>"""
     message=message+"""<input type="submit" id="E" value="Edit">  """ 
     message = message +"""</td></tr></table></div>"""
     
  message = message+"""<br><br><br><center><input type="button" value="InsertNew" id="IN"></tr>"""   
  message = message+"""<div hidden id="second" class="se"><table>"""
  message = message + """<tr><th>Enter Question</th>"""
  message = message + """<td><input type="text" value='' id="q1" placeholder="Eg:This is a Worthwhile Course?" required>"""
  message = message +"""</td></tr>"""
  message = message + """<tr><th>Enter Options</th>"""
  message = message + """<td><input type="text" value='' id="o1" placeholder="Seperated With Comma" required>"""
  message = message +"""</td></tr>"""   
  message = message + """<tr><th>Enter Category</th>"""
  message = message + """<td><input type="text" value='' id="t1" placeholder="Beginning with Blockletter" required>"""
  message = message +"""</td></tr></table><br><br><br>"""
 
    
  message=message+"""<center><input type="button" value="Insert" id="I"></center></div>"""
  
  
  message=message+"""<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>"""
  message=message+"""<script>
$("#E").on("click", function () {
    Doc_Id=$("#j").val();
    id=$("#i").val();
    question = $("#q").val();
    options = $("#o").val();
    type = $("#t").val();
    
   $.ajax({
           type: "GET",
           url: "edit",
           data:{'Doc':Doc_Id,'id':id,'question':question,'options':options,'type':type},
           success: function (result)
           {
               if(result=="Yes")   
               {
           alert("CHANGES WILL BE SAVED SUCCESSFULLY");
           window.location.href = 'http://127.0.0.1:5000/db';
          
                }
               else{
               alert("Some Problem is found");
               }                     
            }
     });
    });
    
$("#IN").on("click",function(){
  $('#first').hide(1000);
  $('#IN').hide(1000);
  $('#second').show();
})

$("#I").on("click", function () {
 
    question = $("#q1").val();
    options = $("#o1").val();
    type = $("#t1").val();
    
   $.ajax({
           type: "GET",
           url: "insert",
           data:{'question':question,'options':options,'type':type},
           success: function (result)
           {
               if(result=="Yes")   
               {
           alert("DATA INSERTED SUCCESSFULLY");
           window.location.href = 'http://127.0.0.1:5000/db';
          
                }
               else{
               alert("Some Problem is found");
               }                     
            }
     });
    }); 
    </script>"""
  return message 
@app.route("/insert")
def Insert():
  global First_Value
  First_Value=First_Value+1;  
  question1=request.args['question']
  options1=request.args['options']
  type1=request.args['type']
  client = MongoClient('localhost', 27017)
  db = client['test'] 
  collection = db["collection"]
  collection.insert_one({'ID':str(First_Value),'question':question1,'options':options1,'type':type1})
  return "Yes"
@app.route("/delete")
def Delete():
  id =  request.args["id"]
  #print(id)
  client = MongoClient('localhost', 27017)
  db = client['test'] 
  collection = db["collection"]
  collection.delete_one({'_id': ObjectId(id)})
  return redirect(url_for('db'))
@app.route("/surveyresults")
def SurResult():
   client = MongoClient('localhost', 27017)
   db = client['test'] 
   collection = db["collection"]
   result = collection.find()
   message="""
  
  <html lang="en">
<head>
    <meta charset="utf-8">
    
    
        <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="http://netdna.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">
    <style type="text/css">
        
.panel.with-nav-tabs .panel-heading{
    padding: 5px 5px 0 5px;
}
.panel.with-nav-tabs .nav-tabs{
	border-bottom: none;
}
.panel.with-nav-tabs .nav-justified{
	margin-bottom: -1px;
}
/********************************************************************/
/*** PANEL DEFAULT ***/
.with-nav-tabs.panel-default .nav-tabs > li > a,
.with-nav-tabs.panel-default .nav-tabs > li > a:hover,
.with-nav-tabs.panel-default .nav-tabs > li > a:focus {
    color: #777;
}
.with-nav-tabs.panel-default .nav-tabs > .open > a,
.with-nav-tabs.panel-default .nav-tabs > .open > a:hover,
.with-nav-tabs.panel-default .nav-tabs > .open > a:focus,
.with-nav-tabs.panel-default .nav-tabs > li > a:hover,
.with-nav-tabs.panel-default .nav-tabs > li > a:focus {
    color: #777;
	background-color: #ddd;
	border-color: transparent;
}
.with-nav-tabs.panel-default .nav-tabs > li.active > a,
.with-nav-tabs.panel-default .nav-tabs > li.active > a:hover,
.with-nav-tabs.panel-default .nav-tabs > li.active > a:focus {
	color: #555;
	background-color: #fff;
	border-color: #ddd;
	border-bottom-color: transparent;
}
.with-nav-tabs.panel-default .nav-tabs > li.dropdown .dropdown-menu {
    background-color: #f5f5f5;
    border-color: #ddd;
}
.with-nav-tabs.panel-default .nav-tabs > li.dropdown .dropdown-menu > li > a {
    color: #777;   
}
.with-nav-tabs.panel-default .nav-tabs > li.dropdown .dropdown-menu > li > a:hover,
.with-nav-tabs.panel-default .nav-tabs > li.dropdown .dropdown-menu > li > a:focus {
    background-color: #ddd;
}
.with-nav-tabs.panel-default .nav-tabs > li.dropdown .dropdown-menu > .active > a,
.with-nav-tabs.panel-default .nav-tabs > li.dropdown .dropdown-menu > .active > a:hover,
.with-nav-tabs.panel-default .nav-tabs > li.dropdown .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #555;
}
/********************************************************************/
/*** PANEL PRIMARY ***/
.with-nav-tabs.panel-primary .nav-tabs > li > a,
.with-nav-tabs.panel-primary .nav-tabs > li > a:hover,
.with-nav-tabs.panel-primary .nav-tabs > li > a:focus {
    color: #fff;
}
.with-nav-tabs.panel-primary .nav-tabs > .open > a,
.with-nav-tabs.panel-primary .nav-tabs > .open > a:hover,
.with-nav-tabs.panel-primary .nav-tabs > .open > a:focus,
.with-nav-tabs.panel-primary .nav-tabs > li > a:hover,
.with-nav-tabs.panel-primary .nav-tabs > li > a:focus {
	color: #fff;
	background-color: #3071a9;
	border-color: transparent;
}
.with-nav-tabs.panel-primary .nav-tabs > li.active > a,
.with-nav-tabs.panel-primary .nav-tabs > li.active > a:hover,
.with-nav-tabs.panel-primary .nav-tabs > li.active > a:focus {
	color: #428bca;
	background-color: #fff;
	border-color: #428bca;
	border-bottom-color: transparent;
}
.with-nav-tabs.panel-primary .nav-tabs > li.dropdown .dropdown-menu {
    background-color: #428bca;
    border-color: #3071a9;
}
.with-nav-tabs.panel-primary .nav-tabs > li.dropdown .dropdown-menu > li > a {
    color: #fff;   
}
.with-nav-tabs.panel-primary .nav-tabs > li.dropdown .dropdown-menu > li > a:hover,
.with-nav-tabs.panel-primary .nav-tabs > li.dropdown .dropdown-menu > li > a:focus {
    background-color: #3071a9;
}
.with-nav-tabs.panel-primary .nav-tabs > li.dropdown .dropdown-menu > .active > a,
.with-nav-tabs.panel-primary .nav-tabs > li.dropdown .dropdown-menu > .active > a:hover,
.with-nav-tabs.panel-primary .nav-tabs > li.dropdown .dropdown-menu > .active > a:focus {
    background-color: #4a9fe9;
}
/********************************************************************/
/*** PANEL SUCCESS ***/
.with-nav-tabs.panel-success .nav-tabs > li > a,
.with-nav-tabs.panel-success .nav-tabs > li > a:hover,
.with-nav-tabs.panel-success .nav-tabs > li > a:focus {
	color: #3c763d;
}
.with-nav-tabs.panel-success .nav-tabs > .open > a,
.with-nav-tabs.panel-success .nav-tabs > .open > a:hover,
.with-nav-tabs.panel-success .nav-tabs > .open > a:focus,
.with-nav-tabs.panel-success .nav-tabs > li > a:hover,
.with-nav-tabs.panel-success .nav-tabs > li > a:focus {
	color: #3c763d;
	background-color: #d6e9c6;
	border-color: transparent;
}
.with-nav-tabs.panel-success .nav-tabs > li.active > a,
.with-nav-tabs.panel-success .nav-tabs > li.active > a:hover,
.with-nav-tabs.panel-success .nav-tabs > li.active > a:focus {
	color: #3c763d;
	background-color: #fff;
	border-color: #d6e9c6;
	border-bottom-color: transparent;
}
.with-nav-tabs.panel-success .nav-tabs > li.dropdown .dropdown-menu {
    background-color: #dff0d8;
    border-color: #d6e9c6;
}
.with-nav-tabs.panel-success .nav-tabs > li.dropdown .dropdown-menu > li > a {
    color: #3c763d;   
}
.with-nav-tabs.panel-success .nav-tabs > li.dropdown .dropdown-menu > li > a:hover,
.with-nav-tabs.panel-success .nav-tabs > li.dropdown .dropdown-menu > li > a:focus {
    background-color: #d6e9c6;
}
.with-nav-tabs.panel-success .nav-tabs > li.dropdown .dropdown-menu > .active > a,
.with-nav-tabs.panel-success .nav-tabs > li.dropdown .dropdown-menu > .active > a:hover,
.with-nav-tabs.panel-success .nav-tabs > li.dropdown .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #3c763d;
}
/********************************************************************/
/*** PANEL INFO ***/
.with-nav-tabs.panel-info .nav-tabs > li > a,
.with-nav-tabs.panel-info .nav-tabs > li > a:hover,
.with-nav-tabs.panel-info .nav-tabs > li > a:focus {
	color: #31708f;
}
.with-nav-tabs.panel-info .nav-tabs > .open > a,
.with-nav-tabs.panel-info .nav-tabs > .open > a:hover,
.with-nav-tabs.panel-info .nav-tabs > .open > a:focus,
.with-nav-tabs.panel-info .nav-tabs > li > a:hover,
.with-nav-tabs.panel-info .nav-tabs > li > a:focus {
	color: #31708f;
	background-color: #bce8f1;
	border-color: transparent;
}
.with-nav-tabs.panel-info .nav-tabs > li.active > a,
.with-nav-tabs.panel-info .nav-tabs > li.active > a:hover,
.with-nav-tabs.panel-info .nav-tabs > li.active > a:focus {
	color: #31708f;
	background-color: #fff;
	border-color: #bce8f1;
	border-bottom-color: transparent;
}
.with-nav-tabs.panel-info .nav-tabs > li.dropdown .dropdown-menu {
    background-color: #d9edf7;
    border-color: #bce8f1;
}
.with-nav-tabs.panel-info .nav-tabs > li.dropdown .dropdown-menu > li > a {
    color: #31708f;   
}
.with-nav-tabs.panel-info .nav-tabs > li.dropdown .dropdown-menu > li > a:hover,
.with-nav-tabs.panel-info .nav-tabs > li.dropdown .dropdown-menu > li > a:focus {
    background-color: #bce8f1;
}
.with-nav-tabs.panel-info .nav-tabs > li.dropdown .dropdown-menu > .active > a,
.with-nav-tabs.panel-info .nav-tabs > li.dropdown .dropdown-menu > .active > a:hover,
.with-nav-tabs.panel-info .nav-tabs > li.dropdown .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #31708f;
}
/********************************************************************/
/*** PANEL WARNING ***/
.with-nav-tabs.panel-warning .nav-tabs > li > a,
.with-nav-tabs.panel-warning .nav-tabs > li > a:hover,
.with-nav-tabs.panel-warning .nav-tabs > li > a:focus {
	color: #8a6d3b;
}
.with-nav-tabs.panel-warning .nav-tabs > .open > a,
.with-nav-tabs.panel-warning .nav-tabs > .open > a:hover,
.with-nav-tabs.panel-warning .nav-tabs > .open > a:focus,
.with-nav-tabs.panel-warning .nav-tabs > li > a:hover,
.with-nav-tabs.panel-warning .nav-tabs > li > a:focus {
	color: #8a6d3b;
	background-color: #faebcc;
	border-color: transparent;
}
.with-nav-tabs.panel-warning .nav-tabs > li.active > a,
.with-nav-tabs.panel-warning .nav-tabs > li.active > a:hover,
.with-nav-tabs.panel-warning .nav-tabs > li.active > a:focus {
	color: #8a6d3b;
	background-color: #fff;
	border-color: #faebcc;
	border-bottom-color: transparent;
}
.with-nav-tabs.panel-warning .nav-tabs > li.dropdown .dropdown-menu {
    background-color: #fcf8e3;
    border-color: #faebcc;
}
.with-nav-tabs.panel-warning .nav-tabs > li.dropdown .dropdown-menu > li > a {
    color: #8a6d3b; 
}
.with-nav-tabs.panel-warning .nav-tabs > li.dropdown .dropdown-menu > li > a:hover,
.with-nav-tabs.panel-warning .nav-tabs > li.dropdown .dropdown-menu > li > a:focus {
    background-color: #faebcc;
}
.with-nav-tabs.panel-warning .nav-tabs > li.dropdown .dropdown-menu > .active > a,
.with-nav-tabs.panel-warning .nav-tabs > li.dropdown .dropdown-menu > .active > a:hover,
.with-nav-tabs.panel-warning .nav-tabs > li.dropdown .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #8a6d3b;
}
/********************************************************************/
/*** PANEL DANGER ***/
.with-nav-tabs.panel-danger .nav-tabs > li > a,
.with-nav-tabs.panel-danger .nav-tabs > li > a:hover,
.with-nav-tabs.panel-danger .nav-tabs > li > a:focus {
	color: #a94442;
}
.with-nav-tabs.panel-danger .nav-tabs > .open > a,
.with-nav-tabs.panel-danger .nav-tabs > .open > a:hover,
.with-nav-tabs.panel-danger .nav-tabs > .open > a:focus,
.with-nav-tabs.panel-danger .nav-tabs > li > a:hover,
.with-nav-tabs.panel-danger .nav-tabs > li > a:focus {
	color: #a94442;
	background-color: #ebccd1;
	border-color: transparent;
}
.with-nav-tabs.panel-danger .nav-tabs > li.active > a,
.with-nav-tabs.panel-danger .nav-tabs > li.active > a:hover,
.with-nav-tabs.panel-danger .nav-tabs > li.active > a:focus {
	color: #a94442;
	background-color: #fff;
	border-color: #ebccd1;
	border-bottom-color: transparent;
}
.with-nav-tabs.panel-danger .nav-tabs > li.dropdown .dropdown-menu {
    background-color: #f2dede; /* bg color */
    border-color: #ebccd1; /* border color */
}
.with-nav-tabs.panel-danger .nav-tabs > li.dropdown .dropdown-menu > li > a {
    color: #a94442; /* normal text color */  
}
.with-nav-tabs.panel-danger .nav-tabs > li.dropdown .dropdown-menu > li > a:hover,
.with-nav-tabs.panel-danger .nav-tabs > li.dropdown .dropdown-menu > li > a:focus {
    background-color: #ebccd1; /* hover bg color */
}
.with-nav-tabs.panel-danger .nav-tabs > li.dropdown .dropdown-menu > .active > a,
.with-nav-tabs.panel-danger .nav-tabs > li.dropdown .dropdown-menu > .active > a:hover,
.with-nav-tabs.panel-danger .nav-tabs > li.dropdown .dropdown-menu > .active > a:focus {
    color: #fff; /* active text color */
    background-color: #a94442; /* active bg color */
}
    </style>    <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
    <script src="http://netdna.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
</head>

<title>SURVEYRESULTS2018</title>
<link href='bootstrap.min.css' type='text/css'>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
<link href='https://fonts.googleapis.com/css?family=Maven+Pro' rel='stylesheet' type='text/css'>
<script src="https://apis.google.com/js/platform.js" async defer></script>
<style>

@import url(https://fonts.googleapis.com/css?family=Roboto:400,300,500);
*:focus {
  outline: none;
}
.background{
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0px;
  top: 0px;
  z-index: -1;
  -webkit-filter: blur(35px); /* Safari 6.0 - 9.0 */
  filter: blur(6px);       
    }
body {
  margin: 0;
  padding: 0;
  font-size: 16px;
  color: #DC143C;
  font-family: 'Roboto', sans-serif;
  font-weight: 300;
}

#login-box {
  position: relative;
  margin: 5% auto;
  width: 600px;
  height: 550px;
  background: #FFF;
  border-radius: 2px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
}

.left {
  position: absolute;
  top: 0;
  left: 0;
  box-sizing: border-box;
  padding: 40px;
  width: 300px;
  height: 400px;
}
#para{
  width:100%;
  height:80px;
  background-color: rgba(0,0,0,0.8);
  font-size: 21px;
  font-weight:700;
  font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color:#23717f;
  text-align: justify;
}
#para1
    {
  text-decoration: underline;
  -webkit-text-decoration-color: red; /* Safari */    
  text-decoration-color: red;
    }

h1 {
  margin: 0 0 20px 0;
  font-weight: 300;
  font-size: 28px;
}

input[type="text"],
input[type="password"] {
  display: block;
  box-sizing: border-box;
  margin-bottom: 20px;
  padding: 4px;
  width: 220px;
  height: 32px;
  border: none;
  border-bottom: 1px solid #AAA;
  font-family: 'Roboto', sans-serif;
  font-weight: 400;
  font-size: 15px;
  transition: 0.2s ease;
}

input[type="text"]:focus,
input[type="password"]:focus {
  border-bottom: 2px solid #16a085;
  color: #16a085;
  transition: 0.2s ease;
}

.submit {
  margin-top: 10px;
  width: 120px;
  height: 32px;
  background: #16a085;
  border: none;
  border-radius: 2px;
  color: #FFF;
  font-family: 'Roboto', sans-serif;
  font-weight: 500;
  text-transform: uppercase;
  transition: 0.1s ease;
  cursor: pointer;
}

.submit:hover,
.submit:focus {
  opacity: 0.8;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
  transition: 0.1s ease;
}

.submit:active {
  opacity: 1;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.4);
  transition: 0.1s ease;
}

.or {
  position: absolute;
  top: 180px;
  left: 280px;
  width: 40px;
  height: 40px;
  background: #DDD;
  border-radius: 50%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
  line-height: 40px;
  text-align: center;
}

.right {
  position: absolute;
  top: 0;
  right: 0;
  box-sizing: border-box;
  padding: 40px;
  width: 300px;
  height: 400px;
  background: url('https://goo.gl/lPCXrQ');
  background-size: cover;
  background-position: center;
  border-radius: 0 2px 2px 0;
}

.right .loginwith {
  display: block;
  margin-bottom: 40px;
  font-size: 28px;
  color: #FFF;
  text-align: center;
}

button.social-signin {
  margin-bottom: 20px;
  width: 220px;
  height: 36px;
  border: none;
  border-radius: 4px;
  color: #FFF;
  font-family: 'Roboto', sans-serif;
  font-weight: 500;
  transition: 0.2s ease;
  cursor: pointer;
}

#title{
    position:absolute;        
    width:100%;
            height:6%;
            background-color: rgba(0,0,0,0.3);
             font-weight:bold;
             font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
             font-size:30px;
             color:black;
              text-align: center;            
}

    .auto_style1 {
        flex-align:center;
        width:300px;
        height:20px;
        outline:none;
        border-radius:5px;
    }
        .auto_style1:focus {
            border-radius:5px;

        }
    table {
     //   border-collapse:collapse;
        border-spacing:25px;
    }
    select {
        border-radius:13px;
        border-width:medium;
        width:200px;
        height:25px;
        font-weight:bold;
        font-family:Cambria;
        outline:none;
    }
        select:hover {
            border-radius:13px;
            border-color:HighlightText;
        }
        select:focus {
            border-radius:13px;
            border-color:blue;
}
    


</style>

</head>
<body>
 <img class="background" src="/static/images/Psgtech.jpg" />
 <div id="title">
  CURRICULUM RECOMMENDATION SURVEY RESULTS
  </div>  
  <br><br>
 
    
  <p id="para">
  This Survey Results helps to find the better Curriculum Courses for the Students.
  This year, more and more developers told us how they learn, build their careers,
  which tools they’re using, and what they want in a job.
  </p>
  <meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

  <!-- Header -->
  <header class="w3-container" style="padding-top:22px">
    <h5><b><i class="fa fa-dashboard"></i> My Dashboard</b></h5>
  </header>
<div class="w3-row-padding w3-margin-bottom">
<div class="w3-quarter">
      <div class="w3-container w3-red w3-text-white w3-padding-16">  
        <div class="w3-left"><i class="fa fa-eye w3-xxxlarge"></i></div>
        <div class="w3-right">
          <h3>"""+str(dashboardcontent("TOTAL"))+"""</h3>
        </div>
        <div class="w3-clear"></div>
        <h4>TOTAL</h4>
      </div>
    </div>
    <div class="w3-quarter">
      <div class="w3-container w3-red w3-padding-16">
        <div class="w3-left"><i class="fa fa-users w3-xxxlarge"></i></div>
        <div class="w3-right">
       <h3>"""+str(dashboardcontent("Alumni"))+"""</h3>
        </div>
        <div class="w3-clear"></div>
        <h4>ALUMNI</h4>
      </div>
    </div>
    <div class="w3-quarter">
      <div class="w3-container w3-blue w3-padding-16">
        <div class="w3-left"><i class="fa fa-users w3-xxxlarge"></i></div>
        <div class="w3-right">
         <h3>"""+str(dashboardcontent("Corporate/Industry"))+"""</h3>
        </div>
        <div class="w3-clear"></div>
        <h4>CORPORATE/INDUSTRY</h4>
      </div>
    </div>
    <div class="w3-quarter">
      <div class="w3-container w3-teal w3-padding-16">
        <div class="w3-left"><i class="fa fa-users w3-xxxlarge"></i></div>
        <div class="w3-right">
          <h3>"""+str(dashboardcontent("Experts"))+"""</h3>
        </div>
        <div class="w3-clear"></div>
        <h4>EXPERTS</h4>
      </div>
    </div>
    <div class="w3-quarter">
      <div class="w3-container w3-orange w3-text-white w3-padding-16">
        <div class="w3-left"><i class="fa fa-users w3-xxxlarge"></i></div>
        <div class="w3-right">
          <h3>"""+str(dashboardcontent("Faculty"))+"""</h3>
        </div>
        <div class="w3-clear"></div>
        <h4>FACULTY</h4>
      </div>
    </div>
  
    <div class="w3-quarter">
      <div class="w3-container w3-teal w3-padding-16">
        <div class="w3-left"><i class="fa fa-users w3-xxxlarge"></i></div>
        <div class="w3-right">
          <h3>"""+str(dashboardcontent("Student"))+"""</h3>
        </div>
        <div class="w3-clear"></div>
        <h4>STUDENT</h4>
      </div>
    </div>
    </div>
<br><br>
<p id="para1">
<center><b>WORTHWHILE</b></center>
</p><br><br>
<div class="container">
                    <div class="row">
                            <div class="col-md-6">
                            <div class="panel with-nav-tabs panel-primary">
                                <div class="panel-heading">
                                        <ul class="nav nav-tabs">
                                                <li class="active"><a href="#tab1primary" data-toggle="tab">Alumni</a></li>
                                                <li><a href="#tab2primary" data-toggle="tab">SoftwareIndustry</a></li>
                                                <li><a href="#tab3primary" data-toggle="tab">Experts</a></li>
                                                <li><a href="#tab4primary" data-toggle="tab">Faculty</a></li>
                                                <li><a href="#tab5primary" data-toggle="tab">Student</a></li>
                                            </ul>
                                </div>
                                <div class="panel-body">
                                    <div class="tab-content">
                                        <div class="tab-pane fade in active" id="tab1primary"><b>WORTH COURSE OUT OF """+str(len(Dataset_A))+""":</b><br>
                                        WORTH:"""+str(worA)+"""<br>NotWorth:"""+str(nworA)+"""<br></div>"""
   
   message=message+"""                                        <div class="tab-pane fade" id="tab2primary"><b>WORTH COURSE OUT OF """+str(len(Dataset_I))+""":</b><br>
                                        WORTH:"""+str(worI)+"""<br>NOTWORTH:"""+str(nworI)+"""<br></div>"""
   
   message=message+"""                                  <div class="tab-pane fade" id="tab3primary"><b>WORTH COURSE OUT OF """+str(len(Dataset_E))+""":</b><br>
                                        WORTH:"""+str(worE)+"""<br>NOTWORTH:"""+str(nworE)+"""<br></div>"""
   message=message+"""                                     <div class="tab-pane fade" id="tab4primary"><b>WORTH COURSE OUT OF """+str(len(Dataset_F))+""":</b><br>
                                        WORTH:"""+str(worF)+"""<br>NOTWORTH:"""+str(nworF)+"""<br></div>"""
   message=message+"""                                     <div class="tab-pane fade" id="tab5primary"><b>WORTH COURSE OUT OF """+str(len(Dataset_S))+""":</b><br>
                                        WORTH:"""+str(worS)+"""<br>NOTWORTH:"""+str(nworS)+"""<br></div>"""
   message=message+"""                                 </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <br><br>
                <p id="para1">
                <center><b>CONTENT OF THE COURSE</b></center>
                </p><br><br>
                <div class="container">
                <div class="row">
                <div class="col-md-6">
                                <div class="panel with-nav-tabs panel-default">
                                    <div class="panel-heading">
                                            <ul class="nav nav-tabs">
                                                <li class="active"><a href="#tab1default" data-toggle="tab">Alumni</a></li>
                                                <li><a href="#tab2default" data-toggle="tab">SoftwareIndustry</a></li>
                                                <li><a href="#tab3default" data-toggle="tab">Experts</a></li>
                                                <li><a href="#tab4default" data-toggle="tab">Faculty</a></li>
                                                <li><a href="#tab5default" data-toggle="tab">Student</a></li>
                                            </ul>
                                    </div>
                                    <div class="panel-body">
                                        <div class="tab-content">
                                        <div class="tab-pane fade in active" id="tab1default"><b>WORTH COURSE OUT OF """+str(len(Dataset_A))+""":</b><br>
                                        WORTH:"""+str(cyA)+"""<br>NotWorth:"""+str(cnA)+"""<br></div>"""
   
   message=message+"""                                        <div class="tab-pane fade" id="tab2default"><b>WORTH COURSE OUT OF """+str(len(Dataset_I))+""":</b><br>
                                        WORTH:"""+str(cyI)+"""<br>NOTWORTH:"""+str(cnI)+"""<br></div>"""
   
   message=message+"""                                  <div class="tab-pane fade" id="tab3default"><b>WORTH COURSE OUT OF """+str(len(Dataset_E))+""":</b><br>
                                        WORTH:"""+str(cyE)+"""<br>NOTWORTH:"""+str(cnE)+"""<br></div>"""
   message=message+"""                                     <div class="tab-pane fade" id="tab4default"><b>WORTH COURSE OUT OF """+str(len(Dataset_F))+""":</b><br>
                                        WORTH:"""+str(cyF)+"""<br>NOTWORTH:"""+str(cnF)+"""<br></div>"""
   message=message+"""                                     <div class="tab-pane fade" id="tab5default"><b>WORTH COURSE OUT OF """+str(len(Dataset_S))+""":</b><br>
                                        WORTH:"""+str(cyS)+"""<br>NOTWORTH:"""+str(cnS)+"""<br></div>"""
   message=message+"""                                 </div>    
                                        </div>
                                    </div>
                                </div>
                            </div>
                            </div>
                            </div>
                            <div>
                                </div>
                                <br><br>
                                <p id="para1">
                                <center><b>THIRD QUESTION</b></center>
                                </p>    <br><br>                        
                                <div class="container">
                                        <div class="row">
                                            <div class="col-md-6">
                                                <div class="panel with-nav-tabs panel-success">
                                                    <div class="panel-heading">
                                                            <ul class="nav nav-tabs">
                                                                    <li class="active"><a href="#tab1success" data-toggle="tab">Alumni</a></li>
                                                                    <li><a href="#tab2success" data-toggle="tab">SoftwareIndustry</a></li>
                                                                    <li><a href="#tab3success" data-toggle="tab">Experts</a></li>
                                                                    <li><a href="#tab4success" data-toggle="tab">Faculty</a></li>
                                                                    <li><a href="#tab5success" data-toggle="tab">Student</a></li>
                                                                </ul>
                                                    </div>
                                                    <div class="panel-body">
                                                        <div class="tab-content">
                                                                    <div class="tab-pane fade in active" id="tab1success"><b>COURSE CONTENT OUT OF """+str(len(Dataset_A))+""":</b><br>
                                        WELL:"""+str(labyA)+"""<br>NOTWELL:"""+str(labnA)+"""<br></div>"""
   
   message=message+"""                                        <div class="tab-pane fade" id="tab2success"><b>COURSE CONTENT OUT OF """+str(len(Dataset_I))+""":</b><br>
                                        WELL:"""+str(labyI)+"""<br>NOTELL:"""+str(labnI)+"""<br></div>"""
   
   message=message+"""                                  <div class="tab-pane fade" id="tab3successs"><b>COURSE CONTENT OUT OF """+str(len(Dataset_E))+""":</b><br>
                                        WELL:"""+str(labyE)+"""<br>NOTWELL:"""+str(labnE)+"""<br></div>"""
   message=message+"""                                     <div class="tab-pane fade" id="tab4success"><b>COURSE CONTENT OUT OF """+str(len(Dataset_F))+""":</b><br>
                                        WELL:"""+str(labyF)+"""<br>NOTWELL:"""+str(labnF)+"""<br></div>"""
   message=message+"""                                     <div class="tab-pane fade" id="tab5success"><b>COURSE CONTENT OUT OF """+str(len(Dataset_S))+""":</b><br>
                                        WELL:"""+str(labyS)+"""<br>NOTWELL:"""+str(labnS)+"""<br></div>"""
   message=message+"""                                 </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                </div>
                                </div>
                                <br><br>
                                <p id="para1">
                                <center><b>FOURTH QUESTION</b></center>
                                </p>    <br><br>
                            <div class="container">
                            <div class="row">
                                
                                            <div class="col-md-6">
                                                <div class="panel with-nav-tabs panel-info">
                                                    <div class="panel-heading">
                                                            <ul class="nav nav-tabs">
                                                                    <li class="active"><a href="#tab1info" data-toggle="tab">Alumni</a></li>
                                                                    <li><a href="#tab2info" data-toggle="tab">SoftwareIndustry</a></li>
                                                                    <li><a href="#tab3info" data-toggle="tab">Experts</a></li>
                                                                    <li><a href="#tab4info" data-toggle="tab">Faculty</a></li>
                                                                    <li><a href="#tab5info" data-toggle="tab">Student</a></li>
                                                                </ul>
                                                    </div>
                                                    <div class="panel-body">
                                                        <div class="tab-content">
                                                            <div class="tab-pane fade in active" id="tab1info">Info 1</div>
                                                            <div class="tab-pane fade" id="tab2info">Info 2</div>
                                                            <div class="tab-pane fade" id="tab3info">Info 3</div>
                                                            <div class="tab-pane fade" id="tab4info">Info 4</div>
                                                            <div class="tab-pane fade" id="tab5info">Info 5</div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <br><br>
                                    <p id="para1">
                                    <center><b>FIRST QUESTION</b></center>
                                    </p>    <br><br>                               
                                    <div class="container">
                                        <div class="row">
                                            <div class="col-md-6">
                                                <div class="panel with-nav-tabs panel-warning">
                                                    <div class="panel-heading">
                                                            <ul class="nav nav-tabs">
                                                                    <li class="active"><a href="#tab1warning" data-toggle="tab">Alumni</a></li>
                                                                    <li><a href="#tab2warning" data-toggle="tab">SoftwareIndustry</a></li>
                                                                    <li><a href="#tab3warning" data-toggle="tab">Experts</a></li>
                                                                    <li><a href="#tab4warning" data-toggle="tab">Faculty</a></li>
                                                                    <li><a href="#tab5warning" data-toggle="tab">Student</a></li>
                                                                </ul>
                                                    </div>
                                                    <div class="panel-body">
                                                        <div class="tab-content">
                                                            <div class="tab-pane fade in active" id="tab1warning">Warning 1</div>
                                                            <div class="tab-pane fade" id="tab2warning">Warning 2</div>
                                                            <div class="tab-pane fade" id="tab3warning">Warning 3</div>
                                                            <div class="tab-pane fade" id="tab4warning">Warning 4</div>
                                                            <div class="tab-pane fade" id="tab5warning">Warning 5</div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                                <br><br>
                                                <p id="para1">
                                                <center><b>FIRST QUESTION</b></center>
                                                </p> <br><br>
                                   <div class="container">

                                    <div class="row">
                                            <div class="col-md-6">
                                                <div class="panel with-nav-tabs panel-danger">
                                                    <div class="panel-heading">
                                                            <ul class="nav nav-tabs">
                                                                    <li class="active"><a href="#tab1danger" data-toggle="tab">Alumni</a></li>
                                                                    <li><a href="#tab2danger" data-toggle="tab">SoftwareIndustry</a></li>
                                                                    <li><a href="#tab3danger" data-toggle="tab">Experts</a></li>
                                                                    <li><a href="#tab4danger" data-toggle="tab">Faculty</a></li>
                                                                    <li><a href="#tab5danger" data-toggle="tab">Student</a></li>
                                                                </ul>
                                                    </div>
                                                    <div class="panel-body">
                                                        <div class="tab-content">
                                                            <div class="tab-pane fade in active" id="tab1danger">Danger 1</div>
                                                            <div class="tab-pane fade" id="tab2danger">Danger 2</div>
                                                            <div class="tab-pane fade" id="tab3danger">Danger 3</div>
                                                            <div class="tab-pane fade" id="tab4danger">Danger 4</div>
                                                            <div class="tab-pane fade" id="tab5danger">Danger 5</div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                         </div>   


                        </body>
                        </html>"""
   return message
    

@app.route('/response')
def response():
 from pymongo import MongoClient
 client = MongoClient('localhost', 27017)
 db = client['test'] 
 collection = db["collect1"]
 mobile_no1 =  request.args["mobile_no"]
 name1 =  request.args["username"]
 email1 = request.args["email"]
 otp = request.args["otp"]
 category=request.args["category"] 
 payload = ""
 headers = { 'content-type': "application/x-www-form-urlencoded" }
 conn.request("GET", "/API/V1/fe97a5fe-242c-11e8-a895-0200cd936042/SMS/VERIFY/"+Session_Id+"/"+otp, payload, headers)
 res = conn.getresponse()
 data = res.read()
 data1=data.decode("utf-8")
 a=data1.find("Success")
 if a==-1:
    return "no"
 else:
    collection.insert_one({"username":name1,"email":email1,"MobileNo":mobile_no1,"Category":category})
    return "yes"
@app.route('/dashboardcontent')
def dashboardcontent(x):
  client = MongoClient('localhost', 27017)
  db = client['test'] 
  collection = db["collect1"]
  result = collection.find()
  i=0
  if(x!="TOTAL"):
      for doc in result:
          if(doc['Category']==x):
              i=i+1;
      return i    
  else:
      for doc in result:
          i=i+1;
      return i
@app.route('/course')
def Course():  
  #category=request.args['category']
  #domain=request.args['domain']
  #name=request.args['Name']
  category="Alumni"
  domain="DS"
  name="Bala"
  message=""
  db = client['test'] 
  collection = db["course"]
  result=collection.find()
  
  message=message+"""<link rel = "stylesheet"
   type = "text/css"
   href = "/static/css/Course_Style.css" />  """
  message = message + """
  <table border=1>
  <tr>
  <th>CourseCode</th>
  <th>CourseTitle</th> 
  </tr>
  """
  for doc in result:
     message = message + """<tr><td>"""
     message = message + doc['courseCode']
     message = message +"""</td>"""
     message = message + """<td>"""
     message = message + """ <a href='que?CourseTitle="""+ str(doc['courseTitle']) +"""&category="""+category+"""&domain="""+domain+"""&Name="""+name+"""'>"""+doc['courseTitle']+"""</a>   """
     message = message +"""</td></tr>"""
     
  return message
@app.route('/que')
def Que():
   CourseTitle=request.args['CourseTitle'] 
   category=request.args['category'] 
   domain=request.args['domain'] 
   name=request.args['Name']
   #CourseTitle="Data Structures"
   #domain="OS"
   #name="Alumni1"
   #category="Faculty"
   db=client['test']
   collection=db['collection']
   result=collection.find({'type':category})
       
   message="""<!DOCTYPE html>
   <html lang="en" >

    <head>
  <meta charset="UTF-8">
  <title>Questionnaire Form</title>
  
  </head>
  <body>
        <style type="text/css">

.background{
  width: 100%;
  height: 100%;
  position:fixed;
  left: 0px;
  top: 0px;
  z-index: -1;
  -webkit-filter: blur(35px); /* Safari 6.0 - 9.0 */
  filter: blur(3px);
      
}
#container {
  width: 80%;
  max-width: 700px;
  margin: 60px auto 0 auto;
  text-align: center;
}
#title{
  width:100%;
            height:50px;
            background-color: rgba(0,0,0,0.2);
             font-weight:bold;
             font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
             font-size:35px;
               color:hsl(hue, saturation, lightness);
              text-align: center;        
              box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);    
}
#para{
  width:100%;
  height:100px;
  background-color: rgba(0,0,0,0.8);
  font-size: 21px;
  font-weight:700;
  font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color:#23717f;
  text-align: justify;
}
#questions {
  font-family: arial;
  box-shadow: inset 2px -1px 5px 0px #ccc;
  color: #23717f;
  position: relative;
  width: 100%;
  height: 300px;
  /* border: 1px solid $light-gray; */
  border-radius: 20px;
  overflow: hidden;
  background-color: #f7f7f7;
}

#progress {
  list-style-type: none;
  display: inline-table;
  width: 100%;
  margin: 5px 0;
  padding: 0;
}
#progress li {
  display: inline-block;
  /*background-color:#fff;*/
  border: 1px solid #23717f;
  min-width: 20px;
  height: 6px;
  margin: 0 0 0 0;
  opacity: .175;
}
#progress .status {
  background-color: #a5c4c9;
}

.content {
  padding: 10px 20px;
}

.question {
  text-align: left;
  position: absolute;
  top: 5px;
  width: 100%;
  /* border:1px solid #000; */
}
.question ol {
  list-style-type: none;
  margin: 0px;
  padding: 0;
}
.question ol li {
  border-radius: 10px;
  margin: 0 0 10px 0;
  padding: 8px;
  cursor: pointer;
  -webkit-transition: all .8s ease-in-out;
}
.question ol li:hover {
  background-color: #c3ddda;
  /* color: #f2f2f2; */
}
.question ol li input {
  margin: 0 10px 0 0;
}

.buttons {
  display: block;
  width: 94%;
  padding: 0 15px 15px 15px;
  margin: 0 auto 15px auto;
  overflow: hidden;
  border-bottom: 3px dotted #ededed;
}
.buttons button {
  cursor: pointer;
}

button {
  font-family: arial;
  border-radius: 80px;
  background-color: #c3ddda;
  border: 0;
  height: 40px;
  width: 40px;
  padding: 0;
  margin: 0;
  color: #23717f;
  font-size: 30px;
  outline: none;
  /*-webkit-transition: all .5s ease-in-out;*/
}
button:hover {
  background-color: #a5c4c9;
  /*-webkit-transition: all .5s ease-in-out;*/
}

button.wide {
  border-radius: 10px;
  font-size: 16px;
  padding: 0 15px;
  width: auto;
  height: 40px;
}

#reset, #submit {
  display: block;
  float: right;
  margin-left: 10px;
}

#submit {
  /*display:none;*/
}

.disabled {
  background-color: #ededed;
  color: #ccc;
}
.disabled:hover {
  background-color: #ededed;
}

#previous {
  float: left;
}

#next {
  float: right;
}

input[type=radio] {
  display: none;
}

input[type=radio] + label span {
  display: inline-block;
  float: left;
  width: 15px;
  height: 15px;
  background-color: #a5c4c9;
  border-radius: 20px;
  border: 2px solid;
  margin: 0 10px 0 0;
  padding: 0;
  font-size: 0;
}

input[type=radio]:checked + label span {
  background-color: #23717f;
}

#error {
  display: none;
  position: absolute;
  bottom: 10px;
  left: 0;
  text-align: center;
  width: 100%;
  font-size: 12px;
}

      </style>
<body>
<img class="background" src="/static/images/cur.jpg" />
  <!-- SLIDES | SINGLE OPTION SELECTION | ADVANCE POSSIBLE AFTER ANSWER | RESPONSIVE PROGRESS BAR | PREV/NEXT WITH ARROW KEYS | NEXT WITH RETURN/ENTER KEY -->
<div id="title">
  CURRICULUM RECOMMENDATION SYSTEM
</div>
  <div id="para">
    <p>Our Department(Computer Application),has asked us to investigate for curriculum design.Your input concerning this design process will be very valueable.We would greatly appreciate if you could complete the following questionnaire. The information provided will be reviewed by staff and presented to the Board Of Studies(BOS) and will be 
    used in Planning and Designing the Curriculum.</p>
    </div>
<div id="container">
<div id="questions">
<ul id="progress">
  </ul>"""
   text_id=0;       
   for doc in result:
       text_id=text_id+1;
       message=message+"""
       <div class="question">
       <div class="content">
       <h3>"""+str(text_id)+"."+doc['question']+"""</h3><ol>"""
       opti=doc['options']
       op=opti.split(',')
       if(opti!=""):
        for doc2 in op:
           message=message+"""<li><input class="sample" type="radio"
            name="options" value='"""
           if (doc2=="Yes"): 
             message=message+"""1'><label><span>one</span></label>"""+doc2
           elif (doc2=="No"): 
             message=message+"""0'><label><span>one</span></label>"""+doc2
           elif (doc2=="(0-1)"): 
             message=message+"""1'><label><span>one</span></label>"""+doc2
           elif (doc2=="(1-2)"): 
             message=message+"""2'><label><span>one</span></label>"""+doc2
           elif (doc2=="(2-3)"): 
             message=message+"""3'><label><span>one</span></label>"""+doc2
           elif (doc2=="(3-4)"): 
             message=message+"""4'><label><span>one</span></label>"""+doc2             
           else:
             message=message+"""5'><label><span>one</span></label>"""+doc2  
           message=message+"""</li>"""
           
       else:
           message=message+"""<input type="text" size="35" class="sys" id='"""+str(text_id)+"""'>
          
           """
       message=message+"""</ol></div></div>    """
   message=message+"""
   <span id="error"></span>
</div>
<br>
<div class="buttons">
  <button id="previous"><</button>
  <button id="next" class="disabled">></button>
</div>
<div class="buttons">  
  <a href="http://127.0.0.1:5000/ThankU"><button id="submit" class="wide disabled">submit</button></a>
  <button id="reset" class="wide">reset</button>
  
</div>
</div>
<input type="hidden" value='"""+category+"""' id="type">
<input type="hidden" value='"""+domain+"""' id="domain">
<input type="hidden" value='"""+CourseTitle+"""' id="CourseTitle">
<input type="hidden" value='"""+name+"""' id="name">
"""
   message=message+"""<script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>"""
   
   message=message+"""<script>
var lastQ = "This is the last question. Try the submit button.";
var firstQ = "You are on the first question.";
var unansweredQ = "Please make a selection.";
var earlySubmit = "Please complete all questions.";
var m=0;
$("input[type='text']").val("");
/*$(document).ready( function() {
$.getJSON('https://gist.github.com/catherinemaldonado/0c72e27f347dc5204214.js', function(data) {
  for (var i = 0; i < data.questions.length; i++) {
            var question = '<h3>'+data.questions[i].question+'</h3>';
            var thisNumber = Number(i)+1;
            var answers = '<ol id="answers_'+thisNumber+'"></ol>';
            var answersID = $(answers).attr('id');
    
    var build = '<div class="question"><div class="content">'+question+'</div></div>';
    $("#questions").append(build);
  }
 });
 });*/

$(".question").css({right: '-705px'});

$("#questions div:first").addClass("active").show().animate({right: '0px'});

var questions = $("#questions > div");

for (var i = 0; i < questions.length; i++) {
  $("#progress").append("<li></li>");
}

var progressItems = $("#progress li").length;
    var percent = (1/progressItems)*92;
    $("#progress li").css("width",percent+"%");

function checkIndex (){
  
  var current = $(".active").index();
  var total = $("#questions > div").length;
  var currentNum = Number(current);
  
  $("#progress li").removeClass("status");
  $("#progress li").slice(0,currentNum).addClass("status");
  
  if (current == total){
    $("#next").addClass("disabled");
  }
  
  if (current == 1){
    $("#previous").addClass("disabled");
  }else{
    $("#previous").removeClass("disabled");
  }
  
  
}

checkIndex();


function checkChecked() {
  var current = $(".active ol input:checked");
  if ($(current).length == 1){
    $("#next").removeClass("disabled"); 
  }else{
    $("#next").addClass("disabled");
  }
  
  if ($(current).length == 1 && $(".active").index() == $("#questions > div").length){
    $("#submit").removeClass("disabled"); 
  }
  
  if ($(".active").index() == $("#questions > div").length){
      $("#next").addClass("disabled"); 
  }

}

$("#next").on("click", function () {
var Answer=""
var Answer1=""
var type=document.getElementById("type").value;
var domain=document.getElementById("domain").value;
var Course=document.getElementById("CourseTitle").value;
var Name=document.getElementById("name").value;
var ANS=(document.getElementsByTagName('h3')[m++].innerHTML);
ANS1=ANS.split(".");
ANS=ANS1[0];
console.log(ANS);


if(m==5||m==8||m==11)
{
var n=m.toString();
Answer=document.getElementById(n).value;
console.log(Answer);
  $.ajax({
           type: "GET",
           url: "AnsDB",
           data:{'table':type,'domain':domain,'Course':Course,'Ques_id':ANS,'Answer':Answer,'Name':Name},
           success: function (result)
           {
            }
     });

}
else{
var n=m.toString();
Answer1=document.querySelector('input[name =options]:checked').value;
console.log(Answer1);
 $.ajax({
           type: "GET",
           url: "AnsDB",
           data:{'table':type,'domain':domain,'Course':Course,'Ques_id':ANS,'Answer':Answer1,'Name':Name},
           success: function (result)
           {
            }
     });
  

}
$("#error").fadeOut("slow");
    if ($(this).hasClass("disabled") && $(".active").index() == $("#questions > div").length){
    
      $("#error").html(lastQ);
      $("#error").fadeIn("slow");
      return false;
    }else if ($(this).hasClass("disabled")){
      $("#error").html(unansweredQ);
      $("#error").fadeIn("slow");
      return false;
    }

    var slide = $(".active");
    var next = $(".active").next(".question");
    // SLIDE ANIMATION TRANSITION
    $(slide).animate({left: '-705px'},450).toggleClass("active");
    $(next).animate({right: '0px'},450).toggleClass("active");
  
    function resetDiv() {
      $(".active").prev(".question").css({position: "absolute",width: "100%", left: "-705px",right:"auto"});
    }

    setTimeout(resetDiv, 900);
    
    checkChecked();
    checkIndex();
    
});


$("#previous").on("click", function () {
  if ($(this).hasClass("disabled")){
      $("#error").html(firstQ);
      $("#error").fadeIn("slow");
      return false;
    }
  /*event.preventDefault()*/
  var slide = $(".active");
  var prev = $(".active").prev(".question");

  // SLIDE ANIMATION TRANSITION
  $(slide).css({left: "auto"}).animate({right: '-705px',left:'auto'},350).toggleClass("active");
  $(prev).animate({left: '0px'},450).toggleClass("active");
  $("#error").fadeOut("slow");
  checkIndex();
  checkChecked();
});

$("ol li").on("click", function () {
    var $this = $(this).find("input:radio");
    var all = $(this).parent().find("input:radio").not($this);
    var val = $this.val();

    $this.prop("checked", true);

    if ($this.prop("checked") === true) {
        all.filter(function () {
            return $(this).val() === val;
        }).prop("checked", false);
    }
  $("#error").fadeOut("slow");

  checkChecked();
});

$("#reset").on("click", function () {
  $("#error").fadeOut("slow");
  $("#submit").addClass("disabled");
  $("input:radio").each( function() {
      $(this).attr('checked',false);
  });
  checkChecked();
   $(".question").removeClass("active").css({right: '-705px',left: 'auto'});

  $("#questions div:first").fadeIn("slow").css({left: "auto"}).animate({right: '0',left:'auto'},350).toggleClass("active");
  checkIndex();
});

$(document).keyup(function(e) {
    /*checkIndex();*/
    if(e.which == 13 || e.which == 39) {
       $("#next").trigger('click');
    }else if(e.which == 37) {
       $("#previous").trigger('click');
    }
});


$("#submit").on("click", function () {
var type=document.getElementById("type").value;
var domain=document.getElementById("domain").value;
var Course=document.getElementById("CourseTitle").value;
var Name=document.getElementById("name").value;
var ANS=(document.getElementsByTagName('h3')[m++].innerHTML);
ANS1=ANS.split(".");
ANS=ANS1[0];
console.log(ANS);
var total = $("#questions > div").length;
var n=total.toString();
var Answer1=document.getElementById(n).value;

$.ajax({
           type: "GET",
           url: "AnsDB",
           data:{'table':type,'domain':domain,'Course':Course,'Ques_id':ANS,'Answer':Answer1,'Name':Name},
           success: function (result)
           {
            }
     });



console.log(Answer1);
if ($(this).hasClass("disabled")){
      $("#error").html(earlySubmit);
      $("#error").fadeIn("slow");
      return false;
    }else{
      alert("This will eventually do something awesome!");
    }
});
</script>"""
   message=message+"""<script>
   $('.sys').on("change",function() 
   {
       var current = $(".active").index();
       var total = $("#questions > div").length;
      var currentNum = Number(current);

   if(current==total)
    {  $("#submit").removeClass("disabled");
    }
     else
     {
      $("#submit").addClass("disabled");
      }
  
   if(current!=total)
    {  $("#next").removeClass("disabled");}
     else
     {
      $("#next").addClass("disabled");}
  
  if (current == 1){
    $("#previous").addClass("disabled");
    
  }else{
    $("#previous").removeClass("disabled");
  }

   })
  </script>"""
   return message 
@app.route('/AnsDB')
def AnsDB():
  table=request.args['table']  
  Ques_Id=request.args['Ques_id'] 
  Answer=request.args['Answer'] 
  domain=request.args['domain']
  Course=request.args['Course']
  Name=request.args['Name']
  client = MongoClient('localhost', 27017)
  db = client['test'] 
  collection = db[table]
  collection.insert_one({'Name':Name,'domain':domain,'Course':Course,'Ques_Id':Ques_Id,'Answer':Answer})
  return "yes"
@app.route("/db")
def db():
  client = MongoClient('localhost', 27017)
  db = client['test'] 
  collection = db["collection"]
  result = collection.find()
  message=""
  message=message+"""
  <!DOCTYPE html>
<html>
<title>ADMIN VIEW</title>
  <meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
 <body>
  <!-- Header -->
  <header class="w3-container" style="padding-top:22px">
    <h5><b><i class="fa fa-dashboard"></i> My Dashboard</b></h5>
  </header>
<div class="w3-row-padding w3-margin-bottom">
<div class="w3-quarter">
      <div class="w3-container w3-red w3-text-white w3-padding-16">  
        <div class="w3-left"><i class="fa fa-eye w3-xxxlarge"></i></div>
        <div class="w3-right">
          <h3>"""+str(dashboardcontent("TOTAL"))+"""</h3>
        </div>
        <div class="w3-clear"></div>
        <h4>TOTAL</h4>
      </div>
    </div>
    <div class="w3-quarter">
      <div class="w3-container w3-red w3-padding-16">
        <div class="w3-left"><i class="fa fa-users w3-xxxlarge"></i></div>
        <div class="w3-right">
       <h3>"""+str(dashboardcontent("Alumni"))+"""</h3>
        </div>
        <div class="w3-clear"></div>
        <h4>ALUMNI</h4>
      </div>
    </div>
    <div class="w3-quarter">
      <div class="w3-container w3-blue w3-padding-16">
        <div class="w3-left"><i class="fa fa-users w3-xxxlarge"></i></div>
        <div class="w3-right">
         <h3>"""+str(dashboardcontent("Corporate/Industry"))+"""</h3>
        </div>
        <div class="w3-clear"></div>
        <h4>CORPORATE/INDUSTRY</h4>
      </div>
    </div>
    <div class="w3-quarter">
      <div class="w3-container w3-teal w3-padding-16">
        <div class="w3-left"><i class="fa fa-users w3-xxxlarge"></i></div>
        <div class="w3-right">
          <h3>"""+str(dashboardcontent("Experts"))+"""</h3>
        </div>
        <div class="w3-clear"></div>
        <h4>EXPERTS</h4>
      </div>
    </div>
    <div class="w3-quarter">
      <div class="w3-container w3-orange w3-text-white w3-padding-16">
        <div class="w3-left"><i class="fa fa-users w3-xxxlarge"></i></div>
        <div class="w3-right">
          <h3>"""+str(dashboardcontent("Faculty"))+"""</h3>
        </div>
        <div class="w3-clear"></div>
        <h4>FACULTY</h4>
      </div>
    </div>
  
    <div class="w3-quarter">
      <div class="w3-container w3-teal w3-padding-16">
        <div class="w3-left"><i class="fa fa-users w3-xxxlarge"></i></div>
        <div class="w3-right">
          <h3>"""+str(dashboardcontent("Student"))+"""</h3>
        </div>
        <div class="w3-clear"></div>
        <h4>STUDENT</h4>
      </div>
    </div>
    </div>
    
      
"""
  collection2 = db["collect1"]
  result1 = collection2.find()
  message=message+"""
     <html lang="en">
<head>
    <meta charset="utf-8">
    <!-- This file has been downloaded from Bootsnipp.com. Enjoy! -->
    <title>Welcome</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    
        <link href="http://netdna.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">
    <style type="text/css">
        .panel.with-nav-tabs .panel-heading{
    padding: 5px 5px 0 5px;
}
.panel.with-nav-tabs .nav-tabs{
	border-bottom: none;
}
.panel.with-nav-tabs .nav-justified{
	margin-bottom: -1px;
}
        .with-nav-tabs.panel-primary .nav-tabs > li > a,
        .with-nav-tabs.panel-primary .nav-tabs > li > a:hover,
        .with-nav-tabs.panel-primary .nav-tabs > li > a:focus {
            color: #fff;
        }
        .with-nav-tabs.panel-primary .nav-tabs > .open > a,
        .with-nav-tabs.panel-primary .nav-tabs > .open > a:hover,
        .with-nav-tabs.panel-primary .nav-tabs > .open > a:focus,
        .with-nav-tabs.panel-primary .nav-tabs > li > a:hover,
        .with-nav-tabs.panel-primary .nav-tabs > li > a:focus {
            color: #fff;
            background-color: #3071a9;
            border-color: transparent;
        }
        .with-nav-tabs.panel-primary .nav-tabs > li.active > a,
        .with-nav-tabs.panel-primary .nav-tabs > li.active > a:hover,
        .with-nav-tabs.panel-primary .nav-tabs > li.active > a:focus {
            color: #428bca;
            background-color: #fff;
            border-color: #428bca;
            border-bottom-color: transparent;
        }
        .with-nav-tabs.panel-primary .nav-tabs > li.dropdown .dropdown-menu {
            background-color: #428bca;
            border-color: #3071a9;
        }
        .with-nav-tabs.panel-primary .nav-tabs > li.dropdown .dropdown-menu > li > a {
            color: #fff;   
        }
        .with-nav-tabs.panel-primary .nav-tabs > li.dropdown .dropdown-menu > li > a:hover,
        .with-nav-tabs.panel-primary .nav-tabs > li.dropdown .dropdown-menu > li > a:focus {
            background-color: #3071a9;
        }
        .with-nav-tabs.panel-primary .nav-tabs > li.dropdown .dropdown-menu > .active > a,
        .with-nav-tabs.panel-primary .nav-tabs > li.dropdown .dropdown-menu > .active > a:hover,
        .with-nav-tabs.panel-primary .nav-tabs > li.dropdown .dropdown-menu > .active > a:focus {
            background-color: #4a9fe9;
        }

    


 
-------------------Next Design-----------------
  
  table {
    border-collapse: collapse;
    width: 100%;
        }

th, td {
    text-align: left;
    padding: 8px;
}
input[type=submit]
      {
      width:100;
      height:40;
      font-size:30;
      background-color:#FF3366;
      color:white;
      border-radius:10px;
      }
      
       input[type=submit]:hover
       {
       color:red;
       background-color:powderblue;
       }
tr:nth-child(even){background-color: #f2f2f2}

th {
    background-color: #4CAF50;
    color: white;
}
    .logoutLblPos{
   position:fixed;
   right:10px;
   top:5px;
}
    
    html,body,h1,h2,h3,h4,h5 { font-family: "Times New Roman", Times, serif;}
    
    
    </style>
  
  <form align="right" name="form1" action="http://127.0.0.1:5000/admin_login">
  <label class="logoutLblPos">
  <input name="submit2" type="submit" id="submit2" value="log out">
  </label>
</form>

  <div class="container">
                    <div class="row">
                            <div class="col-md-10">
                                    <div class="panel with-nav-tabs panel-primary">
                                        <div class="panel-heading">
                                                <ul class="nav nav-tabs">
                                                    <li><a href="#tab1primary" data-toggle="tab">User</a></li>
                                                    <li class="active"><a href="#tab2primary" data-toggle="tab">Student</a></li>
                                                </ul>
                                        </div>
                                        <div class="panel-body">
                                            <div class="tab-content">
                                                <div class="tab-pane fade" id="tab1primary">"""
     
  message = message + """
  <table border=1>
  <tr backgroundcolor=green>
  <th>SNO</th>
  <th>Username</th>
  <th>EmailId</th>
  <th>MobileNo</th>
  <th>Category</th>
  </tr>
  """
  i=1
  for doc in result1:
     message = message + """<tr><td>"""
     message = message +str(i)
     message = message +"""</td>"""
     message = message + """<td>"""
     message = message + doc['username']
     message = message +"""</td>"""
     message = message + """<td>"""
     message = message + doc['email']
     message = message +"""</td>"""
     message = message + """<td>"""
     message  = message + doc['MobileNo']
     message = message +"""</td>"""
     message = message + """<td>"""
     message = message + doc['Category']
     message = message +"""</td></tr>"""
  
     i=i+1    
  message = message + """</table></body>
  </div>
  <div class="tab-pane fade in active" id="tab2primary">"""
  message = message + """
  <table border=1>
  <tr backgroundcolor=green>
  <th>ID</th>
  <th>Question</th>
  <th>Option</th>
  <th>Category</th>
  <th>Select</th>
  </tr>
  """
  i=1
  for doc in result:
     message = message + """<tr><td>"""
     message = message + str(i)
     message = message +"""</td>"""
     message = message + """<td>"""
     message = message + doc['question']
     message = message +"""</td>"""
     message = message + """<td>"""
     message  = message + doc['options']
     message = message +"""</td>"""
     message = message + """<td>"""
     message = message + doc['type']
     message = message +"""</td>"""
     message = message + """<td>"""
     message = message + """ <a href='show?id="""+ str(doc['_id']) +"""'>Edit</a> | <a href='delete?id="""+ str(doc['_id']) +"""'>delete</a>   """
     message = message +"""</td></tr>"""
     
     i=i+1
  message = message + """</table></body>"""
  message=message+"""</div>
                    </div>
                </div>
            </div>
        </div>
        </div></div>"""
  message=message+"""
     <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
    <script src="http://netdna.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>"""

  
  return message

@app.route('/ThankU')
def Thanku():
   message="""<!DOCTYPE html>
<html lang="en" >

<head>
  <meta charset="UTF-8">
  <title>Thank You Page </title>
  <link rel='stylesheet prefetch' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.5/css/bootstrap.min.css'>
  
</head>

<body>

  <div class="jumbotron text-xs-center">
  <h1 class="display-3">Thank You!</h1>
  <p class="lead"><strong>Please check your email</strong> for further instructions on how to complete your account setup.</p>
  <hr>
  <p>
    Rate Any Other Course? <a href="http://127.0.0.1:5000/course">Click here</a>
  </p>
  <p class="lead">
    <a class="btn btn-primary btn-sm" href="https://bootstrapcreative.com/" role="button">Continue to homepage</a>
  </p>
</div>
  <script src='https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js'></script>
<script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/js/bootstrap.min.js'></script>
</body>
</html>
"""
   return message
@app.route('/g_signin')
def g_signin():
    name=request.args["Mob_No"]
    #EmailId=request.args["EmailID"]
    return name
    
#cursor=collect.find()
#for doc in cursor:
 #   print(doc)
#print(collect.delete_one({"name":"BhuvanaVignesh"}))
#cursor=collect.find()
#for doc in cursor:
#    print(doc)
 
#----------------------------------------------------------------------------
#YES,NO DATA INTREPRETATION--------------------------------------------------
@app.route('/Worth')
def Worth():   
    global Dataset_A
    Dataset=Dataset_A   
    global worA
    global nworA
    i=0
    while i<len(Dataset):
        if(Dataset[i][0]=='1'):
            worA+=1
        else:
            nworA+=1
        i+=1
    global Dataset_I
    Dataset=Dataset_I   
    global worI
    global nworI
    i=0
    while i<len(Dataset):
        if(Dataset[i][0]=='1'):
            worI+=1
        else:
            nworI+=1
        i+=1
    global Dataset_E
    Dataset=Dataset_E   
    global worE
    global nworE
    i=0
    while i<len(Dataset):
        if(Dataset[i][0]=='1'):
            worE+=1
        else:
            nworE+=1
        i+=1
    global Dataset_F
    Dataset=Dataset_F   
    global worF
    global nworF
    i=0
    while i<len(Dataset):
        if(Dataset[i][0]=='1'):
            worF+=1
        else:
            nworF+=1
        i+=1
    global Dataset_S
    Dataset=Dataset_S   
    global worS
    global nworS
    i=0
    while i<len(Dataset):
        if(Dataset[i][0]=='1'):
            worS+=1
        else:
            nworS+=1
        i+=1
    return redirect(url_for('SurResult'))   
@app.route('/content')
def content():
    global Dataset_A
    global cyA
    global cnA
    Dataset=Dataset_A
    i=0
    
    while i<len(Dataset):
        if(Dataset[i][2]==1):
            cyA+=1
        else:
            cnA+=1
        i+=1
    global Dataset_I
    global cyI
    global cnI
    Dataset=Dataset_I
    i=0
    
    while i<len(Dataset):
        if(Dataset[i][2]==1):
            cyI+=1  
        else:
            cnI+=1
        i+=1        
    global Dataset_E
    global cyE
    global cnE
    Dataset=Dataset_E
    i=0
    
    while i<len(Dataset):
        if(Dataset[i][2]==1):
            cyE+=1
        else:
            cnE+=1
        i+=1        
    global Dataset_F
    global cyF
    global cnF
    Dataset=Dataset_F
    i=0
    
    while i<len(Dataset):
        if(Dataset[i][2]==1):
            cyF+=1
        else:
            cnF+=1
        i+=1 
    global Dataset_S
    global cyS
    global cnS
    Dataset=Dataset_S
    i=0
    
    while i<len(Dataset):
        if(Dataset[i][2]==1):
            cyS+=1
        else:
            cnS+=1
        i+=1
    return redirect(url_for('lab1')) 
@app.route('/lab1')
def lab1():
        global Dataset_A
        Dataset=Dataset_A
        global labyA
        global labnA
        i=0
        while i<len(Dataset):
            if(Dataset[i][3]==1):
                labyA+=1
            else:
                labnA+=1
            i+=1
        global Dataset_I
        Dataset=Dataset_I
        global labyI
        global labnI
        i=0
        while i<len(Dataset):
            if(Dataset[i][3]==1):
                labyI+=1
            else:
                labnI+=1
            i+=1
        global Dataset_E
        Dataset=Dataset_E
        global labyE
        global labnE
        i=0
        while i<len(Dataset):
            if(Dataset[i][3]==1):
                labyE+=1
            else:
                labnE+=1
            i+=1
        global Dataset_F
        Dataset=Dataset_F
        global labyF
        global labnF
        i=0
        while i<len(Dataset):
            if(Dataset[i][3]==1):
                labyF+=1
            else:
                labnF+=1
            i+=1
        global Dataset_S
        Dataset=Dataset_S
        global labyS
        global labnS
        i=0
        while i<len(Dataset):
            if(Dataset[i][3]==1):
                labyS+=1
            else:
                labnS+=1
            i+=1            
        return redirect(url_for('SurResult'))
@app.route('/precourse')
def precourse():
    Dataset=Dataset_A
    course_list=[]
    py=pn=0
    i=0
    while i<len(Dataset):
        s=str(Dataset[i][4])
        s=s.lower()
        if(s=='no' or s=='-'):
            pn+=1
        else:
            py+=1
            if(s not in course_list):
                course_list.append(Dataset[i][3])
        i+=1
    print("Precourses list\n")
    print(course_list,"\n precourse :",py,"\n No precourses required",pn)

@app.route('/lab2')
def lab2():
        Dataset=Dataset_A
        i=0
        laby=labn=0
        while i<len(Dataset):
            if(Dataset[i][6]==1):
                laby+=1
            else:
                labn+=1
            i+=1
        
@app.route('/suggest2')
def suggest2():
    Dataset=Dataset_A
    course_list=[]
    py=pn=0
    i=0
    while i<len(Dataset):
        s=str(Dataset[i][7])
        s=s.lower()
        if(s=='no' or s=='-'):
            pn+=1
        else:
            py+=1
            if(s not in course_list):
                course_list.append(Dataset[i][3])
        i+=1
    print("\n\nOther course Suggestion\n")
    print(course_list,"\nSuggested:",py,"\nNot suggested:",pn)
@app.route('/lab2')
def lab3():
        Dataset=Dataset_A
        i=0
        laby=labn=0
        while i<len(Dataset):
            if(Dataset[i][9]==1):
                laby+=1
            else:
                labn+=1
            i+=1
        print("\n\nLab for this course\nOut of ",len(Dataset))
        print("lab needed",laby,"\nNot needed",labn)    
@app.route('/prereq2')
def prereq2():
        Dataset=Dataset_A
        course_list=[]
        py=pn=0
        i=0
        while i<len(Dataset):
            s=str(Dataset[i][10])
            s=s.lower()
            if(s=='no' or s=='-'):
                pn+=1
            else:
                py+=1
                if(s not in course_list):
                    course_list.append(Dataset[i][3])
            i+=1
        print("Precourses list\n")
        print(course_list,"\n precourse :",py,"\n No precourses required",pn)

if __name__ == '__main__':
  
    app.run(debug = True)