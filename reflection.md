# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

(1) The hints were backwards. It says, "Go LOWER!", but the correct number is actually higher.
(2) When I click "Submit Guess," no hint is shown. I have to click twice to make the hint appear.
(3) After clicking the "New Game" button, I entered my guess and clicked "Submit," but it did not submit.

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

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
