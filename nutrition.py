import api_access as api
import sqlite3

class Nutrition:
    def __init__(self):
        pass
    
    def get_nutrition(self, food_name, calories, protein):
        self.food_name = food_name
        self.calories = calories
        self.protein = protein
        
        api.api_call(self.food_name)
        
        return self.food_name, self.calories, self.protein
    
    def log_nutrition(self):
        log = self.get_nutrition(self.food_name, self.calories, self.protein)
        return log
    
    
    