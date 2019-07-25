PLUS, NUM, EOF = "plus", "num", "eof"

class Token:
  
  def __init__(self, token_type, value):
    self.token_type = token_type
    self.value = value

  def __str__(self):
    return "(type:{},value:{})".format(self.token_type, self.value)


class Interpreter:

  def __init__(self, text):
    self.text = text
    self.pos = 0
    self.curr_token = None
  
  def error(self, s):
    raise RuntimeError(s)

  def next_token(self):
    if self.pos >= len(self.text):
      return Token(EOF, None)

    text = self.text
    curr_char = text[self.pos]

    if curr_char == "+":
      self.pos += 1
      return Token(PLUS, None)
    elif curr_char.isdigit():
      val = int(curr_char)
      self.pos += 1
      return Token(NUM, val)
    else:
      self.error("No Token Left")

  def eat(self, token_type):
    if self.curr_token.token_type == token_type:
      self.curr_token = self.next_token()
    else:
      self.error("syntax error")

  def expr(self):
    self.curr_token = self.next_token()

    left = self.curr_token
    self.eat(NUM)

    plus = self.curr_token
    self.eat(PLUS)

    right = self.curr_token
    self.eat(NUM)

    return left.value + right.value


def main():
  while True:
    try:
      text = input("expr> ")
    except Exception:
      print("EOF Error")
    if (text == "q"):
      print("bye bye")
      break
    i = Interpreter(text)
    print(i.expr())

if __name__ == "__main__":
  main()
