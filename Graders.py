def grade_classification(pred, true):
    return 1.0 if pred == true else 0.0

def grade_response(response, keywords):
    if not response:
        return 0.0

    score = 0
    for k in keywords:
        if k.lower() in response.lower():
            score += 1

    return min(score / len(keywords), 1.0)

def grade_resolution(class_score, response_score):
    return 0.3 * class_score + 0.7 * response_score
