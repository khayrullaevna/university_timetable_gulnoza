from flask import Flask, render_template, request
import pg8000

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/timetable", methods=["GET"])
def timetable():
    level = request.args.get('level')
    if not level:
        return render_template("timetable_gulnoza.html", level=None, data=[], message="Level not provided!")

    try:
        conn = pg8000.connect(
            user="postgres",
            password="gaybullayeva03",
            host="gulnoza-db.c1w00oaegslj.us-east-1.rds.amazonaws.com",
            port=5432,
            database="postgres"
        )
        cur = conn.cursor()
        query = "SELECT course_name, day, time FROM timetable WHERE level = %s;"
        cur.execute(query, (level,))
        rows = cur.fetchall()
        if rows:
            return render_template("timetable_gulnoza.html", level=level, data=rows, message="")
        else:
            return render_template("timetable_gulnoza.html", level=level, data=[], message="No data found for this level.")
    except Exception as e:
        return render_template("timetable_gulnoza.html", level=level, data=[], message=f"An error occurred: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
