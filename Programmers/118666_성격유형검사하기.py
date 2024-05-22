def solution(survey, choices):
    # 성격 유형 dictionary
    types = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    # choice에 따라 성격 유형 점수 바꿔주기
    for i in range(len(choices)):
        if choices[i] < 4:
            types[survey[i][0]] += 4 - choices[i]
        if choices[i] > 4:
            types[survey[i][1]] += choices[i] - 4
    type_key = list(types.keys())

    # 최종 결과 구하기
    answer = ''
    for i in range(0, len(type_key), 2):
        if types[type_key[i]] > types[type_key[i + 1]]:
            answer += type_key[i]
        elif types[type_key[i]] < types[type_key[i + 1]]:
            answer += type_key[i + 1]
        else:
            answer += min(type_key[i], type_key[i + 1])
    return answer