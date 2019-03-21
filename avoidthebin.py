from flask import Flask, render_template, request
from flask_navigation import Navigation

app = Flask("AvoidTheBin")
nav = Navigation(app)

nav.Bar('top', [
	nav.Item('Home', 'home'),
    nav.Item('List It', 'listit'),
    nav.Item('Listed', 'listed'),
])

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/listit")
def listit():
	return render_template("listit.html")

availableitems = []

def getuniquefood():
	i = 0
	x = []
	while i < len(availableitems):
		if availableitems[i]["food"] not in x:
			x.append(availableitems[i]["food"])
		i += 1
	return x

def getitemdetails(food):
	i = 0
	a = []
	while i < len(availableitems):
		if availableitems[i]["food"] == food:
			a.append(availableitems[i])
		i += 1
	print a
	return a


@app.route("/listed")
def listed():
	print getuniquefood
	return render_template('listed.html', listed = getuniquefood())


@app.route("/added", methods=["POST"])
def list_it():
	form_data = request.form
	name = form_data["name"]
	food = form_data["food"]
	postcode = form_data["postcode"]

	availableitems.append({"name": name, "food": food,"postcode": postcode})
	return render_template('itemadded.html',  user = form_data)

@app.route("/item", methods=["POST"])
def getitem():
	form_data = request.form
	food = form_data["food_item"]
	return render_template('item.html', food = food, people = getitemdetails(food))


app.run(debug=True)
