
"""
入力: arr = [1,2,3]
出力: [2,4,6]
説明: 1*2=2, 2*2=4, 3*2=6 なので [2,4,6] が答えとなる。
"""

def solution(arr):
    results = []
    for num in arr:
        results.append(num*2)

    return results


print(solution([1,2,3]))

