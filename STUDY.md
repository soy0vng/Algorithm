# 알고리즘

## Collections

### Counter

> 컨테이너에 동일한 값의 자료가 몇 개인지를 파악하는데 사용하는 객체
>
> 결과 값(return)은 딕셔너리 형태로 출력(내림차순)

#### `most_common()`

> 높은 빈도(frequency) 순으로 정렬된 배열 리턴

```python
# BOJ/2108. 통계학.py
from collections import Counter

numbers = [-1, -2, -3, -1, -2]
numbers_dict = Counter(numbers)
nums = numbers_dict.most_common()

print(numbers_dict) # Counter({-1: 2, -2: 2, -3: 1})
print(nums)	# [(-1, 2), (-2, 2), (-3, 1)]
```



## 최대 재귀 깊이 설정

```python
import sys
sys.setrecursionlimit(10000)
```



## 시간 초과

**1. sys.stdin.readline()**

```python
import sys

# input() 대신 사용
sys.stdin.readline() 
```

입출력 속도 비교: sys.stdin.readline() > raw_input() > input()

**2. Pypy로 제출**



## isalpha, isdigit

`isalpha()`

> 문자열이 문자인지 아닌지를 True, False로 리턴 (문자열에 숫자 또는 공백이 있으면 False)

`isdigit()`

> 문자열이 숫자인지 아닌지를 True, False로 리턴

