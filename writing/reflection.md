# Palindrome Checking

## Evelyn Griffith

## Program Output

### Use four fenced code blocks to provide output from four different runs of `palindromechecker` with different inputs

TODO: Provide the complete command-line for your use of the `palindromechecker` program

TODO: Provide the output for running `palindromechecker` in the following configurations:

- Recursive:
  - Input `word` is a palindrome
  - Input `word` is not a palindrome

- Reverse:
  - Input `word` is a palindrome
  - Input `word` is not a palindrome

### What is the output from running the test suite with test coverage monitoring?

Provide the command that you used to run the coverage tracking for the test suite

`poetry run task test`

```
=================================================================== test session starts ===================================================================
platform win32 -- Python 3.8.2, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\gforc\computer-science-101-fall-2021-ee-palindrome-checking-EvelynGriffith\palindromechecker
plugins: cov-3.0.0
collected 10 items

tests\test_main.py ....
tests\test_palindrome.py ....
tests\test_util.py ..

=================================================================== 10 passed in 0.29s ==================================================================== 
```

## Source Code

### Describe in detail how the completed source code works

#### An example of a test case for the command-line interface of the `palindromechecker`

TODO: Use a fenced code block to provide the requested source code
TODO: Write at least one paragraph to explain the request source code

#### An example of a test case for the `util` module of the `palindromechecker`

TODO: Use a fenced code block to provide the requested source code
TODO: Write at least one paragraph to explain the request source code

#### An example of a test case for the `palindrome` module of the `palindromechecker`

TODO: Use a fenced code block to provide the requested source code
TODO: Write at least one paragraph to explain the request source code

## Professional Development

### Think of an appropriate activity that you associate with play. Make a list of the characteristics of that activity that make it seem playful. Are software testing and debugging also playful activities with the same characteristics? Why or why not?

My activity that I associate with "play" is singing. There are a lot of things that I like about singing. I like making and reading music, I like that it is a challenge that I also feel like I am good at. It makes me genuinely feel less stressed and it comes easily in some respects even though it is a challenge in others. I like the output that it produces and that it feels rewarding. I also like that it is a social or solo event depending on my mood. Finally, I like that I can choose any style of music to sing and that I can use singing for a lot of different things.

I think that software testing an debugging can sometimes be like this. I think that testing and debugging can be really frustrating if you don't feel like you are making any progress, but I also think it can be really rewarding once you figure out the answer. I also think that even though it does make me feel stressed at times, especially when it is required for an assignment with a deadline, it makes me feel like I am capable and that I could be successful with coding and in this feild as a whole if I am able to figure out what was wrong with the code.

### What was the greatest challenge that you faced when completing this assignment?

TODO: Provide a one-paragraph response that answers this question in your own words.
TODO: Provide a response to this question that is different from any previous answers.

The greatest challenge I faced while doing this assignment actually came up after I had gotten everything to work. I finally got everything to produce an output and I thought that meant I was done and that everything was functioning correctly. However, when I tried to actually run the program with the word "taylor" it said that that word was a palindrome. This was when I realized that my code was saying that every word was a palindrome. I didn't really know what to do from this point because in my opinion, semantic errors are much harder to figure out than errors related to syntax. I also recognized this error as an overt, transient error which means that it isn't the hardest to figure out, but it also isnt the easiest.

### Leveraging your response to the previous question, how did you overcome the challenge?

TODO: Provide a one-paragraph response that answers this question in your own words.
TODO: Provide a response to this question that is different from any previous answers.
