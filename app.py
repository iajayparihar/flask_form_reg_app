from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'  # Change this to a random secret key for production

class StudentRegistrationForm(FlaskForm):
    name = StringField('Name')
    age = IntegerField('Age') 
    mob = IntegerField('Mobile')
    submit = SubmitField('Register')

students = []

@app.route('/', methods=['GET', 'POST'])
def index():
    form = StudentRegistrationForm()

    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        mob = form.mob.data

        student = {'name': name, 'age': age, 'mobile':mob}
        print(student)
        students.append(student)

        flash(f'{name} registered successfully!', 'success')
        flash(f'Given age is :- {age} ', 'danger')

        return redirect(url_for('index'))

    return render_template('index.html', form=form, students=students)



@app.route('/update/<name>',methods=['GET','POST'])
def update(name):
    for person in students:
        if person['name'] == name:
            data = person
            print(f"{data=}")
            break

    #----post-------
    if request.method == "POST":
        for person in students:
            if person['name'] == name:
                person['name'] = request.form.get("name")
                person['age'] = request.form.get("age")
                person['mobile'] = request.form.get("mobile")

        print(f"{students=}")
        return redirect("/")

    #-------get-------
    return render_template('update.html',student=data)

@app.route("/delete/<name>",methods=['GET','POST'])
def delete(name):
    for person in students:
        if person['name'] == name:
            students.remove(person)
            break
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
