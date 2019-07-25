PLUS, MINUS, NUM, EOF = "plus", "minus", "num", "eof"

class Token:
  
  def __init__(self, token_type, value):
    self.token_type = token_type
    self.value = value

  def __str__(self):
    return "(type:{},value:{})".format(self.token_type, self.value)


class Interpreter:

  def __init__(self, text):
    self.text = text
    self.pos = -1
    self.curr_token = None
    self.curr_char = None
  
  def error(self, s):
    raise RuntimeError(s)

  def next_char(self):
    self.pos += 1
    if self.pos >= len(self.text):
      self.curr_char = None
      return
    
    self.curr_char = self.text[self.pos]
  
  def back_char(self):
    self.pos -= 1
    self.curr_char = self.text[self.pos]

  def next_token(self):
    if self.pos >= len(self.text):
      self.curr_token = Token(EOF, None)
      return

    self.next_char()

    if self.curr_char == "+":
      self.curr_token = Token(PLUS, None)
      return

    if self.curr_char == "-":
      self.curr_token = Token(MINUS, None)
      return
    
    val = ""
    while True:
      if not self.curr_char:
        break
      if self.curr_char.isdigit():
        val += self.curr_char
        self.next_char()
      else:
        self.back_char()
        break

    if val:
      num = int(val)
      self.curr_token = Token(NUM, num)
      return

    self.error("No Token Left")

  def eat(self, token_type):
    if self.curr_token.token_type == token_type:
      self.next_token()
    else:
      self.error("syntax error")

  def expr(self):
    self.next_token()

    left = self.curr_token
    self.eat(NUM)

    sign = self.curr_token
    calc = None
    if sign.token_type == PLUS:
      self.eat(PLUS)
      calc = lambda x, y : x + y
    elif sign.token_type == MINUS:
      self.eat(MINUS)
      calc = lambda x, y : x - y
    else:
      self.error("sysntax error")

    right = self.curr_token
    self.eat(NUM)

    return calc(left.value, right.value)


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
