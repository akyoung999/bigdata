def get_mbti_type():
    extroversion_score = 0
    sensing_score = 0
    thinking_score = 0
    judging_score = 0

    # '선호하는 세계'에 대한 질문
    answer = input("질문1. 새로운 장소에서 모르는 사람에게 먼저 인사를 건네는 편인가요? (예/아니오): ")
    if answer.lower() == "예":
        extroversion_score += 1

    answer = input("질문2. 쉬는 날에는 집에 있어야 회복 되나요? (예/아니오): ")
    if answer.lower() == "아니오":
        extroversion_score += 1

    answer = input("질문3. 기분이 안 좋을 때 사람을 만나면 기분이 나아지나요? (예/아니오): ")
    if answer.lower() == "예":
        extroversion_score += 1


    # '정보 수집 방식'에 대한 질문
    answer = input("질문4. 노래를 들을 때 가사보다 멜로디를 더 중점적으로 듣나요? (예/아니오): ")
    if answer.lower() == "예":
        sensing_score += 1

    answer = input("질문 5. 시나 소설, 혹은 가정에 대해 말하는 것을 좋아하나요? (예/아니오): ")
    if answer.lower() == "아니오":
        sensing_score += 1

    answer = input("질문 6. 처음 해보는 요리를 할 때 정량을 철저히 지키는 편인가요? (예/아니오): ")
    if answer.lower() == "예":
        sensing_score += 1


    # '생활 방식'에 대한 질문
    answer = input("질문 7. 결과보다는 과정을 더 중요하다고 생각하나요? (예/아니오): ")
    if answer.lower() == "아니오":
        thinking_score += 1

    answer = input("질문 8. 다른 사람이 울고 있다면 그 마음에 공감해주고 싶나요?? (예/아니오): ")
    if answer.lower() == "아니오":
        thinking_score += 1

    answer = input("질문 9. 친구에게 현실적으로 조언을 하는 편인가요? (예/아니오): ")
    if answer.lower() == "예":
        thinking_score += 1


    # '결정 방식'에 대한 질문
    answer = input("질문 10. 계획을 세세하게 세운 이후 진행하는 것을 선호하는 편인가요? (예/아니오): ")
    if answer.lower() == "예":
        judging_score += 1

    answer = input("질문 11. 시험 며칠 전부터 벼락치기를 시작하나요? (예/아니오): ")
    if answer.lower() == "아니오":
        judging_score += 1

    answer = input("질문 12. 자신의 일이 계획대로 진행되지 않아도 유연하게 방법을 찾는 편인가요? (예/아니오): ")
    if answer.lower() == "아니오":
        judging_score += 1


    mbti_type = ""

    # E/I 결정
    if extroversion_score >= 2:
        mbti_type += "E"
    else:
        mbti_type += "I"

    # S/N 결정
    if sensing_score >= 2:
        mbti_type += "S"
    else:
        mbti_type += "N"

    # T/F 결정
    if thinking_score >= 2:
        mbti_type += "T"
    else:
        mbti_type += "F"

    # J/P 결정
    if judging_score >= 2:
        mbti_type += "J"
    else:
        mbti_type += "P"

    return mbti_type

# MBTI 유형 획득
my_mbti = get_mbti_type()
print("당신의 MBTI 유형은:", my_mbti)