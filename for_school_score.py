school_scores = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
                {'school_class': '4b', 'scores': [2,5,5,3,3,5]},
                {'school_class': '4c', 'scores': [4,5,2,2,4]}]

school_total_score = 0

for class_score in school_scores:
    cls_sc = 0
    for num in class_score['scores']:
        cls_sc = cls_sc + num
    school_total_score = school_total_score + cls_sc
    mid_cls_sc = cls_sc / len(class_score['scores'])
    print('В классе {} средний балл равен {}'.format(class_score['school_class'], mid_cls_sc))

sc_mid_sc = school_total_score / len(school_scores)

print('Средний балл по школе равен {}'.format(sc_mid_sc))