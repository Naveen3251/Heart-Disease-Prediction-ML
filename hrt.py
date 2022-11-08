'''age
sex
chest pain type (4 values)
resting blood pressure
serum cholestoral in mg/dl
fasting blood sugar > 120 mg/dl
resting electrocardiographic results (values 0,1,2)
maximum heart rate achieved
exercise induced angina
oldpeak = ST depression induced by exercise relative to rest
the slope of the peak exercise ST segment
number of major vessels (0-3) colored by flourosopy
thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
The names and social security numbers of the patients were recently removed from the database, replaced with dummy values.'''
import streamlit as st
import pickle as pk
model=pk.load(open('Heart.pkl','rb'))
def run():
    st.title("HEART DISEASE PREDICTION")
    st.image('heart.jpg')
    #name
    name=st.text_input("ENTER YOUR NAME")
    #age
    age=st.number_input("Age",min_value=18,step=1)
    #sex
    s=("Male","Female")
    op1=list(range(len(s)))
    sex=st.selectbox("Gender",op1,format_func=lambda x:s[x])
    #chest pain
    c=("NO","Less","Medium","high")
    op2=list(range(len(c)))
    chest=st.selectbox("Chest Pain",op2,format_func=lambda x:c[x])
    #resting blood pressure
    b=st.number_input("Resting Blood Pressure",min_value=90)
    #serum cholestrol level
    se=st.number_input("Serum Cholestrol Level mg/dl",min_value=120)
    #fbs
    f=("<=120 mg/dl",">120 mg/dl")
    op4=list(range(len(f)))
    fbs=st.selectbox("Fasting Blood Sugar",op4,format_func=lambda x:f[x])
    #resting electro cardiographic res
    rest=st.number_input("Resting Electrocardiograph",min_value=0,max_value=2)
    #maximum heat rate achived
    h=st.number_input("Maximum Heart Rate Achieved",min_value=65,step=1)
    #exag
    e=("No","Yes")
    op5=list(range(len(e)))
    exer=st.selectbox("Exercise Induced Agina",op5,format_func=lambda x:e[x])
    #old peak
    old=st.number_input("ST segment",value=0)
    #slope
    slope=st.number_input("Slope of ST segment",min_value=0,max_value=2,step=1)
    #ca
    ves=st.number_input("Number of major vessels",min_value=0,max_value=4,step=1)
    #thal
    t=("normal","fixed defect","reversable defect","other defect")
    op6=list(range(len(t)))
    thal=st.selectbox("Defect",op6,format_func=lambda x:t[x])

    if st.button("SUBMIT"):
        lis = [[age, sex, chest, b, se, fbs, rest, h, exer, old, slope, ves, thal]]
        prediction = model.predict(lis)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans==0:
            st.success("Hello"+name+" || "
                   "You are Alright!!!")
        else:
            st.error("Hello"+name+" || "
                   "Don't painc You get Heart Disease"
                    "Follow the Doctor's Prescription")
run()
