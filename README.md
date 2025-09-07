# Placement Prediction using Logistic Regression

This project implements a simple **Placement Prediction Model** using **Logistic Regression** in Python. The model predicts whether a student will get placed based on their **CGPA** and **IQ** scores.

---

## **Dataset**

The dataset used is a CSV file (`placement.csv`) containing at least the following columns:

- `cgpa` – Cumulative Grade Point Average of the student.
- `iq` – IQ score of the student.
- `placement` – Target variable (1 = Placed, 0 = Not Placed).

> Make sure to update the dataset path in the code before running.

---

## **Dependencies**

The code uses the following Python libraries:

- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`

Install them using pip if you don’t have them already:

```bash
pip install pandas matplotlib seaborn scikit-learn
