from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

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
