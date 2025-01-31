import streamlit as st
import matplotlib.pyplot as plt
import math

class Line:
    def __init__(self):
        self.get_task()
    
    def get_task(self):
        task = st.sidebar.selectbox("What do you have?", 
                                    ["Two Points", "One Point with Slope", "One Point with Intercept", 
                                     "Slope and Intercept Form", "Distance Between Two Points", 
                                     "Distance from Point to Line"])
        
        if task == "Two Points":
            self.two_points()
        elif task == "One Point with Slope":
            self.point_and_slope()
        elif task == "One Point with Intercept":
            self.point_and_intercept()
        elif task == "Slope and Intercept Form":
            self.slope_and_intercept()
        elif task == "Distance Between Two Points":
            self.two_point_distance()
        elif task == "Distance from Point to Line":
            self.distance_point_line()
    
    def validate_float_input(self, prompt):
        return st.number_input(prompt, value=0.0)
    
    def two_points(self, x1=None, y1=None, x2=None, y2=None):
        if None in (x1, y1, x2, y2):
            x1, y1 = self.validate_float_input("Enter x1: "), self.validate_float_input("Enter y1: ")
            x2, y2 = self.validate_float_input("Enter x2: "), self.validate_float_input("Enter y2: ")
        
        a = y2 - y1
        b = x1 - x2
        c = a * x1 + b * y1

        if b == 0:
            st.write(f"The line passing through the points is: x = {x1}")
        elif a == 0:
            st.write(f"The line passing through the points is: y = {y1}")
        else:
            st.write(f"The line passing through the points is: {a}x + {b}y = {c}")
        
        self.plot_line(a, b, c, x1, y1, x2, y2)
    
    def point_and_slope(self, m=None, x=None, y=None):
        if m is None and x is None and y is None:
            m = self.validate_float_input("Enter the slope: ")
            x, y = self.validate_float_input("Enter x: "), self.validate_float_input("Enter y: ")
        
        c = y - m * x
        st.write(f"The line equation is: y = {m}x + {c}")
        
        self.plot_line(m, -1, c, x, y)
    
    def point_and_intercept(self, c=None, x=None, y=None):
        if c is None and x is None and y is None:
            c = self.validate_float_input("Enter the y-intercept: ")
            x, y = self.validate_float_input("Enter x: "), self.validate_float_input("Enter y: ")
        
        self.two_points(0, c, x, y)
    
    def slope_and_intercept(self, m=None, c=None):
        if m is None and c is None:
            m = self.validate_float_input("Enter the slope (m): ")
            c = self.validate_float_input("Enter the y-intercept (c): ")
        
        st.write(f"The line equation is: y = {m}x + {c}")
        
        self.plot_line(m, -1, c)
    
    def two_point_distance(self, x1=None, x2=None, y1=None, y2=None):
        if None in (x1, x2, y1, y2):
            x1, y1 = self.validate_float_input("Enter x1: "), self.validate_float_input("Enter y1: ")
            x2, y2 = self.validate_float_input("Enter x2: "), self.validate_float_input("Enter y2: ")
        
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        st.write(f'Distance between point A and point B is {distance:.2f}')
        
        self.plot_points(x1, y1, x2, y2)
    
    def distance_point_line(self, x=None, y=None, a=None, b=None, c=None):
        if None in (a, b, c, x, y):
            x, y = self.validate_float_input("Enter x: "), self.validate_float_input("Enter y: ")
            a, b, c = self.validate_float_input("Enter coefficient a: "), self.validate_float_input("Enter coefficient b: "), self.validate_float_input("Enter intercept c: ")
        
        numerator = abs(a * x + b * y + c)
        denominator = math.sqrt(a**2 + b**2)
        if denominator > 0:
            distance = numerator / denominator
            st.write(f'Distance between point and the line is {distance:.2f} unit')
        else:
            st.write("Invalid line equation provided.")
        
        self.plot_line(a, b, c, x, y)
    
    def plot_line(self, a, b, c, x1=None, y1=None, x2=None, y2=None):
        fig, ax = plt.subplots()
        
        if b == 0:
            ax.axvline(x=x1, color='r', label=f'x = {x1}')
        elif a == 0:
            ax.axhline(y=y1, color='r', label=f'y = {y1}')
        else:
            x_values = [x1, x2] if x1 is not None and x2 is not None else [-10, 10]
            y_values = [(-a * x + c) / b for x in x_values]
            ax.plot(x_values, y_values, label=f'{a}x + {b}y = {c}')
        
        if x1 is not None and y1 is not None:
            ax.scatter(x1, y1, color='b', label='Point 1')
        if x2 is not None and y2 is not None:
            ax.scatter(x2, y2, color='g', label='Point 2')
        
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)
    
    def plot_points(self, x1, y1, x2, y2):
        fig, ax = plt.subplots()
        ax.scatter(x1, y1, color='b', label='Point 1')
        ax.scatter(x2, y2, color='g', label='Point 2')
        ax.plot([x1, x2], [y1, y2], 'r--', label='Distance')
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

# Streamlit app
st.title("Line Visualization App")
line = Line()