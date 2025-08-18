# data_module.py
import matplotlib.pyplot as plt
import pandas as pd

Y7_NAPLAN_Results_df = pd.read_csv('Unformatted Pre-2023 Year 7 Reading and Writing NAPLAN Results.csv')

def display_dataset_preview():
    print(Y7_NAPLAN_Results_df)

def display_reading_visualisation():
    axis = Y7_NAPLAN_Results_df.plot(
               kind='line',
               x='Year',
               y='Male Reading % at or above NMS',
               color='blue',
               alpha=0.3,
               title='Year 7 NAPLAN Reading Results by Gender'
              )

    Y7_NAPLAN_Results_df.plot(
               kind='line',
               x='Year',
               y='Female Reading % at or above NMS',
               color='red',
               alpha=0.3,
               ax=axis
              )
    plt.show()


def display_writing_visualisation():
    axis = Y7_NAPLAN_Results_df.plot(
               kind='line',
               x='Year',
               y='Male Writing % at or above NMS',
               color='blue',
               alpha=0.3,
               title='Year 7 NAPLAN Writing Results by Gender'
              )
    
    Y7_NAPLAN_Results_df.plot(
               kind='line',
               x='Year',
               y='Female Writing % at or above NMS',
               color='red',
               alpha=0.3,
               ax=axis
              )
    plt.show()

def display_averages():
    print(f"\n=== Reading Averages ===")
    Y7_NAPLAN_Results_df['Male Reading Mean / (S.D.)'] = Y7_NAPLAN_Results_df['Male Reading Mean / (S.D.)'].str.split(' ').str[0].astype(float)
    m_r_mean = Y7_NAPLAN_Results_df['Male Reading Mean / (S.D.)'].mean()
    print(f"mean of male reading scores = {m_r_mean}")

    Y7_NAPLAN_Results_df['Female Reading Mean / (S.D.)'] = Y7_NAPLAN_Results_df['Female Reading Mean / (S.D.)'].str.split(' ').str[0].astype(float)
    f_r_mean = Y7_NAPLAN_Results_df['Female Reading Mean / (S.D.)'].mean()
    print(f"mean of female reading scores = {f_r_mean}")

    print(f"\n=== Writing Averages ===")
    Y7_NAPLAN_Results_df['Male Writing Mean / (S.D.)'] = Y7_NAPLAN_Results_df['Male Writing Mean / (S.D.)'].str.split(' ').str[0].astype(float)
    m_w_mean = Y7_NAPLAN_Results_df['Male Writing Mean / (S.D.)'].mean()
    print(f"mean of male writing scores = {m_w_mean}")

    Y7_NAPLAN_Results_df['Female Writing Mean / (S.D.)'] = Y7_NAPLAN_Results_df['Female Writing Mean / (S.D.)'].str.split(' ').str[0].astype(float)
    f_w_mean = Y7_NAPLAN_Results_df['Female Writing Mean / (S.D.)'].mean()
    print(f"mean of female writing scores = {f_w_mean}")

    user_input = input(f"\nWould you like to see this data in a graph?")
    if user_input == "Yes":
        avgs_graph = pd.DataFrame([
                        ['Male Reading Mean', m_r_mean,],
                        ['Female Reading Mean', f_r_mean,],
                        ['Male Writing Mean', m_w_mean,],
                        ['Female Writing Mean', f_w_mean,],
                        ],
                        columns = ['Means', 'Mean Scores']
                        )

        avgs_graph.plot(
                    kind='bar',
                    x='Means',
                    y='Mean Scores',
                    color=['blue', 'red', 'blue', 'red'],
                    alpha=0.3,
                    legend=False,
                    title='Averages of NAPLAN Writing and Reading Results by Gender'
                     )
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        plt.show()

    elif input == "No":
        pass
    else:
        print("Invalid. Please input Yes or No.")