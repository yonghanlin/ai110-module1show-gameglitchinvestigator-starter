# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  This game is about guessing a secret number. After entering your guess, it can give you a hint telling you whether to go higher or lower to get closer to the correct number.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  (1) The hints were backwards. It says, "Go LOWER!", but the correct number is actually higher.  
  (2) When I click "Submit Guess," no hint is shown. I have to click twice to make the hint appear.  
  (3) After clicking the "New Game" button after winning the game, it didn't start new game.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  I used Claude on this project. For bug (1), Claude’s suggestion was correct: the lines in check_guess() in app.py had the wrong return value. I verified this by stepping through the function myself. I also modified the code based on Claude’s suggestion and ran app.py again to test it in the web application.

  However, Claude’s suggestion for bug (2) was incorrect. Claude initially suggested fixing some lines in the "if submit" block (for example, lines 142 and 149). However, after I applied the suggested fix and ran the application, the bug still existed. After asking Claude several more times for a direct fix, I found that its suggestions still did not work. So I used st.write() to debug the issue myself and identified the problematic code. Then, I asked Claude to suggest how to fix the incorrect code I had found.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

  I verified the fixes by running both pytest and the Streamlit application multiple times to check whether the specific bugs were resolved. I ran test_too_high_hint_says_go_lower() and test_too_low_hint_says_go_higher() to confirm that bug (1) was fixed, and the results showed that my code was working correctly. Claude also helped me design the tests by suggesting the inputs and assertions.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

  I didn't experience the secret number changing in the original app, but I found three other bugs. First, the hints were reversed — it said "Go LOWER!" when the correct number was actually higher, which I fixed by correcting the comparison logic in check_guess. Second, clicking "Submit Guess" once showed no hint; it required two clicks, which I fixed by wrapping the input and buttons in st.form() so Streamlit only reruns when the form is submitted. Third, clicking "New Game" after winning didn't restart the game because st.session_state.status was still set to "won", so I reset it to "playing" along with clearing the history and calling st.rerun(). 
  
  Streamlit "reruns" means every time a user interacts  with anything on the page, Streamlit re-executes the entire Python script from top to bottom. Session state persists across reruns for a single user's session — whatever you store there survives the next rerun.
  
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

  I will continue the habit of verifying AI-generated code by using tests and manually checking it several times, since AI can give incorrect suggestions. I will also leave comments for myself indicating which lines of code were generated or assisted by AI. In addition, I will provide more detail in my prompts, make them clearer, and mention the files that I believe are causing the bugs.  

  One thing I would do differently next time when working with AI is to trust myself more. I found that I could sometimes debug faster than AI, especially when AI did not fully understand my prompt. After identifying the source of the bug, I could then use AI to suggest possible solutions. I feel this is a better way for me to work with AI, unless I cannot find the bug on my own for a long time.  

  This project changed the way I think about AI-generated code. I realized that AI does not always gives the best solution, although it is still helpful and can suggest ideas that I might not have thought of before.