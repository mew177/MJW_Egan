"""
            Question:
            1. How should I handle n = 1? is it different?
            2.

            Idea1(naive algo):
            1. go from, i =  1 to n
            2. if i % 3 == 0, List[i] = Fizz
            3. if i % 5 == 0, List[i] = Buzz
            4. if i %15 == 0, List[i] = FizzBuzz

            Time Complexity:
            O(n)

        """

n = 15
result = []

for i in range(n):
    if (i + 1) % 15 == 0:
        result.append("FizzBuzz")
    elif (i + 1) % 5 == 0:
        result.append("Buzz")
    elif (i + 1) % 3 == 0:
        result.append("Fizz")
    else:
        result.append(str(i + 1))
print(result)