# 1. Conditional Statement
age = 20
if age >= 18:
    print("1. You are eligible to vote.")
else:
    print("1. You are not eligible to vote.")

# 2. For Loop - List
fruits = ["apple", "banana", "cherry"]
print("\n2. Fruits list:")
for fruit in fruits:
    print(f" - {fruit}")

# 3. While Loop - Print 1 to 5
print("\n3. Numbers from 1 to 5 using while loop:")
i = 1
while i <= 5:
    print(i)
    i += 1

# 4. List - Append and Remove
numbers = [1, 2, 3]
numbers.append(4)
numbers.remove(2)
print(f"\n4. Updated list: {numbers}")

# 5. Dictionary - Add and Access
person = {
    "name": "Ayushi",
    "age": 25
}
person["city"] = "Delhi"
print(f"\n5. Dictionary: {person}")
print(f"   Name: {person['name']}")

# 6. String Manipulation
message = " Hello, Python! "
print(f"\n6. Original message: '{message}'")
print(f"   Stripped: '{message.strip()}'")
print(f"   Lowercase: '{message.lower()}'")
print(f"   Uppercase: '{message.upper()}'")
print(f"   Replace: '{message.replace('Python', 'World')}'")

# 7. String Interpolation
name = "Ayushi"
language = "Python"
print(f"\n7. My name is {name} and I am learning {language}.")

# 8. Sum of even numbers in a list
nums = [1, 2, 3, 4, 5, 6]
even_sum = 0
for num in nums:
    if num % 2 == 0:
        even_sum += num
print(f"\n8. Sum of even numbers: {even_sum}")

# 9. Count characters in a string using dict
text = "banana"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(f"\n9. Character count in '{text}': {char_count}")

# 10. Check if a word is a palindrome
word = "madam"
is_palindrome = word == word[::-1]
print(f"\n10. Is '{word}' a palindrome? {is_palindrome}")
