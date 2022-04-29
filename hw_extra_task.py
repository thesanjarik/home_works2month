class Solution:

    def maximum_wealth(self, account: list) -> int:
        self.account = account


account = [[1, 2, 3], [3, 2, 1]]
print("Input  : ", account)

#Empty list
j = []

count = 0

# traverse the array


for i in account:
	if i not in j:
		count = count + 1
		account.append(i)

# printing the output
print("Объяснение: оба клиента считатся богатыми ведь их богатсво равны) : ", j)
print(count)