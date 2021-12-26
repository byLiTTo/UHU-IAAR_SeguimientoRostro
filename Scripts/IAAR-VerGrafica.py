import matplotlib.pyplot as plt
import pandas as pd
import argparse
    
parser = argparse.ArgumentParser(description='Show metric evolution')

parser.add_argument('files',
                    type=str,
                    nargs=1)

args = parser.parse_args()

resultados = pd.read_csv(args.files[0])

plt.figure()
plt.plot(resultados["train_loss"].tolist(), label="Training")
plt.plot(resultados["val_loss"].tolist(), label="Validation")
plt.legend(loc='best')
plt.xlabel('Épocas')
plt.title('Loss')
plt.grid(True)
plt.show(block=False)

plt.figure()
plt.plot(resultados["train_regression_loss"].tolist(), label="Training")
plt.plot(resultados["val_regression_loss"].tolist(), label="Validation")
plt.legend(loc='best')
plt.xlabel('Épocas')
plt.title('Regression Loss')
plt.grid(True)
plt.show(block=False)

plt.figure()
plt.plot(resultados["train_classification_loss"].tolist(), label="Training")
plt.plot(resultados["val_classification_loss"].tolist(), label="Validation")
plt.legend(loc='best')
plt.xlabel('Épocas')
plt.title('Classification Loss')
plt.grid(True)
plt.show(block=False)

plt.show()


# "train_loss,train_regression_loss,train_classification_loss,val_loss,val_regression_loss,val_classification_loss"