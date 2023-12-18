import matplotlib.pyplot as plt
import pandas as pd

# Load data
df = pd.read_csv('customers.csv', encoding='ISO-8859-1')

# Create scatter plot
colors = {'M': 'blue', 'F': 'pink'}
plt.scatter(df['CustomerName'], df['Age'], c=df['Gender'].map(colors))
plt.xticks(rotation=90)
plt.xlabel('Customer Name')
plt.ylabel('Age')
plt.title('Scatter Plot of Customer Age by Gender')
plt.show()
