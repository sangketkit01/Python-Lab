all_subject = []
all_score = []
for i in range(5) :
     subject = input("Enter subject : ")
     score = float(input("Enter score : "))
     all_subject.append(subject)
     all_score.append(score)

maxScore = max(all_score)
maxSubject = all_subject[all_score.index(maxScore)]

minScore = min(all_score)
minSubject = all_subject[all_score.index(minScore)]

print("Max score is : {} | Subject : {}".format(maxScore,maxSubject))
print("Min score is {} | Subject : {}".format(minScore,minSubject))
