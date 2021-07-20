import sqlite3
from Internet_Module import check_inernet_connection


def create_connection():
    connection=sqlite3.connect('memory.db')
    return connection

def get_questions_and_answers():
    con=create_connection()
    cur=con.cursor()
    cur.execute('SELECT * FROM QuestionsAndAnswers')
    return cur.fetchall()

def insert_question_and_answer(ques,ans):
    con=create_connection()
    cur=con.cursor()
    query="INSERT INTO QuestionsAndANswers VALUES('"+ques+"','"+ans+"')"
    cur.execute(query)
    con.commit()


def get_answers_from_memory(question):
    rows=get_questions_and_answers()
    answer=''
    for row in rows:
        if row[0].lower() in question.lower():
            answer=row[1]
            break
    return answer

def update_last_seen_date(last_seen_date):
    con=create_connection()
    cur=con.cursor()
    query="update memory set value='"+str(last_seen_date)+"' where name='last_seen'"
    cur.execute(query)
    con.commit()

def get_last_seen():
    con=create_connection()
    cur=con.cursor()
    query='select value from memory where name ="last_seen"'
    cur.execute(query)
    return str(cur.fetchall()[0][0])


def get_assistant_name():
    con=create_connection()
    cur=con.cursor()
    query='select value from memory where name ="assistant_name"'
    cur.execute(query)
    return cur.fetchall()[0][0]


def new_assistant_name(new_name):
    con=create_connection()
    cur=con.cursor()
    query="update memory set value='"+new_name+"' where name='assistant_name'"
    cur.execute(query)
    con.commit()

def turn_on_speech():
    if check_inernet_connection():
        con=create_connection()
        cur=con.cursor()
        query="update memory set value='on' where name='speech'"
        cur.execute(query)
        con.commit()
        return('Okay! I will speak')
    else:
        return ('Hey please turn internet connection')

def turn_off_speech():
    con=create_connection()
    cur=con.cursor()
    query="update memory set value='off' where name='speech'"
    cur.execute(query)
    con.commit()
    return("Okay! I won't speak")


def speak_is_on():
    con=create_connection()
    cur=con.cursor()
    query='select value from memory where name ="speech"'
    cur.execute(query)
    ans= cur.fetchall()[0][0]
    if ans=='on' and check_inernet_connection():
        return True
    else:
        return False
