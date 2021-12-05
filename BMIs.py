import pandas as pd
import numpy as np
class BMIs:
    Health_risk = ['Malnutrition risk', 'Low risk', 'Enhanced risk', 'Medium risk', 'High risk', 'Very high risk']
    BMI_category = ['Underweight', 'Normal weight', 'Overweight', 'Moderately obese', 'Severely obese', 'Very severely obese']

    def bmi_calculator(self, input):
        try:
            self.df = pd.read_json(input)
            if(not(self.df.empty) and self.df.columns[0]=='Gender' and self.df.columns[1]== 'HeightCm' and self.df.columns[2]== 'WeightKg' ):
                self.df['BMI'] = round(self.df['WeightKg']/ (self.df['HeightCm'] / 100) ** 2, 2)
                check = [
                    (self.df['BMI'] <= 18.4),
                    (self.df['BMI'] >= 18.5) & (self.df['BMI'] <= 24.9),
                    (self.df['BMI'] >= 25) & (self.df['BMI'] <= 29.9),
                    (self.df['BMI'] >= 30) & (self.df['BMI'] <= 34.9),
                    (self.df['BMI'] >= 35) & (self.df['BMI'] <= 39.9),
                    (self.df['BMI'] >= 40)
                ]
                self.df['BMI_category'] = np.select(check, self.BMI_category)
                self.df['Health_risk'] = np.select(check, self.Health_risk)
            else:
                print("dataframe is not correct")
                df=[]
        except:
            print("dataframe is not correct")
            df = []
        finally:
            return self.df



    @staticmethod
    def count_overweight(df):
        try:
            overweight_Count = df['BMI_category'].where(df['BMI_category'] == 'Overweight').count()
        except:
            overweight_Count=0
        finally:
            return overweight_Count



if __name__ == '__main__':
    j = '''[ {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
    { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
    { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
    { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82} ]'''
    m = BMIs()
    print(m.bmi_calculator(j))

    print(BMIs.count_overweight(m.df))







































