def find_s_algorithm(examples):
    for example in examples:
        if example[-1] == 'Yes':
            hypothesis = example[:-1]
            break
    else:
        return None 

    for example in examples:
        if example[-1] == 'Yes':
            for i in range(len(hypothesis)):
                if hypothesis[i] != example[i]:
                    hypothesis[i] = '?'

    return hypothesis

training_data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

hypothesis = find_s_algorithm(training_data)

print("Most specific hypothesis found by FIND-S:")
print(hypothesis)