while True:
    try:
        nums = list(map(int, input("Введите целые числа: ").split()))
        break
    except:
        print("Ошибка! Попробуйте снова.")

avg = sum(nums) / len(nums)

reversed_nums = []
for i in range(len(nums) - 1, -1, -1):
    reversed_nums.append(nums[i])
result = []
for num in reversed_nums:
    if num >= avg:
        result.append(num)

print("Среднее =", avg)
print("Развернутый:", *reversed_nums)
print("Результат:", *result)