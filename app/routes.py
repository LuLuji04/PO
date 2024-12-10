from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index0():
    # 这里可以调用数据分析逻辑
    analysis_result = "这是分析结果"
    return render_template('index0.html', result=analysis_result)

@main.route('/detail0')
def detail0():
    # 这里可以调用数据分析逻辑
    analysis_result = "这是分析结果"
    return render_template('detail0.html', result=analysis_result)

@main.route('/index1')
def index1():
    # 这里可以调用数据分析逻辑
    analysis_result = "这是分析结果"
    return render_template('index1.html', result=analysis_result)

@main.route('/detail1')
def detail1():
    # 这里可以调用数据分析逻辑
    analysis_result = "这是分析结果"
    return render_template('detail1.html', result=analysis_result)

@main.route('/index2')
def index2():
    # 这里可以调用数据分析逻辑
    analysis_result = "这是分析结果"
    return render_template('index2.html', result=analysis_result)

@main.route('/detail2')
def detail2():
    # 这里可以调用数据分析逻辑
    analysis_result = "这是分析结果"
    return render_template('detail2.html', result=analysis_result)

@main.route('/index3')
def index3():
    # 这里可以调用数据分析逻辑
    analysis_result = "这是分析结果"
    return render_template('index3.html', result=analysis_result)

@main.route('/index4')
def detail3():
    # 这里可以调用数据分析逻辑
    analysis_result = "这是分析结果"
    return render_template('index4.html', result=analysis_result)