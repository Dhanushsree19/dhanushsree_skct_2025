Given a number N reverse the number and print it.

Example 1: Input: N = 123 Output: 321 Explanation: The reverse of 123 is 321

Example 2: Input: N = 234 Output: 432 Explanation: The reverse of 234 is 432

Input Format

123

Constraints

N <= 1000

Output Format

321

Sample Input 0

123

Sample Output 0

321

Sample Input 1

2341

Sample Output 1

1432

Answer:
N = int(input())
temp = N
reverse = 0
while N > 0:
    remainder = N % 10
    reverse = (reverse * 10) + remainder
    N = N // 10

print(reverse)