from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, abort
from werkzeug.datastructures import ImmutableMultiDict
import os
import json

app = Flask(__name__)
api = Api(app)

class getDrinks(Resource):
    def get(self):
        f = open("./drinks.json", "r", encoding="utf-8")
        data = json.load(f)
        args = request.args
        ingredients = args.getlist('in')
        
        if len(ingredients) > 30:
            abort(404, message="list too long")

        
        names = []
        for x in data:
            isComplete = True
            for y in x.get('ingredients'):
                if (y.get('ingredient')):
                    if (y.get('ingredient').lower().replace(" ","") not in ingredients):
                        isComplete = False
            if (isComplete):    
                names.append(x)


        return jsonify({"recipes": names})

api.add_resource(getDrinks, '/')

if __name__ == '__main__':
    app.run(debug=True, port=8000)