from flask import Flask, request, redirect, url_for, render_template, request
from flask import session as login_session
from databases import query_all_north, createSession, addNorth, query_all_south, query_all_east, query_all_west, query_by_user, add_user


app = Flask(__name__)
app.secret_key = "SECRET_KEY"

@app.route('/')
def test():
	if not 'logged_in' in login_session:
		login_session['logged_in'] = False
	return render_template("homePage.html", log=login_session['logged_in'])

@app.route('/login', methods= ['GET','POST'])
def login():
	if request.method == 'POST':
		user = query_by_user(request.form['username'], request.form["password"])
		if user != None:
			login_session['name'] = user.username
			login_session['logged_in'] = True
			return render_template('homePage.html')
		else:
			return render_template("index.html")
	else:
		return render_template("index.html")

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
    	username = request.form['username']
    	password = request.form['password']
    	add_user(username, password)
    	return render_template('homePage.html')
    else:
    	return render_template('signup.html')

@app.route('/logged-in')
def logged_in():
    return render_template('profile.html')

@app.route('/logout' , methods=['POST'])
def logout():
    login_session['name'] = None
    login_session['logged_in'] = False
    return render_template('homePage.html', log=str(False))

@app.route('/north')
def north():
	allLocationsnorth = query_all_north()
	return render_template("north.html", allLocationsnorth=allLocationsnorth)

@app.route('/south')
def south():
	allLocationssouth = query_all_south()
	return render_template("south.html",allLocationssouth=allLocationssouth )

@app.route('/east')
def east():
	allLocationseast = query_all_east()
	return render_template("east.html",allLocationseast=allLocationseast)

@app.route('/west')
def west():
	allLocationswest= query_all_west()
	return render_template("west.html",allLocationssouth=allLocationseast)

@app.route('/admin')
	def admin():
		return render_template("admin.html")



if __name__ == '__main__':
    app.run(debug=True)
