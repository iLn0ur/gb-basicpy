
def tutor_kls_gen(sampl_tutors, sampl_klasses):
    klasses_gen = (i for i in sampl_klasses)
    for count, el in enumerate(sampl_tutors):
        try:
            kls = next(klasses_gen)
            yield el, kls
        except StopIteration:
            yield el, None


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Дарья', 'Всеволод'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

print(type(tutor_kls_gen(tutors, klasses)))
print(*tutor_kls_gen(tutors, klasses))
