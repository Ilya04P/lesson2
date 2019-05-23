school_scores = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
                {'school_class': '4b', 'scores': [2,5,5,3,3,5]},
                {'school_class': '4c', 'scores': [4,5,2,2,4]}]

school_total_score_class = 0
school_total_score_students = 0
students_in_school = 0

for class_score in school_scores:
    cls_sc = 0
    for num in class_score['scores']:
        cls_sc = cls_sc + num
    mid_cls_sc = cls_sc / len(class_score['scores'])
    school_total_score_class = school_total_score_class + mid_cls_sc
    school_total_score_students = school_total_score_students + cls_sc
    students_in_school = students_in_school + len(class_score['scores'])
    print('В классе {} средний балл равен {}'.format(class_score['school_class'], mid_cls_sc))

sc_mid_sc = school_total_score_class / len(school_scores)
sc_mid_sc_st = school_total_score_students / students_in_school

print('Средний балл по школе равен (классы) {}'.format(sc_mid_sc))
print('Средний балл по школе равен (ученики) {}'.format(sc_mid_sc_st))