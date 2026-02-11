import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nilai.siswa.csv')
print(data.head())
print(data.info())
print(data.describe())

print("Rata Rata:", data['nilai'].mean())
print("Median:", data['nilai'].median())
print("Modus:", data['nilai'].mode()[0])

# matematika = data[data['mata_pelajaran'] == 'Matematika']
# print(matematika)

# Inggris = data[data['mata_pelajaran'] == 'Bahasa Inggris']
# print(Inggris)

# Indonesia = data[data['mata_pelajaran'] == 'Bahasa Indonesia']
# print(Indonesia)

# data.groupby('Mapel')['Nilai'].agg(['max','min'])
# rata = data.groupby('Mapel')['Nilai'].mean()
# rata.plot(kind='bar')
# plt.title('Rata-Rata Nilai per Mapel')
# plt.xlabel('Mata Pelajaran')
# plt.ylabel('Nilai Rata-Rata')
# plt.show()

# sns.boxplot(x='Mapel', y='Nilai', data=data)
# sns.boxplot(x='Mapel', y='Nilai', data=data)
# plt.show()