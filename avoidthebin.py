from flask import Flask, render_template, request
from flask_navigation import Navigation
from sendemailitem import send_simple_message

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
	postcode = postcode.replace(" ","")
	postcode = postcode.upper()
	print "You are here 1"
	email = form_data["email"]
	print "still here " + email

	availableitems.append({"name": name, "food": food,"postcode": postcode, "email": email})
	print availableitems
	return render_template('itemadded.html',  user = form_data)

@app.route("/item", methods=["POST"])
def getitem():
	item_data = request.form
	food = item_data["food_item"]
	return render_template('item.html', food = food, people = getitemdetails(food))

@app.route("/contact", methods=["POST"])
def contact():
	user_data = request.form
	name = user_data["name"]
	emailfrom = user_data["email"]
	emailto = user_data.get("emailto")
	nameto = user_data.get("nameto")
	foodgone = user_data.get("food")
	print user_data
	print "you have made it here"
	send_simple_message(emailto, emailfrom, nameto, name, foodgone)
	return render_template('thanks.html', person = user_data)

if __name__ == '__main__':
	app.run(debug=True)
