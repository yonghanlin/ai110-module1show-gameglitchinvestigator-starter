from logic_utils import check_guess

#FIX: Modified the test to align with the bug I fix using Claude
def test_too_high_hint_says_go_lower():
    # When guess > secret, the hint must tell the player to go lower, not higher.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected hint to say LOWER, got: {message}"

def test_too_low_hint_says_go_higher():
    # When guess < secret, the hint must tell the player to go higher, not lower.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected hint to say HIGHER, got: {message}"

def test_check_guess_numeric_order_when_secret_is_string():
    # 9 < 10 numerically, so outcome must be "Too Low"
    outcome, message = check_guess(9, "10")
    assert outcome == "Too Low", f"Expected 'Too Low' but got '{outcome}' (possible lexicographic comparison bug)"

def test_check_guess_too_high_when_secret_is_string():
    # 20 > 10 numerically, so outcome must be "Too High"
    outcome, message = check_guess(20, "10")
    assert outcome == "Too High"

def test_check_guess_win_when_secret_is_string():
    # Exact match should still be a win when secret is passed as a string
    outcome, message = check_guess(42, "42")
    assert outcome == "Win"

