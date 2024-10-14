from test_lib import test, report

def snapint(int): return round(int * 20) / 20

print(snapint(1301.02))
print(snapint(305.99))

input = snapint(122.00)
expect_content = 122.0
name = f'input: {input} output: {snapint(input)}'
test(name, expect_content, snapint(input))

input = snapint(2398.95)
expect_content = 2398.95
name = f'input: {input} output: {snapint(input)}'
test(name, expect_content, snapint(input))

input = snapint(224.23)
expect_content = 224.25
name = f'input: {input} output: {snapint(input)}'
test(name, expect_content, snapint(input))

input = snapint(1301.02)
expect_content = 1301.0
name = f'input: {input} output: {snapint(input)}'
test(name, expect_content, snapint(input))

input = snapint(305.99)
expect_content = 306.0
name = f'input: {input} output: {snapint(input)}'
test(name, expect_content, snapint(input))

if __name__ == "__main__": report()
