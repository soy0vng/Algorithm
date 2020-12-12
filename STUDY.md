# 알고리즘

## Collections

### Counter

> 컨테이너에 동일한 값의 자료가 몇 개인지를 파악하는데 사용하는 객체
>
> 결과 값(return)은 딕셔너리 형태로 출력(내림차순)

#### most_common()

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

