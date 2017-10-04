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

def is_substring_helper(data):
	# YOUR CODE GOES HERE
    n = len(data)//2   # check for substrings of length 1 to n, where n is len(data)/2
    while n > 0:
        print 'Checking ' + data + ' for matching substrings of length ' + str(n)
        if len(data) % n == 0:  # if substring of length n can compose data without leftover letters
            num_substrings = len(data)/n  # if data is len 9 and n is 3, check for 3 substrings
            # ideally would only check for prime numbers of num_substrings
            substring_start_indices = [i*n for i in range(1, num_substrings)]
            x = 0
            curr_substring_loc = substring_start_indices[x]
            first_substring_loc = 0
            while data[curr_substring_loc] == data[first_substring_loc]:  # while later substring matches first series
                curr_substring_loc += 1
                first_substring_loc += 1
                if curr_substring_loc == len(data):  # if we reach the end of the last possible substring
                    print 'Found ' + str(x+2) + ' matching substrings of length ' + str(n)
                    return True
                elif curr_substring_loc - substring_start_indices[x] == n:
                    # if we reach the end of the current possible substring of length n
                    x += 1
                    curr_substring_loc = substring_start_indices[x]
                    first_substring_loc = 0  # start checking next possible substring against the first series
                else:
                    continue  # check match at new locations with while loop
            # when a substring of length n stops matching first series, increment n
            print 'Did not find all matches for substring of length ' + str(n)
            n -= 1
            continue
        else:
            print 'String not divisible into substrings of length ' +str(n)
            n -= 1
            continue
    else:
        return False


# DO NOT CHANGE THIS FUNCTION
def is_substring (string_input):
	return is_substring_helper(string_input)


# test case
def main():
    TEST_CASE1 = "abab"
    TEST_CASE2 = "aba"
    TEST_CASE3 = "abcabcabcabc"

    # needed to add more test cases to check instances of >2 substring occurrences
    TEST_CASE4 = "abcabcabc"
    TEST_CASE5 = "abadabad"
    TEST_CASE6 = "aaaaa"
    TEST_CASE7 = "aaaab"

    print ("Testing your code with TEST_CASE1, the expected output is True, your output is {}".format(is_substring(TEST_CASE1)))
    print ("Testing your code with TEST_CASE2, the expected output is False, your output is {}".format(is_substring(TEST_CASE2)))
    print ("Testing your code with TEST_CASE3, the expected output is True, your output is {}".format(is_substring(TEST_CASE3)))

    print ("Testing your code with TEST_CASE4, the expected output is True, your output is {}".format(is_substring(TEST_CASE4)))
    print ("Testing your code with TEST_CASE5, the expected output is True, your output is {}".format(is_substring(TEST_CASE5)))
    print ("Testing your code with TEST_CASE6, the expected output is True, your output is {}".format(is_substring(TEST_CASE6)))
    print ("Testing your code with TEST_CASE7, the expected output is False, your output is {}".format(is_substring(TEST_CASE7)))


if __name__ == "__main__":
    main()