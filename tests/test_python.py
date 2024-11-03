"""
Tests for Context Manager exercise.
"""

import os
import sys
import io
import contextlib

def test_ContextManagers():
    # Add the exercise directory to the Python path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ContextManagers"))
    sys.path.append(exercise_dir)
    
    from main import suppress_output, noisy_sum_squared
    
    # First verify the function is still noisy when called directly
    string_buffer = io.StringIO()
    with contextlib.redirect_stdout(string_buffer):
        result = noisy_sum_squared(3)
    
    assert string_buffer.getvalue() != "", "Original function should print output"
    assert result == 5, "Original function returned wrong value"
    
    # Now test if output is suppressed when using suppress_output
    string_buffer = io.StringIO()
    with contextlib.redirect_stdout(string_buffer):
        result = suppress_output(noisy_sum_squared, 3)
    
    assert string_buffer.getvalue() == "", "Output was not properly suppressed"
    assert result == 5, "Wrong return value for noisy_sum_squared(3)"

