def solution(today, terms, privacies):
    answer = []
    
    # today list
    today = list(map(int, today.split(".")))
    
    # term dictionary
    terms_dict = {}
    for term in terms:
        t = term.split()
        terms_dict[t[0]] = int(t[1])
    
    # 개인정보 for문
    idx = 1
    for privacy in privacies:
        collection_date = list(map(int, privacy.split()[0].split("."))) 
        term_type = privacy.split()[1] 
        
        term_period = terms_dict[term_type]
        
        # 최대 날짜 구하기
        max_date = collection_date[:]
        max_date[1] += term_period
        if max_date[1] > 12:
            max_date[0] += max_date[1]//12
            max_date[1] %= 12
            if max_date[1] == 0:
                max_date[1]=12
                max_date[0] -= 1
        print(max_date)
        # 최대 날짜보다 today가 크거나 같으면 파기
        if max_date <= today:
            answer.append(idx)
        idx += 1
    
    return answer
