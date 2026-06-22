# main.py
class MyChatLogic:
    def __init__(self):
        self.points_per_dollar = 25 
        self.min_withdrawal_usd = 10
        self.min_points_needed = self.min_withdrawal_usd * self.points_per_dollar

    def calculate_withdrawal(self, user_points):
        """Kalkile si itilizatè a ka retire lajan"""
        if user_points >= self.min_points_needed:
            amount = user_points / self.points_per_dollar
            return f"Ou ka retire {amount}$"
        return f"Ou bezwen {self.min_points_needed} pwen pou 10$."

    def validate_moncash(self, number):
        """Validasyon senp pou nimewo MonCash"""
        return len(number) == 8 and number.isdigit()

# Egzanp Lojik
mychat = MyChatLogic()
# Moun nan gen 300 pwen
print(mychat.calculate_withdrawal(300))
