# def meanderingArray(unsorted):
#     unsorted.sort()
#     meandering = []
#     end_index = len(unsorted) - 1
#     if len(unsorted) % 2 != 0:
#         for i in range(int(len(unsorted)/2)+1):
#             meandering.append(unsorted[end_index - i])
#             meandering.append(unsorted[i])
#         meandering.pop()
#     if len(unsorted) % 2 == 0:
#         for i in range(int(len(unsorted)/2)):
#             meandering.append(unsorted[end_index - i])
#             meandering.append(unsorted[i])
#     return meandering
#
#
# numbers = [1,2,3,4,5,6]
# k = 2
# def countPairs(numbers, k):
#     unique = set(numbers)
#     count = 0
#     for number in unique:
#         if number + k in unique:
#             count += 1
#     return print(count)
#
# countPairs(numbers,k)
interest_rate = .03
loan_term = 30
loan_amount = 80000
interest_monthly = float(interest_rate / 12)
n = float(loan_term * 12)

M = round(loan_amount * (interest_monthly * (1 + interest_monthly) ** n) / ((1 + interest_monthly) ** n - 1), 2)
print(M)