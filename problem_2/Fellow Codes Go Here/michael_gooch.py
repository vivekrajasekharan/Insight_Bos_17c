"""
Given a string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba"
Output: False

Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

def is_substring_helper (data):
    #YOUR CODE GOES HERE
    length = len(data)
    repeat_length = int(length / 2)
    while repeat_length >= 1:
        if length % repeat_length == 0:
            # divisible by size, check for substr composition
            data_slice = data[0:repeat_length]
            combined = "".join([data_slice for x in range(int(length / repeat_length))])
            if combined == data:
                return True
        repeat_length -= 1


    return False

#DON NOT CHANGE THIS FUNCTION
def is_substring (string_input):
    return is_substring_helper(string_input)


#test case
def main():
    TEST_CASE1 = "abab"
    TEST_CASE2 = "aba"
    TEST_CASE3 = "abcabcabcabc"

    print ("Testing your code with TEST_CASE1, the expected output is True, your output is {}".format(is_substring(TEST_CASE1)))
    print ("Testing your code with TEST_CASE2, the expected output is False, your output is {}".format(is_substring(TEST_CASE2)))
    print ("Testing your code with TEST_CASE3, the expected output is True, your output is {}".format(is_substring(TEST_CASE3)))

if __name__ == "__main__":
    main()