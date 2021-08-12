import os
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory,
    g,
    flash,
)
import random

import make10_solver

app = Flask(__name__)

pre_num_str = "1234"
num_str = pre_num_str


# メインルーチン
@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":

        your_ans_id_str = request.form.get("your_answer")

        if your_ans_id_str:
            your_ans_id = int(your_ans_id_str)
            print("your_ans:", your_ans_id)

            your_ans_flag = None
            if your_ans_id == 0:
                your_ans_flag = True
                your_ans_str = "Yes"
            elif your_ans_id == 1:
                your_ans_flag = False
                your_ans_str = "No"

            global pre_num_str, num_str
            pre_num_str = num_str
            correct_flag, formula_str = make10_solver.make10(pre_num_str)
            if correct_flag:
                correct_ans_str = "Yes"
            else:
                correct_ans_str = "No"

            # result = "No Result"
            if correct_flag == your_ans_flag:
                result = "正解！"
            else:
                result = "不正解！"
            
            # 次の値をセット
            num_str = str(random.randint(0, 9999)).zfill(4) # zero-padding

            return render_template(
                "index.html",
                result=result,
                your_ans_s=your_ans_str,
                correct_ans_s=correct_ans_str,
                formula_s=formula_str,
                pre_num_s=pre_num_str,
                num_s=num_str,
            )
        else:
            error_message = "Please select Yes or No."
            return render_template("index.html", error_message=error_message)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1234)  # ポートの変更
