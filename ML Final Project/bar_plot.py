import matplotlib.pyplot as plt


def plot_name_values(data):
    names, values = zip(*data)

    plt.figure(figsize=(8, 6))
    bars = plt.bar(names, values, color='skyblue', edgecolor='black')

    plt.xlabel('Names', fontsize=12)
    plt.ylabel('Values', fontsize=12)

    plt.xticks(rotation=45, ha='right', fontsize=10)

    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval:.3f}', ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.show()
