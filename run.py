import json

from flask import Flask, abort, request, jsonify, Response

app = Flask(__name__)



import pickle
import numpy as np
import pandas as pd
import ast

@app.route('/test', methods=['GET'])
def ml(df):
    #df = dict(ast.literal_eval(df))
    df = pd.DataFrame([df])
    profs = ["Умение расставлять приоритеты", "Умение работать в команде", "Организационная осведомленность",
             "Эффективное решение проблем", "Самосознание", "Проактивность", "Способность оказывать влияние",
             "Эффективное принятие решений", "Способность к обучению", "Техническая смекалка",
             "опыт заключения торговых сделок",
             "навыки делового общения, ведения переговоров", "опыт работы на выставках, презентация продукции",
             "ведение и расширение клиентской базы", "составление и заключение договоров",
             "ведение первичной бухгалтерии",
             "контроль отгрузки и доставки товара", "уверенное владение ПК, знание 1С, Word, Excel",
             "Опыт управления IT-отделом (15 человек в подчинении)", "Управление бюджетом отдела",
             "Развитие IT в компании", "Автоматизация деятельности компании", "Руководство внутренними проектами",
             "Обеспечение информационной безопасности", "Подбор персонала и обучение", "анализ конкурентного окружения",
             "Знание PHP", "Практическое применение объектно-ориентированного программирования (ООП)",
             "Опыт работы с фреймворками для программистов (CMF)", "Знание шаблонных движков",
             "Опыт работы с базами данных (MySQL, PostgreSQL, Oracle), знание языка SQL",
             "Знание JavaScript, HTML+CSS", "Знание принципов построения и работы сайтов и серверов",
             "Знания технологий и языков в соответствующих областях: J2SE‚ J2EE, JPA, JAXB",
             "языки программирования: Java, С++, PHP‚ JavaScript, Phyton; XML‚ HTML; SQL, JPQL",
             "сертификаты: Oracle"]
    gends = ['FEMALE', 'MALE']
    educations = ['HIGH', 'SECONDARY', 'VOCATIONAL']
    for prof in profs:
        df[prof] = df['skills'].map(lambda s: prof in s)
    oldprofs = ['ИСПЫТАТЕЛЬ', 'НОТАРИУС', 'АНАЛИТИК', 'ЭКСКУРСОВОД', 'ТУРАГЕНТ', 'ПЕРЕВОДЧИК', 'СМЕТЧИК', 'ШТУРМАН',
                'ЮРИСКОНСУЛЬТ', 'ЛЕКТОР', 'ЖУРНАЛИСТ', 'СТАТИСТИК', 'БУХГАЛТЕР', 'ДИАГНОСТ', 'КОРРЕКТОР', 'КОПИРАЙТЕР']
    for oldprof in oldprofs:
        df[oldprof] = df['fromProfession'].map(lambda s: oldprof in s)
    for gend in gends:
        df[gend] = df['gender'].map(lambda s: gend in s)
    for educat in educations:
        df[educat] = df['education'].map(lambda s: educat in s)
    df = df.drop(['fromProfession'], axis=1)
    df = df.drop(['education'], axis=1)
    df = df.drop(['gender'], axis=1)
    print(df.columns)
    X = df.drop('skills', axis=1).values
    with open('model.pkl', 'rb') as f:
        model1 = pickle.load(f)
    model1.predict(X[0:1])
    pred_prob = model1.predict_proba(X[0:1])
    pred_prob=pred_prob*100
    profs1 = np.array(profs)
    pred_prob1 = pd.DataFrame(pred_prob, columns=model1.classes_)
    pred_prob2 = pred_prob1.T.to_dict()
    pred_prob2=json.dumps(pred_prob2, ensure_ascii=False)
    my_str = pred_prob2.replace('{"0"', '{"name"')
    return  Response(my_str, mimetype='application/json')


@app.route('/foo', methods=['POST'])
def foo():
    if not request.json:
        abort(400)
    return ml(request.json)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

