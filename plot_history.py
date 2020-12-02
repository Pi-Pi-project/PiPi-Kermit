import matplotlib.pyplot as plt

def plot_model(model_history, filename):
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))

    axs[0].plot(model_history.history["accuracy"], "y", label="train_acc")
    axs[0].plot(model_history.history["val_accuracy"], "r", label="val_acc")

    axs[0].set_title("Model Accuracy")
    axs[0].set_ylabel("Accuracy")
    axs[0].set_xlabel("Epoch")

    axs[0].legend(["train", "validation"], loc="best")

    # loss history 요약
    axs[1].plot(model_history.history["loss"], "b", label="train_loss")
    axs[1].plot(model_history.history["val_loss"], "g", label="val_loss")

    axs[1].set_title("Model Loss")
    axs[1].set_ylabel("Loss")
    axs[1].set_xlabel("Epoch")

    axs[1].legend(["train", "validation"], loc="best")

    fig.savefig("./img/" + str(filename) + ".png")
    plt.show()