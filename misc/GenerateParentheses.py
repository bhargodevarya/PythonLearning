def generate_all_valid_parentheses(count):
    recur(count, '', count, count)

def recur(count, current: str, opening_count, closing_count):
    if len(current) == 2*count:
        print(current)
        return
    
    if opening_count > 0:
        current += '('
        opening_count -= 1
        recur(count, current, opening_count, closing_count)
    
    if closing_count > opening_count:
        current += ')'
        closing_count -= 1
        recur(count, current, opening_count, closing_count)


generate_all_valid_parentheses(2)
