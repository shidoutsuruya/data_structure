while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)