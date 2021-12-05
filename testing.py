import unittest
import BMIs as BMIsClass
import pandas as pd


class MyTestCase(unittest.TestCase):

    # This is a setup method, gets called before every test case
    def setUp(self):
        self.objBMI = BMIsClass.BMIs()  # instantiate the Person Class

    def test_positive_case_1(self):
        input = '''[ {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
           { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
           { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
           { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
           {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
           {"Gender": "Female", "HeightCm": 167, "WeightKg": 82} ]'''
        output = pd.read_json(input)
        df = self.objBMI.bmi_calculator(input)
        self.assertEqual(1, self.objBMI.count_overweight(df))
        output['BMI'] = [32.83, 32.79, 23.77, 22.50, 31.11, 29.40]
        output['BMI_category'] = ['Moderately obese', 'Moderately obese', 'Normal weight', 'Normal weight',
                                  'Moderately obese', 'Overweight']
        output['Health_risk'] = ['Medium risk', 'Medium risk', 'Low risk', 'Low risk', 'Medium risk', 'Enhanced risk']
        self.assertTrue(df.equals(output))

    def test_positive_case_2(self):
        input = '''[ {"Gender": "Male", "HeightCm": 171, "WeightKg": 86 },
           { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
           { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
           { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
           {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
           {"Gender": "Female", "HeightCm": 167, "WeightKg": 82} ]'''
        output = pd.read_json(input)
        df = self.objBMI.bmi_calculator(input)
        self.assertEqual(2, self.objBMI.count_overweight(df))
        output['BMI'] = [29.41, 32.79, 23.77, 22.50, 31.11, 29.40]
        output['BMI_category'] = ['Overweight', 'Moderately obese', 'Normal weight', 'Normal weight',
                                  'Moderately obese', 'Overweight']
        output['Health_risk'] = ['Enhanced risk', 'Medium risk', 'Low risk', 'Low risk', 'Medium risk', 'Enhanced risk']
        self.assertTrue(df.equals(output))

    def test_negative_case_1(self):
        input = '[]'
        output = pd.read_json(input)
        df = self.objBMI.bmi_calculator(input)
        self.assertEqual(0, self.objBMI.count_overweight(df))
        self.assertTrue(df.equals(pd.DataFrame()))



if __name__ == '__main__':
    unittest.main()
