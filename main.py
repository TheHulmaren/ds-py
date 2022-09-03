from package.stack.LLStack import LLStack

a = LLStack()
a.push(2).push(4).push(7)
print(a)

print(a.pop())
print(a)

a.push(10).push(11).push(0)
print(a)

print(a.top())

print(a.pop())
print(a.pop())
print(a)