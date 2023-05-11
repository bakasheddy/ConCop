# <cnetre> ConCop </centre>
### <centre> by </centre>
## <centre> Shedrack David </centre>

#### click [here](https://bakasheddy-concop-concop-wenurc.streamlit.app/) to view live model

# About the dataset
The lack of legitimate datasets on mobile money transac-tions to perform research on in the domain of fraud detection is a big problem today in the scientific community. Part of the problem is the intrinsic private nature of financial transactions, that leads to no public available datasets. This will leave the researchers with the burden of first harnessing the dataset before performing the actual researchon it. This paper propose an approach to such a problemthat we named the PaySim simulator.

PaySim is a financial simulator that simulates mobilemoney transactions based on an original dataset. In thispaper, we present a solution to ultimately yield the pos-sibility to simulate mobile money transactions in such away that they become similar to the original dataset. Withtechnology frameworks such as Agent-Based simulationtechniques, and the application of mathematical statistics,we show in this paper that the simulated data can be asprudent as the original dataset for research.
This particular dataset was gotten from kaggle, it contains 6,362,620 data points with 11 columns which captures transactions that has occured in the simulator, both legitimate and fraudulent.

Below are the column reference:

- step: represents a unit of time where 1 step equals 1 hour
- type: type of online transaction
- amount: the amount of the transaction
- nameOrig: customer starting the transaction
- oldbalanceOrg: balance before the transaction
- newbalanceOrig: balance after the transaction
- nameDest: recipient of the transaction
- oldbalanceDest: initial balance of recipient before the transaction
- newbalanceDest: the new balance of recipient after the transaction
- isFraud: fraud transaction
