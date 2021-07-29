from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db/tasks'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class shipping(db.Model):
    delivery_number = db.Column(db.Integer, primary_key=True)
    contents = db.Column(db.String(100), unique=False)
    product_value = db.Column(db.Integer)
    description = db.Column(db.String(100))
    delivered = db.column(db.Boolean, default=False)
    shipping_price = db.Column(db.Integer)

    def __init__(self, contents, product_value, description, delivered, shipping_price):
        self.contents = contents
        self.product_value = product_value
        self.description = description
        self.delivered = delivered
        self.shipping_price = shipping_price




db.create_all()



import csv

def import_data(file):
    with open(str(file)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_counter = 0
        for row in csv_reader:
            if line_counter != 0:
                c = Circle(
                    name=row[0],
                    slug_name=row[1],
                    is_public=(False if int(row[2]) == 0 else True),
                    verified=(False if int(row[3]) == 0 else True),
                    members_limit=int(row[4])
                )
                c.save()
            line_counter += 1

import_data('circles.csv')


class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)





@app.route('/tasks', methods=['Post'])
def create_task():
  title = request.json['title']
  description = request.json['description']

  new_task= Task(title, description)

  db.session.add(new_task)
  db.session.commit()

  return task_schema.jsonify(new_task)

@app.route('/tasks', methods=['GET'])
def get_tasks():
  all_tasks = Task.query.all()
  result = tasks_schema.dump(all_tasks)
  return jsonify(result)

@app.route('/tasks/<id>', methods=['GET'])
def get_task(id):
  task = Task.query.get(id)
  return task_schema.jsonify(task)

@app.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
  task = Task.query.get(id)

  title = request.json['title']
  description = request.json['description']

  task.title = title
  task.description = description

  db.session.commit()

  return task_schema.jsonify(task)

@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
  task = Task.query.get(id)
  db.session.delete(task)
  db.session.commit()
  return task_schema.jsonify(task)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to my API'})



if __name__ == "__main__":
    app.run(debug=True)