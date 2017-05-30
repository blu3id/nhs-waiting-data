from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import flask_restless, os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)

class IncompleteCommissioner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    region_code = db.Column(db.String(80))
    ccg_code = db.Column(db.String(80))
    ccg_name = db.Column(db.String(120))
    treatment_function_code = db.Column(db.String(80))
    treatment_function_name = db.Column(db.String(120))
    total_incomplete = db.Column(db.Integer)
    total_within_18 = db.Column(db.Integer)
    total_with_dta = db.Column(db.Integer)

    total_waiting_1 = db.Column(db.Integer)
    total_waiting_2 = db.Column(db.Integer)
    total_waiting_3 = db.Column(db.Integer)
    total_waiting_4 = db.Column(db.Integer)
    total_waiting_5 = db.Column(db.Integer)
    total_waiting_6 = db.Column(db.Integer)
    total_waiting_7 = db.Column(db.Integer)
    total_waiting_8 = db.Column(db.Integer)
    total_waiting_9 = db.Column(db.Integer)
    total_waiting_10 = db.Column(db.Integer)
    total_waiting_11 = db.Column(db.Integer)
    total_waiting_12 = db.Column(db.Integer)
    total_waiting_13 = db.Column(db.Integer)
    total_waiting_14 = db.Column(db.Integer)
    total_waiting_15 = db.Column(db.Integer)
    total_waiting_16 = db.Column(db.Integer)
    total_waiting_17 = db.Column(db.Integer)
    total_waiting_18 = db.Column(db.Integer)
    total_waiting_19 = db.Column(db.Integer)
    total_waiting_20 = db.Column(db.Integer)
    total_waiting_21 = db.Column(db.Integer)
    total_waiting_22 = db.Column(db.Integer)
    total_waiting_23 = db.Column(db.Integer)
    total_waiting_24 = db.Column(db.Integer)
    total_waiting_25 = db.Column(db.Integer)
    total_waiting_26 = db.Column(db.Integer)
    total_waiting_27 = db.Column(db.Integer)
    total_waiting_28 = db.Column(db.Integer)
    total_waiting_29 = db.Column(db.Integer)
    total_waiting_30 = db.Column(db.Integer)
    total_waiting_31 = db.Column(db.Integer)
    total_waiting_32 = db.Column(db.Integer)
    total_waiting_33 = db.Column(db.Integer)
    total_waiting_34 = db.Column(db.Integer)
    total_waiting_35 = db.Column(db.Integer)
    total_waiting_36 = db.Column(db.Integer)
    total_waiting_37 = db.Column(db.Integer)
    total_waiting_38 = db.Column(db.Integer)
    total_waiting_39 = db.Column(db.Integer)
    total_waiting_40 = db.Column(db.Integer)
    total_waiting_41 = db.Column(db.Integer)
    total_waiting_42 = db.Column(db.Integer)
    total_waiting_43 = db.Column(db.Integer)
    total_waiting_44 = db.Column(db.Integer)
    total_waiting_45 = db.Column(db.Integer)
    total_waiting_46 = db.Column(db.Integer)
    total_waiting_47 = db.Column(db.Integer)
    total_waiting_48 = db.Column(db.Integer)
    total_waiting_49 = db.Column(db.Integer)
    total_waiting_50 = db.Column(db.Integer)
    total_waiting_51 = db.Column(db.Integer)
    total_waiting_52 = db.Column(db.Integer)
    total_waiting_52_plus = db.Column(db.Integer)

    total_with_dta_1 = db.Column(db.Integer)
    total_with_dta_2 = db.Column(db.Integer)
    total_with_dta_3 = db.Column(db.Integer)
    total_with_dta_4 = db.Column(db.Integer)
    total_with_dta_5 = db.Column(db.Integer)
    total_with_dta_6 = db.Column(db.Integer)
    total_with_dta_7 = db.Column(db.Integer)
    total_with_dta_8 = db.Column(db.Integer)
    total_with_dta_9 = db.Column(db.Integer)
    total_with_dta_10 = db.Column(db.Integer)
    total_with_dta_11 = db.Column(db.Integer)
    total_with_dta_12 = db.Column(db.Integer)
    total_with_dta_13 = db.Column(db.Integer)
    total_with_dta_14 = db.Column(db.Integer)
    total_with_dta_15 = db.Column(db.Integer)
    total_with_dta_16 = db.Column(db.Integer)
    total_with_dta_17 = db.Column(db.Integer)
    total_with_dta_18 = db.Column(db.Integer)
    total_with_dta_19 = db.Column(db.Integer)
    total_with_dta_20 = db.Column(db.Integer)
    total_with_dta_21 = db.Column(db.Integer)
    total_with_dta_22 = db.Column(db.Integer)
    total_with_dta_23 = db.Column(db.Integer)
    total_with_dta_24 = db.Column(db.Integer)
    total_with_dta_25 = db.Column(db.Integer)
    total_with_dta_26 = db.Column(db.Integer)
    total_with_dta_27 = db.Column(db.Integer)
    total_with_dta_28 = db.Column(db.Integer)
    total_with_dta_29 = db.Column(db.Integer)
    total_with_dta_30 = db.Column(db.Integer)
    total_with_dta_31 = db.Column(db.Integer)
    total_with_dta_32 = db.Column(db.Integer)
    total_with_dta_33 = db.Column(db.Integer)
    total_with_dta_34 = db.Column(db.Integer)
    total_with_dta_35 = db.Column(db.Integer)
    total_with_dta_36 = db.Column(db.Integer)
    total_with_dta_37 = db.Column(db.Integer)
    total_with_dta_38 = db.Column(db.Integer)
    total_with_dta_39 = db.Column(db.Integer)
    total_with_dta_40 = db.Column(db.Integer)
    total_with_dta_41 = db.Column(db.Integer)
    total_with_dta_42 = db.Column(db.Integer)
    total_with_dta_43 = db.Column(db.Integer)
    total_with_dta_44 = db.Column(db.Integer)
    total_with_dta_45 = db.Column(db.Integer)
    total_with_dta_46 = db.Column(db.Integer)
    total_with_dta_47 = db.Column(db.Integer)
    total_with_dta_48 = db.Column(db.Integer)
    total_with_dta_49 = db.Column(db.Integer)
    total_with_dta_50 = db.Column(db.Integer)
    total_with_dta_51 = db.Column(db.Integer)
    total_with_dta_52 = db.Column(db.Integer)
    total_with_dta_52_plus = db.Column(db.Integer)

class IncompleteProvider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    region_code = db.Column(db.String(80))
    provider_code = db.Column(db.String(80))
    provider_name = db.Column(db.String(120))
    is_provider = db.Column(db.Boolean)
    treatment_function_code = db.Column(db.String(80))
    treatment_function_name = db.Column(db.String(120))
    total_incomplete = db.Column(db.Integer)
    total_within_18 = db.Column(db.Integer)
    total_with_dta = db.Column(db.Integer)

    total_waiting_1 = db.Column(db.Integer)
    total_waiting_2 = db.Column(db.Integer)
    total_waiting_3 = db.Column(db.Integer)
    total_waiting_4 = db.Column(db.Integer)
    total_waiting_5 = db.Column(db.Integer)
    total_waiting_6 = db.Column(db.Integer)
    total_waiting_7 = db.Column(db.Integer)
    total_waiting_8 = db.Column(db.Integer)
    total_waiting_9 = db.Column(db.Integer)
    total_waiting_10 = db.Column(db.Integer)
    total_waiting_11 = db.Column(db.Integer)
    total_waiting_12 = db.Column(db.Integer)
    total_waiting_13 = db.Column(db.Integer)
    total_waiting_14 = db.Column(db.Integer)
    total_waiting_15 = db.Column(db.Integer)
    total_waiting_16 = db.Column(db.Integer)
    total_waiting_17 = db.Column(db.Integer)
    total_waiting_18 = db.Column(db.Integer)
    total_waiting_19 = db.Column(db.Integer)
    total_waiting_20 = db.Column(db.Integer)
    total_waiting_21 = db.Column(db.Integer)
    total_waiting_22 = db.Column(db.Integer)
    total_waiting_23 = db.Column(db.Integer)
    total_waiting_24 = db.Column(db.Integer)
    total_waiting_25 = db.Column(db.Integer)
    total_waiting_26 = db.Column(db.Integer)
    total_waiting_27 = db.Column(db.Integer)
    total_waiting_28 = db.Column(db.Integer)
    total_waiting_29 = db.Column(db.Integer)
    total_waiting_30 = db.Column(db.Integer)
    total_waiting_31 = db.Column(db.Integer)
    total_waiting_32 = db.Column(db.Integer)
    total_waiting_33 = db.Column(db.Integer)
    total_waiting_34 = db.Column(db.Integer)
    total_waiting_35 = db.Column(db.Integer)
    total_waiting_36 = db.Column(db.Integer)
    total_waiting_37 = db.Column(db.Integer)
    total_waiting_38 = db.Column(db.Integer)
    total_waiting_39 = db.Column(db.Integer)
    total_waiting_40 = db.Column(db.Integer)
    total_waiting_41 = db.Column(db.Integer)
    total_waiting_42 = db.Column(db.Integer)
    total_waiting_43 = db.Column(db.Integer)
    total_waiting_44 = db.Column(db.Integer)
    total_waiting_45 = db.Column(db.Integer)
    total_waiting_46 = db.Column(db.Integer)
    total_waiting_47 = db.Column(db.Integer)
    total_waiting_48 = db.Column(db.Integer)
    total_waiting_49 = db.Column(db.Integer)
    total_waiting_50 = db.Column(db.Integer)
    total_waiting_51 = db.Column(db.Integer)
    total_waiting_52 = db.Column(db.Integer)

class CompleteCommissioner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    admitted = db.Column(db.Boolean)
    region_code = db.Column(db.String(80))
    ccg_code = db.Column(db.String(80))
    ccg_name = db.Column(db.String(120))
    treatment_function_code = db.Column(db.String(80))
    treatment_function_name = db.Column(db.String(120))
    total_complete = db.Column(db.Integer)
    total_complete_within_18 = db.Column(db.Integer)

    total_complete_in_1 = db.Column(db.Integer)
    total_complete_in_2 = db.Column(db.Integer)
    total_complete_in_3 = db.Column(db.Integer)
    total_complete_in_4 = db.Column(db.Integer)
    total_complete_in_5 = db.Column(db.Integer)
    total_complete_in_6 = db.Column(db.Integer)
    total_complete_in_7 = db.Column(db.Integer)
    total_complete_in_8 = db.Column(db.Integer)
    total_complete_in_9 = db.Column(db.Integer)
    total_complete_in_10 = db.Column(db.Integer)
    total_complete_in_11 = db.Column(db.Integer)
    total_complete_in_12 = db.Column(db.Integer)
    total_complete_in_13 = db.Column(db.Integer)
    total_complete_in_14 = db.Column(db.Integer)
    total_complete_in_15 = db.Column(db.Integer)
    total_complete_in_16 = db.Column(db.Integer)
    total_complete_in_17 = db.Column(db.Integer)
    total_complete_in_18 = db.Column(db.Integer)
    total_complete_in_19 = db.Column(db.Integer)
    total_complete_in_20 = db.Column(db.Integer)
    total_complete_in_21 = db.Column(db.Integer)
    total_complete_in_22 = db.Column(db.Integer)
    total_complete_in_23 = db.Column(db.Integer)
    total_complete_in_24 = db.Column(db.Integer)
    total_complete_in_25 = db.Column(db.Integer)
    total_complete_in_26 = db.Column(db.Integer)
    total_complete_in_27 = db.Column(db.Integer)
    total_complete_in_28 = db.Column(db.Integer)
    total_complete_in_29 = db.Column(db.Integer)
    total_complete_in_30 = db.Column(db.Integer)
    total_complete_in_31 = db.Column(db.Integer)
    total_complete_in_32 = db.Column(db.Integer)
    total_complete_in_33 = db.Column(db.Integer)
    total_complete_in_34 = db.Column(db.Integer)
    total_complete_in_35 = db.Column(db.Integer)
    total_complete_in_36 = db.Column(db.Integer)
    total_complete_in_37 = db.Column(db.Integer)
    total_complete_in_38 = db.Column(db.Integer)
    total_complete_in_39 = db.Column(db.Integer)
    total_complete_in_40 = db.Column(db.Integer)
    total_complete_in_41 = db.Column(db.Integer)
    total_complete_in_42 = db.Column(db.Integer)
    total_complete_in_43 = db.Column(db.Integer)
    total_complete_in_44 = db.Column(db.Integer)
    total_complete_in_45 = db.Column(db.Integer)
    total_complete_in_46 = db.Column(db.Integer)
    total_complete_in_47 = db.Column(db.Integer)
    total_complete_in_48 = db.Column(db.Integer)
    total_complete_in_49 = db.Column(db.Integer)
    total_complete_in_50 = db.Column(db.Integer)
    total_complete_in_51 = db.Column(db.Integer)
    total_complete_in_52 = db.Column(db.Integer)

class CompleteProvider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    admitted = db.Column(db.Boolean)
    is_provider = db.Column(db.Boolean)
    region_code = db.Column(db.String(80))
    provider_code = db.Column(db.String(80))
    provider_name = db.Column(db.String(120))
    treatment_function_code = db.Column(db.String(80))
    treatment_function_name = db.Column(db.String(120))
    total_complete = db.Column(db.Integer)
    total_complete_within_18 = db.Column(db.Integer)

    total_complete_in_1 = db.Column(db.Integer)
    total_complete_in_2 = db.Column(db.Integer)
    total_complete_in_3 = db.Column(db.Integer)
    total_complete_in_4 = db.Column(db.Integer)
    total_complete_in_5 = db.Column(db.Integer)
    total_complete_in_6 = db.Column(db.Integer)
    total_complete_in_7 = db.Column(db.Integer)
    total_complete_in_8 = db.Column(db.Integer)
    total_complete_in_9 = db.Column(db.Integer)
    total_complete_in_10 = db.Column(db.Integer)
    total_complete_in_11 = db.Column(db.Integer)
    total_complete_in_12 = db.Column(db.Integer)
    total_complete_in_13 = db.Column(db.Integer)
    total_complete_in_14 = db.Column(db.Integer)
    total_complete_in_15 = db.Column(db.Integer)
    total_complete_in_16 = db.Column(db.Integer)
    total_complete_in_17 = db.Column(db.Integer)
    total_complete_in_18 = db.Column(db.Integer)
    total_complete_in_19 = db.Column(db.Integer)
    total_complete_in_20 = db.Column(db.Integer)
    total_complete_in_21 = db.Column(db.Integer)
    total_complete_in_22 = db.Column(db.Integer)
    total_complete_in_23 = db.Column(db.Integer)
    total_complete_in_24 = db.Column(db.Integer)
    total_complete_in_25 = db.Column(db.Integer)
    total_complete_in_26 = db.Column(db.Integer)
    total_complete_in_27 = db.Column(db.Integer)
    total_complete_in_28 = db.Column(db.Integer)
    total_complete_in_29 = db.Column(db.Integer)
    total_complete_in_30 = db.Column(db.Integer)
    total_complete_in_31 = db.Column(db.Integer)
    total_complete_in_32 = db.Column(db.Integer)
    total_complete_in_33 = db.Column(db.Integer)
    total_complete_in_34 = db.Column(db.Integer)
    total_complete_in_35 = db.Column(db.Integer)
    total_complete_in_36 = db.Column(db.Integer)
    total_complete_in_37 = db.Column(db.Integer)
    total_complete_in_38 = db.Column(db.Integer)
    total_complete_in_39 = db.Column(db.Integer)
    total_complete_in_40 = db.Column(db.Integer)
    total_complete_in_41 = db.Column(db.Integer)
    total_complete_in_42 = db.Column(db.Integer)
    total_complete_in_43 = db.Column(db.Integer)
    total_complete_in_44 = db.Column(db.Integer)
    total_complete_in_45 = db.Column(db.Integer)
    total_complete_in_46 = db.Column(db.Integer)
    total_complete_in_47 = db.Column(db.Integer)
    total_complete_in_48 = db.Column(db.Integer)
    total_complete_in_49 = db.Column(db.Integer)
    total_complete_in_50 = db.Column(db.Integer)
    total_complete_in_51 = db.Column(db.Integer)
    total_complete_in_52 = db.Column(db.Integer)

class NewCommissioner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    region_code = db.Column(db.String(80))
    ccg_code = db.Column(db.String(80))
    ccg_name = db.Column(db.String(120))
    treatment_function_code = db.Column(db.String(80))
    treatment_function_name = db.Column(db.String(120))
    total_started = db.Column(db.Integer)

class NewProvider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    region_code = db.Column(db.String(80))
    provider_code = db.Column(db.String(80))
    provider_name = db.Column(db.String(120))
    is_provider = db.Column(db.Boolean)
    treatment_function_code = db.Column(db.String(80))
    treatment_function_name = db.Column(db.String(120))
    total_started = db.Column(db.Integer)


manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(IncompleteCommissioner, methods=['POST'], collection_name='incomplete-commissioner')
manager.create_api(IncompleteProvider, methods=['POST'], collection_name='incomplete-provider')
manager.create_api(CompleteCommissioner, methods=['POST'], collection_name='complete-commissioner')
manager.create_api(CompleteProvider, methods=['POST'], collection_name='complete-provider')
manager.create_api(NewCommissioner, methods=['POST'], collection_name='new-commissioner')
manager.create_api(NewProvider, methods=['POST'], collection_name='new-provider')


@app.route("/rtt/commissioner/incomplete")
def hello():
    #treatment_function_code = request.args.get('treatment_function_code', '')

    query = IncompleteCommissioner.query.filter_by(treatment_function_code='IP999') \
        .order_by(IncompleteCommissioner.ccg_code) \
        .order_by(IncompleteCommissioner.year.asc()) \
        .order_by(IncompleteCommissioner.month.asc()) \
        .all()
    
    output = {}

    for row in query:
        if not row.year in output:
            output[row.year] = {}

        if not row.month in output[row.year]:
            output[row.year][row.month] = {}

        output[row.year][row.month][row.ccg_code] = {
            #"year": row.year,
            #"month": row.month,
            #"ccg_code": row.ccg_code,
            "total_incomplete": row.total_incomplete,
            "total_within_18": row.total_within_18,
            "total_with_dta": row.total_with_dta,
            "percent_within_18": round((row.total_within_18/row.total_incomplete)*100, 2),
            "percent_with_dta": round((row.total_with_dta/row.total_incomplete)*100, 2)
        }

    #sql = text('SELECT * from incomplete_commissioner WHERE')
    #result = db.engine.execute(sql)
    #names = []
    #for row in result:
    #    names.append(row[0])

    return jsonify(output)

db.create_all()

if __name__ == "__main__":
    app.run()