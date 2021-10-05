numbers =[12,2,30]
print(len(numbers))#3

print(max(numbers))#30

numbers.sort()
print(numbers) #[2, 12, 30]

numbers.reverse()
print(numbers) #[30, 12, 2]

numbers.append(20)
print(numbers)#[30, 12, 2, 20]

numbers.insert(1,200)
print(numbers) #[30, 200, 12, 2, 20]

numbers.remove(2)
print(numbers) #[30, 200, 12, 20]

numbers.pop()
print(numbers) #[30, 200, 12]