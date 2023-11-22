import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_random_data(seed=0, size=(100, 2)):
    """Generate random data with a given seed."""
    np.random.seed(seed)
    return np.random.randn(*size)

def plot_descriptive_statistics(ax, data):
    """각 변수의 평균과 중앙값에 대한 막대 그래프를 그립니다."""
    variables = [data[:, 0], data[:, 1]]
    labels = ['Variable 1', 'Variable 2']
    colors = ['blue', 'green']

    for i, (variable, label, color) in enumerate(zip(variables, labels, colors)):
        ax.bar(['평균', '중앙값'], [np.mean(variable), np.median(variable)], color=color, alpha=0.7, label=label)

    ax.legend()
    ax.set_title('기술통계: 평균과 중앙값')

def plot_correlation_analysis(ax, data):
    """상관 분석을 위한 히트맵을 그립니다."""
    sns.heatmap(np.corrcoef(data.T), annot=True, ax=ax)
    ax.set_title('상관 분석')

def plot_histogram(ax, data):
    """각 변수에 대한 히스토그램을 그립니다."""
    colors = ['blue', 'green']
    labels = ['Variable 1', 'Variable 2']

    for variable, color, label in zip(data.T, colors, labels):
        ax.hist(variable, bins=15, color=color, alpha=0.7, label=label)

    ax.legend()
    ax.set_title('변수의 히스토그램')

def plot_scatter(ax, data):
    """변수 1 대 변수 2의 산점도를 그립니다."""
    ax.scatter(data[:, 0], data[:, 1], alpha=0.7)
    ax.set_xlabel('Variable 1')
    ax.set_ylabel('Variable 2')
    ax.set_title('변수 1 대 변수 2의 산점도')

def main():
    # 난수 데이터 생성
    data = generate_random_data(seed=0, size=(100, 2))

    # 2x2 서브플롯 생성
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # 다양한 분석 부분을 그릴 수 있는 모듈화된 함수 호출
    plot_descriptive_statistics(axes[0, 0], data)
    plot_correlation_analysis(axes[0, 1], data)
    plot_histogram(axes[1, 0], data)
    plot_scatter(axes[1, 1], data)

    # 레이아웃 조정 및 플롯 표시
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

