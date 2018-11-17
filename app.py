from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def index():
    return render_template('details.html')
@app.route("/send",methods=['POST','GET'])
def send():

    if(request.method=='POST'):
        getname=request.form['name']
        getregno=request.form['regno']
        getcollege=request.form['college']
        getsem=request.form['sem']
        getsub1=request.form['sub1']
        getsub1m=request.form['sub1m']
        getsub2=request.form['sub2']
        getsub2m=request.form['sub2m']
        getsub3=request.form['sub3']
        getsub3m=request.form['sub3m']
        getsub4=request.form['sub4']
        getsub4m=request.form['sub4m']
        
        malayalam_mark = int(getsub1)
        malayalam_maxmark = int(getsub1m)
        english_mark = int(getsub2)
        english_maxmark = int(getsub2m)
        maths_mark = int(getsub3)
        maths_maxmark = int(getsub3m)
        computer_mark = int(getsub4)
        computer_maxmark = int(getsub4m)
        
        percent_malayalam = malayalam_mark/malayalam_maxmark*100
        percent_english = english_mark/english_maxmark*100
        percent_maths = maths_mark/maths_maxmark*100
        percent_computer = computer_mark/computer_maxmark*100

        slist=[percent_malayalam,percent_english,percent_maths,percent_computer]

        result_list=[]
        
        for i in slist:
                
                if i>=50 and i<58:
                        
                        grade='D+'
                        result='Pass'
                
                elif i>=58 and i<65:
                        
                        grade='C'
                        result='Pass'
                
                elif i>=65 and i<72:
                        
                        grade='C+'
                        result='Pass'

                elif i>=72 and i<79:
                        
                        grade='B'
                        result='Pass'

                elif i>=79 and i<86:
                        
                        grade='B+'
                        result='Pass'

                elif i>=86 and i<93:
                        
                        grade='A'
                        result='Pass'

                elif i>=93 and i<=100:
                        
                        grade='A+'
                        result='Pass'
                
                else:
                        grade='D'
                        result='Fail'

                

                result_list.append(grade)
                result_list.append(result)

        for j in result_list:

                if j=='Fail':
                        semester_result='Fail'
                        break
                else:
                        semester_result='Pass'
        
        
        return render_template('/results.html',final_result=semester_result,list=result_list,a=getname,b=getregno,c=getsem,d=getcollege,e=getsub1,e1=getsub1m,f=getsub2,f1=getsub2m,g=getsub3,g1=getsub3m,h=getsub4,h1=getsub4m)

if(__name__=='__main__'):
        app.run(debug=True)