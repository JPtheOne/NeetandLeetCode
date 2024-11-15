nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

i = 0
print(f"Estado inicial: nums = {nums}, i = {i}\n")

for index, num in enumerate(nums):
    print(f"Iteración {index}: num = {num}, nums[i-1] = {nums[i-1] if i > 0 else 'N/A'}")
    
    if i < 1 or num > nums[i - 1]:
        print(f"  Condición cumplida: i < 1 ({i < 1}) o num > nums[i-1] ({num > nums[i-1] if i > 0 else 'N/A'})")
        nums[i] = num
        print(f"  Actualizando nums[{i}] = {num}")
        i += 1
        print(f"  Incrementando i → {i}")
    else:
        print(f"  Condición no cumplida: num no es mayor a nums[i-1]")

    print(f"  Estado actual: nums = {nums}\n")

print(f"Resultado final: i = {i}, nums[:i] = {nums[:i]}")
