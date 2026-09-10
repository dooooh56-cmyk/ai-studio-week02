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