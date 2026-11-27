# Instructor Outline (Draft): Predict the Output

**Topic:** Functions (print vs. return)
**Time:** about 20 minutes
**Materials:** printed worksheet (`worksheet.md`), one per student; a computer with Python (Thonny) to show answers

## Learning goals
- Students can explain the difference between `print` and `return`.
- Students can predict what a function call gives back and fix code that doesn't save a returned value.

## How to run it

1. **Introduce (2 min).** Hand out the worksheet. Tell students to predict first and not run the code yet.
2. **Prompt 1 (5 min).** Students predict on their own for 1 minute, then compare with their partner.
   Ask for a show of hands: "Who thinks it prints 10 twice? Who thinks 10 then None?"
   Run the code on the screen and ask one pair to explain why the second line is `None`.
3. **Prompt 2 (5 min).** Same steps. Show of hands: "Who thinks 20? Who thinks 25?"
   Run the code and ask a pair to explain why `price` didn't change.
4. **Prompt 3: Fix it (5 min).** Pairs rewrite both snippets. Walk around and check their fixes.
5. **Wrap-up (3 min).** Ask: "When should a function use `return` instead of `print`?"
   Sum up: `print` only shows a value on the screen, while `return` sends it back so the code can save and use it.

## What to look for
- **Predicts `10` twice in Prompt 1:** still thinks `print` gives back a value the same way `return` does.
- **Predicts `25` in Prompt 2:** thinks calling a function changes the variable even when the result isn't saved.
- **Correct fixes in Prompt 3** (`return x * 2` and `price = add_shipping(price)`) show the student can correct the mistake, not just spot it.
