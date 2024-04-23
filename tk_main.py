from flask import Flask, redirect, url_for, request, Response, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Don@sonu19'
app.config['MYSQL_DB'] = 'dcc_finale'

mysql = MySQL(app)

@app.route('/', methods = ["POST", "GET"])
def main_page():
    return render_template("index.html")


@app.route('/pp', methods = ["POST", "GET"])
def pp():
    if request.method=='POST' :
        option = request.form['type_g']
        if option == 'Political Parties':
            return render_template('pp.html')
        elif option == 'Individuals':
            return render_template('indi.html', indi_data='Beeeeeeee')
        else:
            return render_template('result_invalid_option.html')


#Defining funcs for political parties
@app.route('/pp_eb_search', methods = ["POST", "GET"])
def pp_search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `eb_poli` WHERE `Name of the Political Party` = %s", (request.form["pp_box"],))
        data = cursor.fetchall()
        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", a_5_data = [["Not Found !!!"]]) 
    return render_template("pp.html", pp_search_data = data)



@app.route('/pp_eb_doe_search', methods = ["POST", "GET"])
def pp_doe_search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `eb_poli` WHERE `Date of Encashment` = %s", (request.form["pp_doe_box"],))
        data = cursor.fetchall()
        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", pp_doe_search_data = [["Not Found !!!"]]) 
    return render_template("pp.html", pp_doe_search_data = data)

@app.route('/pp_eb_an_search', methods = ["POST", "GET"])
def pp_an_search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `eb_poli` WHERE `Account no. of Political Party` = %s", (request.form["pp_an_box"],))
        data = cursor.fetchall()
        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", pp_an_search_data = [["Not Found !!!"]]) 
    return render_template("pp.html", pp_an_search_data = data)

@app.route('/pp_eb_p_search', methods = ["POST", "GET"])
def pp_p_search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `eb_poli` WHERE `Prefix` = %s", (request.form["pp_p_box"],))
        data = cursor.fetchall()
        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", pp_p_search_data = [["Not Found !!!"]]) 
    return render_template("pp.html", pp_p_search_data = data)

@app.route('/pp_eb_bn_search', methods = ["POST", "GET"])
def pp_bn_search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `eb_poli` WHERE `Bond Number` = %s", (request.form["pp_bn_box"],))
        data = cursor.fetchall()
        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", pp_bn_search_data = [["Not Found !!!"]]) 
    return render_template("pp.html", pp_bn_search_data = data)


@app.route('/pp_eb_pb_search', methods = ["POST", "GET"])
def pp_pb_search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `eb_poli` WHERE `Pay Branch Code` = %s", (request.form["pp_pb_box"],))
        data = cursor.fetchall()
        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", pp_pb_search_data = [["Not Found !!!"]]) 
    return render_template("pp.html", pp_pb_search_data = data)

@app.route('/pp_eb_pt_search', methods = ["POST", "GET"])
def pp_pt_search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `eb_poli` WHERE `Pay Teller` = %s", (request.form["pp_pt_box"],))
        data = cursor.fetchall()
        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", pp_pt_search_data = [["Not Found !!!"]]) 
    return render_template("pp.html", pp_pt_search_data = data)


#Defining funcs for Individuals
@app.route('/indi_eb_rn_search', methods = ["POST", "GET"])
def indi_rn_search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `eb_indi` WHERE `Reference No (URN)` = %s", (request.form["indi_rn_box"],))
        data = cursor.fetchall()
        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", indi_rn_search_data = [["Not Found !!!"]]) 
    return render_template("indi.html", indi_rn_search_data = data)

@app.route('/indi_eb_jd_search', methods = ["POST", "GET"])
def indi_jd_search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `eb_indi` WHERE `Journal Date` = %s", (request.form["indi_jd_box"],))
        data = cursor.fetchall()
        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", indi_jd_search_data = [["Not Found !!!"]]) 
    return render_template("indi.html", indi_jd_search_data = data)

@app.route('/indi_eb_dop_search', methods = ["POST", "GET"])
def indi_dop_search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `eb_indi` WHERE `Date of Purchase` = %s", (request.form["indi_dop_box"],))
        data = cursor.fetchall()
        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", indi_dop_search_data = [["Not Found !!!"]]) 
    return render_template("indi.html", indi_dop_search_data = data)

@app.route('/indi_eb_doe_search', methods = ["POST", "GET"])
def indi_doe_search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `eb_indi` WHERE `Date of Expiry` = %s", (request.form["indi_doe_box"],))
        data = cursor.fetchall()
        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", indi_doe_search_data = [["Not Found !!!"]]) 
    return render_template("indi.html", indi_doe_search_data = data)

@app.route('/indi_eb_nop_search', methods = ["POST", "GET"])
def indi_nop_search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `eb_indi` WHERE `Name of the Purchaser` = %s", (request.form["indi_nop_box"],))
        data = cursor.fetchall()
        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", indi_nop_search_data = [["Not Found !!!"]]) 
    return render_template("indi.html", indi_nop_search_data = data)

@app.route('/indi_eb_p_search', methods = ["POST", "GET"])
def indi_p_search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `eb_indi` WHERE `Prefix` = %s", (request.form["indi_p_box"],))
        data = cursor.fetchall()
        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", indi_p_search_data = [["Not Found !!!"]]) 
    return render_template("indi.html", indi_p_search_data = data)

@app.route('/indi_eb_bn_search', methods = ["POST", "GET"])
def indi_bn_search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `eb_indi` WHERE `Bond Number` = %s", (request.form["indi_bn_box"],))
        data = cursor.fetchall()
        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", indi_bn_search_data = [["Not Found !!!"]]) 
    return render_template("indi.html", indi_bn_search_data = data)


@app.route('/indi_eb_dn_search', methods = ["POST", "GET"])
def indi_dn_search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `eb_indi` WHERE `Denominations` = %s", (request.form["indi_dn_box"],))
        data = cursor.fetchall()
        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", indi_bn_search_data = [["Not Found !!!"]]) 
    return render_template("indi.html", indi_bn_search_data = data)

@app.route('/indi_eb_ibc_search', methods = ["POST", "GET"])
def indi_ibc_search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `eb_indi` WHERE `Issue Branch Code` = %s", (request.form["indi_ibc_box"],))
        data = cursor.fetchall()
        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", indi_ibc_search_data = [["Not Found !!!"]]) 
    return render_template("indi.html", indi_ibc_search_data = data)

@app.route('/indi_eb_it_search', methods = ["POST", "GET"])
def indi_it_search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `eb_indi` WHERE `Issue Teller` = %s", (request.form["indi_it_box"],))
        data = cursor.fetchall()
        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", indi_it_search_data = [["Not Found !!!"]]) 
    return render_template("indi.html", indi_it_search_data = data)

@app.route('/indi_eb_s_search', methods = ["POST", "GET"])
def indi_s_search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `eb_indi` WHERE `Status` = %s", (request.form["indi_s_box"],))
        data = cursor.fetchall()
        cursor.close()

    if len(data) == 0:
        return render_template("index.html", indi_s_search_data = [["Not Found !!!"]]) 
    return render_template("indi.html", indi_s_search_data = data)

#QUESTION-2 REGARDING BOND INFO

#REDIRECTING TO POLITICAL PARTY OR INDI/COMPANIES
@app.route('/bond', methods = ["POST", "GET"])
def bond_redirect():
    if request.method == "POST":
        option=request.form['bond_info']
        if option=='Political Parties':
            return render_template("pp_bond_info.html", welcome="Welcome to this page where you can find info for any Political Party")
        elif option=='Individuals and Companies':
            return render_template("indi_bond_info.html",welcome="Welcome to this page where you can find info for any Political Party")


@app.route('/pp_bond_search', methods = ["POST", "GET"])
def pp_bond_search():
    if request.method == "POST":
        party_name = request.form['poli_bs']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM eb_poli WHERE `Name of the Political Party` = %s", (party_name,))
        bond_num= (cursor.fetchone())[0]

#To do this I had to change the Original Database a bit. Removing the commas, and making it an int.
        cursor.execute("select sum(Denominations) from eb_poli where `Name of the Political Party`= %s", (party_name,))
        bond_value = (cursor.fetchone())[0]
        cursor.close()
        return render_template("pp_bond_info.html", bond_num=bond_num, party_name=party_name, bond_value=bond_value  )

@app.route('/indi_bond_search', methods = ["POST", "GET"])
def indi_bond_search():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM `eb_indi` WHERE `Status` = %s", (request.form["indi_s_box"],))

        data = cursor.fetchall()
        cursor.close()
    
    if len(data) == 0:
        return render_template("indi_bond_info.html", indi_s_search_data = [["Not Found !!!"]]) 
    return render_template("indi.html", indi_bond_data = data)


if __name__ == '__main__':
   app.run(host="0.0.0.0", port="80", debug = True) 
