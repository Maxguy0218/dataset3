import streamlit as st
import pandas as pd

def main():
    st.title("View Dataset")

    # Load the dataset
    df = pd.read_csv("Inventory dataset.csv")  # Replace "your_dataset.csv" with your dataset file path

    # Display the dataset
    st.write(df)

    # You can also display specific parts of the dataset, for example:
    # Display the first 10 rows of the dataset
    st.write("First 10 rows of the dataset:")
    st.write(df.head(10))

    # Display summary statistics of the dataset
    st.write("Summary statistics of the dataset:")
    st.write(df.describe())

if __name__ == "__main__":
    main()
