# Palindrome Checking

## Evelyn Griffith

## Program Output

### Use four fenced code blocks to provide output from four different runs of `palindromechecker` with different inputs

- Recursive:
- Input `word` is a palindrome

```
✨ Awesome. using the recursive for palindrome checking!

🔖 Going to check to see if the word civic is a palindrome!

😆 Is this word a palindrome? Yes, it is!
```

- Input `word` is not a palindrome

```
✨ Awesome. using the recursive for palindrome checking!

🔖 Going to check to see if the word taylor is a palindrome!

😆 Is this word a palindrome? No, it is not!
```

- Reverse:
- Input `word` is a palindrome

```
✨ Awesome. using the reverse for palindrome checking!

🔖 Going to check to see if the word civic is a palindrome!

😆 Is this word a palindrome? Yes, it is!
```

- Input `word` is not a palindrome

```
✨ Awesome. using the reverse for palindrome checking!

🔖 Going to check to see if the word taylor is a palindrome!

😆 Is this word a palindrome? No, it is not!
```

### What is the output from running the test suite with test coverage monitoring?

`poetry run task coverage`

```
=================================================================== test session starts ===================================================================
platform win32 -- Python 3.8.2, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\gforc\computer-science-101-fall-2021-ee-palindrome-checking-EvelynGriffith\palindromechecker
plugins: cov-3.0.0
collected 10 items

tests\test_main.py ....
tests\test_palindrome.py ....
tests\test_util.py ..

----------- coverage: platform win32, python 3.8.2-final-0 -----------
Name                              Stmts   Miss  Cover   Missing
---------------------------------------------------------------
palindromechecker\__init__.py         1      0   100%
palindromechecker\main.py            22      0   100%
palindromechecker\palindrome.py      18      1    94%   30
palindromechecker\util.py             5      0   100%
---------------------------------------------------------------
TOTAL                                46      1    98%


=================================================================== 10 passed in 0.61s ==================================================================== 
```

## Source Code

### Describe in detail how the completed source code works

#### An example of a test case for the command-line interface of the `palindromechecker`

```
def test_palindromechecker_recursive_is_palindrome():
    """Ensure that the command-line interface works for recursive approach."""
    result = runner.invoke(cli, ["--word", "civic", "--approach", "recursive"])
    assert result.exit_code == 0
    assert "recursive" in result.stdout
    assert "reverse" not in result.stdout
    assert "Yes, it is!" in result.stdout
    assert "civic" in result.stdout
```

This is the test case for the test_palindromechecker_recursive_is_palindrome function. This function is used to check the recursive_is_palindrome function within the palindrome.py file. The purpose of this function is to check a few key inputs and outputs for this function. Essentially what it does is it first checks whether we are running the correct approach for the function. This can be seen in lines five and six. Because it says that "Reverse" is "not in result.stdout" that means that we are going to be running the recursive function. By saying that something is not in the result.stdout, it is saying that that output or method for producing that output should not be in this function. You may be wondering how the function knows that "recursive" ties into the recursive functions? This is because we tied it into our class system at the top of the main.py file. This allows for us to tie the word "recursive" to the different function methods not only in our cli function but also into the test cases that function along with that file. The other thing that this test case does is it defines an output case that should work correctly, as in it is a palindrome. By saying in the final line "assert "civic" in result.stdout" the function is saying that "civic" should be considered a palindrome when run through the function. If it is not cosidered a palindrome then you know something is wrong with the function.

#### An example of a test case for the `util` module of the `palindromechecker`

```
def test_human_readable_boolean_true():
    """Ensure that a human-readable true boolean works correctly."""
    true_value = True
    true_value_human_readable = util.human_readable_boolean(true_value)
    assert true_value_human_readable == "Yes, it is!"
```

This source code is an example of a test case for our util.py file. The function in the util.py file is basically a boolean producing function that determines whether or not the palindrome functions are true or false and based on that output it produces a response that gives a human readible output (in this case it is either "Yes, it is", or "No, it is not!"). This test case is used to check whether or not the human_readible_boolean will actually produce the right output if given the input "True". This test case will define a new variable called true_value and set it equal to True. Then it will create a new variable called true_Value_human_Readible and ask that to call upon the human_readible_boolean function with the true_value variable as the input. This test case will then try to get that functin to produce the output of "yes, it is!" If it does produce that then we know that the function is working correctly.

#### An example of a test case for the `palindrome` module of the `palindromechecker`

```
def test_short_palindrome_word_reverse():
    """Ensure that a short word of "civic" works correctly."""
    # implement this test case using the provided example
    word = "civic"
    result = palindrome.is_palindrome_reverse(word)
    assert result is True
```

This test case is used to test the palindrome.py file functions. It will create a new variable called "word" and it will assing "civic" to that word then it will call upon the function with the input "civic". It will then assert that the function should produce True as it's answer and if it doesn't then we know that there is something wrong with the function.

## Professional Development

### Think of an appropriate activity that you associate with play. Make a list of the characteristics of that activity that make it seem playful. Are software testing and debugging also playful activities with the same characteristics? Why or why not?

My activity that I associate with "play" is singing. There are a lot of things that I like about singing. I like making and reading music, I like that it is a challenge that I also feel like I am good at. It makes me genuinely feel less stressed and it comes easily in some respects even though it is a challenge in others. I like the output that it produces and that it feels rewarding. I also like that it is a social or solo event depending on my mood. Finally, I like that I can choose any style of music to sing and that I can use singing for a lot of different things.

I think that software testing an debugging can sometimes be like this. I think that testing and debugging can be really frustrating if you don't feel like you are making any progress, but I also think it can be really rewarding once you figure out the answer. I also think that even though it does make me feel stressed at times, especially when it is required for an assignment with a deadline, it makes me feel like I am capable and that I could be successful with coding, and in this feild as a whole, if I am able to figure out what was wrong with the code.

### What was the greatest challenge that you faced when completing this assignment?

The greatest challenge I faced while doing this assignment actually came up after I had gotten everything to work. I finally got everything to produce an output and I thought that meant I was done and that everything was functioning correctly. However, when I tried to actually run the program with the word "taylor" it said that that word was a palindrome. This was when I realized that my code was saying that every word was a palindrome. I didn't really know what to do from this point because in my opinion, semantic errors are much harder to figure out than errors related to syntax. I also recognized this error as an overt, transient error which means that it isn't the hardest to figure out, but it also isnt the easiest.

### Leveraging your response to the previous question, how did you overcome the challenge?

To overcome this challenge I realized that I needed help from someone who had more knowlege than me. I ended up talking to a couple different TLs and eventually the solution that we came to was that in the reverse function we needed this line `x = [el for el in to_chars(s)]`. This line makes the function work properly. Another challenge that I faced has to do with the imports. What was happening was that whenever I changed my imports to match what the linters wanted to me to do, I failed my test cases. However, whenever I fixed my test cases, I failed my linters again. This struggle became really frustrating because I didn't know how I could move forward so that everything would pass. Eventually I just enlisted the help of Professor Kapfhammer who gave me an example of what my imports should look like. I decided to use his suggestio which was to delete my import typer. This works because I don't need typer to actually run the test suite. Even though this aspect of the project was frustrating, it was the first time that I learned that imports have to be inserted into the file in specific orders.
