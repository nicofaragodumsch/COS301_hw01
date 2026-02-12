# Inline comment key: [G] = "generated with AI" (not manually written by a human)
import re #[G]

# --- 1. Basic Math Functions (Placeholders) ---#[G]
def add(a, b): #[G]
    return a + b #[G]

def subtract(a, b):#[G]
    return a - b #[G]

# --- 2. Helper: Evaluates logic inside a single set of parens ---#[G]
def evaluate_flat_expression(expression): #[G]
    """
    Parses a string without parentheses (e.g., "5 - 20" or "5 - 2 - 1") #[G]
    and calculates the result left-to-right. #[G]
    """
    # Remove all whitespace for easier parsing #[G]
    expression = expression.replace(" ", "") #[G]
    
    # This regex finds all numbers (including negatives) and operators separately#[G]
    # Pattern explanation: #[G]
    # (?<!\d)-?\d+  : Matches a number (potentially negative) ensuring it's not a subtraction operator following a digit #[G]
    # [+-]          : Matches operators #[G]
    # This is a basic tokenizer for integers #[G]
    tokens = re.findall(r'(?<!\d)-?\d+|[+-]', expression) #[G]
    
    if not tokens: #[G]
        return 0 #[G]
        
    # Start with the first number #[G]
    current_value = int(tokens[0]) #[G]
    
    # Iterate through the rest of the tokens in pairs (operator, number) #[G]
    i = 1 #[G]
    while i < len(tokens): #[G]
        operator = tokens[i] #[G]
        next_number = int(tokens[i+1]) #[G]
        
        if operator == '+': #[G]
            current_value = add(current_value, next_number) #[G]
        elif operator == '-': #[G]
            current_value = subtract(current_value, next_number) #[G]
            
        i += 2 # Move to the next operator #[G]
        
    return current_value #[G]

# --- 3. Main Recursive Function --- #[G]
def recursive_parentheses_solver(expression): #[G]
    """
    Recursively finds the innermost, leftmost parentheses, evaluates them, #[G]
    and replaces them in the string until no parentheses remain. #[G]
    """
    # Base Case: If there are no closing parentheses, we are done with recursion. #[G]
    # We allow the function to return the final simplified string. #[G]
    if ')' not in expression: #[G]
        # Optional: Evaluate the final string if it's just a math expression #[G]
        # return evaluate_flat_expression(expression) #[G]
        return expression.strip() #[G]

    # Step 1: Find the FIRST closing parenthesis ')' #[G]
    # This ensures we are finding the termination of the leftmost set. #[G]
    close_index = expression.find(')') #[G]
    
    # Step 2: Find the LAST open parenthesis '(' BEFORE the closing index. #[G]
    # This ensures we have found the "innermost" pair. #[G]
    # We slice the string up to close_index to search backwards. #[G]
    open_index = expression.rfind('(', 0, close_index) #[G]
    
    # Step 3: Extract the content inside these parentheses #[G]
    inner_content = expression[open_index + 1 : close_index] #[G]
    
    # Step 4: Evaluate the content #[G]
    # (e.g., turns "5 - 20" into -15) #[G]
    result = evaluate_flat_expression(inner_content) #[G]
    
    # Step 5: Reconstruct the string #[G]
    # Replace (inner_content) with the calculated result #[G]
    # We rely on str() to convert the integer result back to text #[G]
    new_expression = ( #[G]
        expression[:open_index] + #[G]
        str(result) + #[G]
        expression[close_index + 1:]#[G]
    )
    
    print(f"Found: ({inner_content}) -> Evaluated to: {result} -> New Expression: {new_expression}") #[G]

    # Step 6: Recursive Call #[G]
    return recursive_parentheses_solver(new_expression) #[G]

# --- Usage Example --- #[G]
expression_string = "ans = (17 - (5 - 20)) - (1 - 11)" #[G]

print(f"Original: {expression_string}\n") #[G]
final_result = recursive_parentheses_solver(expression_string) #[G]
print(f"\nFinal Result: {final_result}") #[G]