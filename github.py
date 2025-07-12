from flask import Flask

github=Flask(name)

@github.route("/info")
def myinfo():
	return "i am satwika"


@github.route("/phone")
def myphone():
	return "1234567890"

github.run(host="0.0.0.0")