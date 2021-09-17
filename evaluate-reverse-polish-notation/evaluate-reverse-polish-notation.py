class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      st = []
      for item in tokens:
        if item == '+':
          op1 = st.pop()
          op2 = st.pop()
          st.append(op1 + op2)
        elif item == '-':
          op1 = st.pop()
          op2 = st.pop()
          st.append(op2 - op1)
        elif item == '*':
          op1 = st.pop()
          op2 = st.pop()
          st.append(op1 * op2)
        elif item == '/':
          op1 = st.pop()
          op2 = st.pop()
          st.append(int(op2 / op1))
        else:
          st.append(int(item))
      return st.pop()