import sqlite3
connect = sqlite3.connect('DataBase.db')
curs = connect.cursor()

create_participants = 'CREATE TABLE IF NOT EXISTS Participants(' \
                      'Participant_Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' \
                      'Participant_name TEXT,' \
                      'Degree TEXT,' \
                      'Field TEXT,' \
                      'Workplace TEXT,' \
                      'Department TEXT,' \
                      'Position TEXT,' \
                      'Country TEXT,' \
                      'City TEXT,' \
                      'Adress TEXT,' \
                      'Phone TEXT,' \
                      'Email TEXT' \
                      ');'
curs.execute(create_participants)
connect.commit()

create_conference = 'CREATE TABLE IF NOT EXISTS Conference (' \
                    'Conference_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' \
                    'Conference_name TEXT,' \
                    'Date TEXT,' \
                    'Location TEXT,' \
                    'Organizers TEXT,' \
                    'Sponsors TEXT,' \
                    'Duration_days INTEGER,' \
                    'Particip_num INTEGER,' \
                    'Speakers_num INTEGER' \
                    ');'
curs.execute(create_conference)
connect.commit()

create_info = 'CREATE TABLE IF NOT EXISTS Info(' \
              'Report_Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' \
              'Participant_name TEXT,' \
              'Participant_Id INTEGER,'\
              'Conference_name  TEXT,' \
              'Invitation_date TEXT,' \
              'Application_date TEXT,' \
              'Topic TEXT,' \
              'Thesis_admission INTEGER,' \
              'Arrival_date TEXT,' \
              'Hotel_need INTEGER,' \
              'Departure_date TEXT,' \
              'FOREIGN KEY (Participant_Id) REFERENCES Participants(Participant_Id),' \
              'FOREIGN KEY (Conference_name) REFERENCES Conference(Conference_name)' \
              ');'
curs.execute(create_info)
connect.commit()

# participants_list = [
#     ('Petrov Ivan', 'candidate of science', 'social science', 'Russian State Social University', 'social communication department', 'docent', 'Russia', 'Moscow', 'Tverskaya st.13', '+79032973982', 'Petrov_i9@gmail.com'),
#     ('Malashenko Elena', 'doctor of science', 'natural science', 'BSUIR', 'Information security department', 'head of department', 'Belarus', 'Minsk','Partizanskiy av.48', '+375292774548', 'Elen_mal@mail.ru'),
#     ('Sedun Maxim', 'doctor of Philosophy', 'human science', 'International Humanitarian and Economic Institute', 'Humanitarian disciplines department', 'professor', 'Belarus','Minsk','Prititskogo av.25', '+375333879823', 'sedun_88@yandex.by'),
#     ('Sidorov Pavel', 'doctor of science', 'biological science', 'Moscow State University Lomonosov', 'Pharmacology department', 'head of department', 'Russia', 'Moscow','Avtozavodskaya st.56' ,'+79033855412', 'Sidor_pav32@gmail.com'),
#     ('Kupreeva Anna', 'candidate of science', 'natural science', 'BSEU', 'World economy department', 'docent', 'Belarus', 'Minsk','M.Bogdanovicha st. 53' ,'+375448730923', 'Kupr_anna84@tut.by'),
#     ('Shapovalova Viktoria', 'doctor of science', 'natural science', 'Vitebsk State University Masherov', 'Engineering Physics department', 'docent', 'Belarus', 'Vitebsk','Chkalova st.51', '+375259838120', 'Vik_sh80@gmail.com')
# ]
#
# insert_participants = 'INSERT INTO Participants(Participant_name, Degree, Field, Workplace, Department, Position, Country, City, Adress, Phone, Email) VALUES(?,?,?,?,?,?,?,?,?,?,?);'
# curs.executemany(insert_participants, participants_list)
# connect.commit()
#
# conference_list = [
#     ('Economic-mathematical methods and models', '24.12.2022', 'Minsk', 'Business development company', 'MBA Academy', 2, 105, 15),
#     ('Robotic technology', '28.01.2023', 'Moscow', '21 Technologies', 'VTB', 3, 112, 22),
#     ('Cybersecurity', '23.02.2023', 'Minsk', 'IT Group', 'Fort Capital', 2, 100, 14),
#     ('Children\' and youth\'s socialization', '19.12.2022', 'Saint-Petersburg', 'Event Studio', 'Direct media', 3, 150, 25),
#     ('Humanitarian problems of information society', '21.12.2022', 'Minsk', 'All Event', 'Global Finance', 3, 146, 23),
#     ('Pharmacology', '15.01.2023', 'Moscow', 'Go Med', 'Pharma Centre', 4, 164, 28)
# ]
# insert_conference = 'INSERT INTO Conference(Conference_name,Date, Location, Organizers, Sponsors, Duration_days, Particip_num, Speakers_num) VALUES(?,?,?,?,?,?,?,?);'
# curs.executemany(insert_conference, conference_list)
# connect.commit()
#
#
# info_list = [
#     ('Shapovalova Viktoria', 6, 'Robotic technology', '15.12.2022', '20.12.2022', '10 main robotic technologies of the year', 0, '27.01.2023', 1, '30.01.2023'),
#     ('Sidorov Pavel', 4, 'Pharmacology', '02.12.2022', '10.12.2022', 'Environmental pharmacology', 1, '14.01.2023', 0, '18.01.2023'),
#     ('Petrov Ivan', 1, 'Children\' and youth\'s socialization', '05.11.2022', '11.11.2022', 'Impact of Media in Socialization', 1, '18.12.2022', 1, '21.12.2022'),
#     ('Kupreeva Anna', 5, 'Economic-mathematical methods and models', '20.11.2022', '25.11.2022', 'Mathematical Methods of Budget Modeling', 1, '23.12.2022', 0, '25.12.2022'),
#     ('Sedun Maxim', 3, 'Humanitarian problems of information society', '15.11.2022', '20.11.2022', 'Problems of humanitarian education in the information society', 1, '20.12.2022', 0, '23.12.2022'),
#     ('Malashenko Elena', 2, 'Cybersecurity', '15.01.2023', '20.01.2023', 'Public Wi-Fi', 0, '22.02.2023', 0, '24.01.2023')
#     ]
# insert_info = 'INSERT INTO Info(Participant_name,Participant_Id, Conference_name, Invitation_date, Application_date, Topic, Thesis_admission, Arrival_date, Hotel_need, Departure_date) VALUES(?,?,?,?,?,?,?,?,?,?);'
# curs.executemany(insert_info, info_list)
# connect.commit()


# select_all_partic = 'SELECT * FROM PARTICIPANTS;'
# curs.execute(select_all_partic)
# req1 = curs.fetchall()
# for tup in req1:
#     print(tup)

# select_conf = '''SELECT * FROM CONFERENCE WHERE DURATION_DAYS > 2 AND LOCATION = 'Moscow';'''
# curs.execute(select_conf)
# req2 = curs.fetchall()
# for tup in req2:
#     print(tup)

# delete_from_partip = "DELETE FROM Participants WHERE city = 'Minsk';"
# curs.execute(delete_from_partip)
# connect.commit()
#
# upd_partip = '''UPDATE Participants SET adress ='Lenina st.46' WHERE participant_name = 'Petrov Ivan' ;'''
# curs.execute(upd_partip)
# connect.commit()
#
# upd_partip2 = '''UPDATE Participants SET Email='vika_79@mail.ru' WHERE participant_name = 'Shapovalova Viktoria' ;'''
# curs.execute(upd_partip2)
# connect.commit()
#
# upd_partip3 = '''UPDATE Participants SET Phone='+7901806402' WHERE participant_name = 'Sidorov Pavel' ;'''
# curs.execute(upd_partip3)
# connect.commit()

# delete_from_info = "DELETE FROM Info WHERE Hotel_need = 1 ;"
# curs.execute(delete_from_info)
# connect.commit()

# upd_info1 = '''UPDATE Info SET Departure_date='28.12.2023' WHERE participant_name = 'Sedun Maxim' ;'''
# curs.execute(upd_info1)
# connect.commit()

# upd_info2 = '''UPDATE Info SET Topic='Cryptography' WHERE participant_name = 'Malashenko Elena' ;'''
# curs.execute(upd_info2)
# connect.commit()

# delete_from_conference = "DELETE FROM Conference WHERE Particip_num > 115 ;"
# curs.execute(delete_from_conference)
# connect.commit()

upd_conf = '''UPDATE Conference SET Organizers ='Startup_finance' WHERE Organizers ='21 Technologies' ;'''
curs.execute(upd_conf)
connect.commit()

curs.close()
connect.close()
