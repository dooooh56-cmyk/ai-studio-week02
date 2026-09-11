class Customer:
  def __init__(self, name, grade='basic', points=0):
    self.name = name
    self.grade = grade
    self.points = points

  def add_points(self, amount):
    """구매 금액의 5%를 포인트로 적립한다."""
    self.points += int(amount * 0.05)

  def get_discount_rate(self):
    """vip는 0.10, basic은 0.03 할인"""
    if self.grade == 'vip':
      return 0.10
    return 0.03
  
  def summary(self):
    """ "[vip] 김서강 (포인트: 2,250)” 형식 문자열 반환 """
    return f"[{self.grade}] {self.name} (포인트: {self.points:,})"

class Order:
  def __init__(self, order_id, customer, items):
    self.order_id = order_id
    self.customer = customer
    self.items = items

  def total_price(self):
    """고객 등급 할인 적용 총액 반환 """
    subtotal = sum(price for _, price in self.items)
    discount = self.customer.get_discount_rate()
    return (subtotal * (1-discount))

  def add_item(self, name, price):
    self.items.append((name, price))
    self.customer.add_poits(price)

  def pay(self):
    final_price = self.total_price()
    self.customer.add_points(final_price)

c1 = Customer('김서강', 'vip', 2250)
c2 = Customer('최소강')

o1 = Order("A-1001", c1, [("아메리카노", 2000), ("카페라떼", 3500)])
o2 = Order("A-1002", c2, [("말차라떼", 5000), ('바닐라라떼', 3000)])
o3 = Order("A-1003", c1, [("초코케이크", 8000)])

o1.pay()
print(f"{o1.customer.name}님의 결제 금액: {o1.total_price():,}원")
print(f"{o1.customer.summary()}")

o2.pay()
print(f"{o2.customer.name}님의 결제 금액: {o2.total_price():,}원")
print(f"{o2.customer.summary()}")

o3.pay()
print(f"{o3.customer.name}님의 결제 금액: {o3.total_price():,}원")
print(f"{o3.customer.summary()}")