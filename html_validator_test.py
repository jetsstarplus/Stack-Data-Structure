
test_code = '''
def test():
    HtmlValidator()
'''

if __name__=="__main__":
    import timeit
    time_taken=timeit.repeat(stmt=test_code, setup="from html_validator import HtmlValidator", repeat=5)
    print(time_taken)
    print(f'Average time {sum(time_taken)/5}')

# 0.23717257499993138