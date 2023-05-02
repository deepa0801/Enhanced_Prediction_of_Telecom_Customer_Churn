classifier.save("telcom_churn.h5")
from flask import Flask,render_template,request
import keras
from keras.models import load_model
app = Flask(__name__)
model = load_model("telcom_churn.h5")
@app.route('/')# rendering the html template
def home():
  return render_template('home.html')
#testing on random input values
print("Prediction on random input")
ann_pred_own = classifier.predict(sc.tarnform([[0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,456,1,10,3245,4567]]))
print(ann_pred_own)
ann_pred_own = (ann_pred_own)
print("output is:",ann_pred_own)
@app.route('/')
def helloworld():
  return rendder_template("base.html")
@app.route('/assesment')
def prediction():
  return render_template("index.html")
@app.route('/predict',methods=['POST'])
def admin():
  a=request.form["gender"]
  if(a=='f'):
    a=0
  if(a=='m'):
    a=1

  b=request.form["scrition"]
  if(b=='n'):
    b=0
  if(b=='y'):
    b=1
  c=request.form["partner"]
  if(c=='n'):
    c=0
  if(c=='y'):
    c=1
  d=request.form["dependents"]
  if(d=='n'):
    d=0
  if(d=='y'):
    d=1
  e=request.form["tenure"]
  f=request.form["phservics"]
  if(f=='n'):
    f=0
  if(f=='y'):
    f=1
  g=request.form["multi"]
  if(g=='n'):         

11,12,13=1,0,0
if(1=='nis'):
  11,12,13=0,1,0
if(1=='y'):
  11,12,13=0,0,1


m= request.form["stv"]
if(m=='n'):
  m1,m2,m3=1,0,0
if(m=='y'):
  m1,m2,m3=0,1,0
if(m=='y'):
  m1,m2,m3=0,0,1
n= request.form["smv"]
if(n=='n'):
  n1,n2,n3=1,0,0
if(n=='nis'):
  n1,n2,n3=0,0,1
if(n=='y'):
  n1,n2,n3=0,0,1
o= request.form["contract"]
if(o=='mtm'):
  o1,o2,o3=1,0,0
if(o=='oyr'):
  o1,o2,o3=1,0,0
if(o=='tyrs'):
  o1,o2,o3=0,0,1
p =request,form["pmt"]
if(p=='ec'):
  p1,p2,p3,p4=1,0,0,0
if(p=='mail'):
  p1,p2,p3,p4=0,1,0,0,
if(p=='bt'):
  p1,p2,p3,p4=0,0,1,0
if(p=='cc'):
  p1,p2,p3,p4=0,0,0,1

q= request.form["plb"]
if(q=='n'):              
if(g=='n'):
  g1,g2,g3=1,0,0
if(g=='nps'):
  g1,g2,g3=0,1,0
if(g=='y'):
  g1,g2,g3=0,0,1
h=request.form["is"]
if(h=='dsl'):
  h11,h2,h3=0,0,0
if(h=='fo'):
  h1,h2,h3=0,0,1
if(h=='n'):
  h1,h2,h3=0,0,1
i= request.form["os"]
if(i=='n'):
  i1,i2,i3=1,0,0,
if(i=='nis'):
  i1,i2,i3=0,0,1
if(i=='y'):
  i1,i2,i3=0,0,1
j= request.form["ob"]
if(j=='n'):
  j1,j2,j3=1,0,0
if(j=='y'):
  j1,j2,j3=0,1,0:
if(j=='y'):
  j1,j2,j3=0,0,1


k= request.form["dp"]
if(k=='n'):
  k1,k2,k3=1,0,0
if(k=='nis'):
  k1,k2,k3=0,1,0
if(k=='y'):
  k1,k2,k3=0,0,1
l= request.form["ts"]
if(l=='n'):
  l1,l2,l3=1,0,0                    

q=request.form["plb"]
if(q=='n'):
  q=0
if(q=='y'):
  q=1
r=request.form["mcharges"]
s=request.form["tcharges"]
t=[[int(g1),int(g2),int(g3),int(h1),int(h2),int(h3),int(il),int(i2),int(i3),int(j1))]]
print(t)
x=model.predict(t)
print(x[0])
if(x[[0]]<=0.5):
  y="No"
  return render_template("predno.html", z = y)
if(x[[0]]<=0.5):
  y="Yes"
  return render_template("predyes.html", z = y)   
 
