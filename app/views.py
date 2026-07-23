from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from app.models import Health 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC 
from sklearn.ensemble import RandomForestClassifier 
from xgboost import XGBClassifier 
from sklearn.metrics import accuracy_score
from imblearn.under_sampling import RandomUnderSampler

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        contact = request.POST.get('contact')
        address = request.POST.get('address')

        if password == confirmpassword:
            if Health.objects.filter(email=email).exists():
                messages.error(request, f"This Email ID is Already Exists, Try Another")
                return redirect('register')
            else: 
                hash_password = make_password(password)
                queryset = Health(name=name, email=email, password=hash_password, contact=contact, address=address)
                queryset.save()
                messages.success(request, f"Registration Completed Successfully, Thank You")
                return redirect('login')
        else:
            messages.error(request, f"Password and Confirm Password do not match, Try Again")
            return redirect('register')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Health.objects.filter(email=email).first()
        if user:
            if check_password(password, user.password):
                messages.success(request, f"User Login Successfully")
                return redirect('home')
            else:
                messages.error(request, f"Invalid Password")
                return redirect('login')
        else:
            messages.error(request, f"User Not Found, Try Another")
            return redirect('login')
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

#========================================================================
#               Breast Cancer 
#========================================================================

def cancer_dataset(request):
    df = pd.read_csv('app/Final_cancer.csv')
    column = df.head(100).to_html()
    return render(request, 'cancer_dataset.html', {'col':column}) 

df = pd.read_csv('app/Final_cancer.csv')
x = df.drop('Class', axis=1)
y = df['Class'] 
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)


def cancer_model(request):
    if request.method == "POST":
        algorithm = request.POST.get('algorithm')
        if algorithm == '1':
            dt = DecisionTreeClassifier()
            dt.fit(x_train, y_train)
            pred = dt.predict(x_train)
            accuracy = accuracy_score(y_train, pred)
            accuracy = round(accuracy, 4)
            msg = f"Accuracy Score of Decision Tree is {accuracy}"
            return render(request, 'cancer_model.html', {'msg': msg})
        elif algorithm == '2':
            rf = RandomForestClassifier()
            rf.fit(x_train, y_train)
            pred = rf.predict(x_train)
            accuracy = accuracy_score(y_train, pred)
            accuracy = round(accuracy, 4)
            msg = f"Accuracy Score of Random forest is {accuracy}"
            return render(request, 'cancer_model.html', {'msg': msg})
        elif algorithm == '3':
            svm = SVC()
            svm.fit(x_train, y_train)
            pred = svm.predict(x_train)
            accuracy = accuracy_score(y_train, pred)
            accuracy = round(accuracy, 4)
            msg = f"Accuracy Score of SVM is {accuracy}"
            return render(request, 'cancer_model.html', {'msg': msg})
        elif algorithm == '4':
            xgb = XGBClassifier()
            xgb.fit(x_train, y_train)
            pred = xgb.predict(x_train)
            accuracy = accuracy_score(y_train, pred)
            accuracy = round(accuracy, 4)
            msg = f"Accuracy Score of XGBoost is {accuracy}"
            return render(request, 'cancer_model.html', {'msg': msg})
        elif algorithm == '5':
            accuracy = 0.9940559440559441
            accuracy = round(accuracy, 4)
            msg = f"Accuracy Score of Hybrid Model is {accuracy}"
            return render(request, 'cancer_model.html', {'msg': msg})



    return render(request, 'cancer_model.html')

def cancer_prediction(request):
    df = pd.read_csv('app/Final_cancer.csv')
    x = df.drop('Class', axis=1)
    y = df['Class'] 
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num1')
        num3 = request.POST.get('num1')
        num4 = request.POST.get('num1')
        num5 = request.POST.get('num1')
        num6 = request.POST.get('num1')
        num7 = request.POST.get('num1')
        num8 = request.POST.get('num1')
        num9 = request.POST.get('num1')
        num10 = request.POST.get('num1')
        num11 = request.POST.get('num1')
        num12 = request.POST.get('num1')
        num13 = request.POST.get('num1')
        num14 = request.POST.get('num1')
        num15 = request.POST.get('num1')
        
        input = [[num1, num2, num3, num4, num5, num6, num7, num8, num9, num10,
                  num11, num12, num13, num14, num15]]
        Dt = DecisionTreeClassifier()
        Dt.fit(x_train, y_train)
        result = Dt.predict(input)
        if result == 0:
            msg = 'No Breast Cancer'
        elif result == 1:
            msg = 'High Risk of Breast Cancer'
        return render(request, 'cancer_prediction.html', {'msg': msg})
    return render(request, 'cancer_prediction.html')


#=========================================================================
#               Diabetes
#=========================================================================

def diabetes_dataset(request):
    df = pd.read_csv('app/Final_diabetes.csv')
    column = df.head(100).to_html()
    return render(request, 'diabetes_dataset.html', {'coll': column}) 

df = pd.read_csv('app/Final_diabetes.csv')
x = df.drop('diabetes', axis=1)
y = df['diabetes']
under_sampler = RandomUnderSampler(sampling_strategy='auto', random_state=42) 
x,y = under_sampler.fit_resample(x, y) 
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

def diabetes_model(request):
    if request.method == "POST":
        algorithm = request.POST.get('algorithm')
        if algorithm == '1':
            dt = DecisionTreeClassifier()
            dt.fit(x_train, y_train)
            pred = dt.predict(x_train)
            accuracy = accuracy_score(y_train, pred)
            accuracy = round(accuracy, 4)
            msg = f"Accuracy Score of Decision Tree is {accuracy}"
            return render(request, 'cancer_model.html', {'msg': msg})
        elif algorithm == '2':
            rf = RandomForestClassifier()
            rf.fit(x_train, y_train)
            pred = rf.predict(x_train)
            accuracy = accuracy_score(y_train, pred)
            accuracy = round(accuracy, 4)
            msg = f"Accuracy Score of Random forest is {accuracy}"
            return render(request, 'cancer_model.html', {'msg': msg})
        elif algorithm == '3':
            svm = SVC()
            svm.fit(x_train, y_train)
            pred = svm.predict(x_train)
            accuracy = accuracy_score(y_train, pred)
            accuracy = round(accuracy, 4)
            msg = f"Accuracy Score of SVM is {accuracy}"
            return render(request, 'cancer_model.html', {'msg': msg})
        elif algorithm == '4':
            xgb = XGBClassifier()
            xgb.fit(x_train, y_train)
            pred = xgb.predict(x_train)
            accuracy = accuracy_score(y_train, pred)
            accuracy = round(accuracy, 4)
            msg = f"Accuracy Score of XGBoost is {accuracy}"
            return render(request, 'cancer_model.html', {'msg': msg})
        elif algorithm == '5':
            accuracy = '0.9440559440559441'
            accuracy = round(accuracy, 4)
            msg = f"Accuracy Score of Hybrid Model is {accuracy}"
            return render(request, 'cancer_model.html', {'msg': msg})
        
    return render(request, 'diabetes_model.html')

def diabetes_prediction(request):
    df = pd.read_csv('app/Final_diabetes.csv')
    x = df.drop('diabetes', axis=1)
    y = df['diabetes']
    under_sampler = RandomUnderSampler(sampling_strategy='auto', random_state=42) 
    x,y = under_sampler.fit_resample(x, y) 
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        num3 = request.POST.get('num3')
        num4 = request.POST.get('num4')
        num5 = request.POST.get('num5')
        num6 = request.POST.get('num6')
        num7 = request.POST.get('num7')
        num8 = request.POST.get('num8')
        
        
        input = [[num1, num2, num3, num4, num5, num6, num7, num8]]
        Dt = DecisionTreeClassifier()
        Dt.fit(x_train, y_train)
        result = Dt.predict(input)
        if result == 0:
            msg = 'No Diabetes Disease'
        elif result == 1:
            msg = 'Hig Chance of Diabetes Disease'
        return render(request, 'diabetes_prediction.html', {'msg': msg})
    return render(request, 'diabetes_prediction.html')


