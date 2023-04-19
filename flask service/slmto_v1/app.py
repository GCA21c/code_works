from flask import Flask, request, render_template
import random
from collections import Counter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_numbers', methods=['POST'])
def generate_numbers():
    # 45 이하의 숫자 행운숫자 x개 생성(x=행운숫자)
    numbers = [random.randint(1, 45) for _ in range(19850831)]

    # 가장 많이 생성된 숫자를 찾아서 리스트로 만들기
    number_counts = Counter(numbers)
    sorted_numbers = sorted(number_counts, key=lambda x: number_counts[x], reverse=True)
    most_common_numbers = sorted_numbers[:30]

    number_sets = []
    for i in range(5):
        start_idx = i * 6
        end_idx = start_idx + 6
        number_set = most_common_numbers[start_idx:end_idx]
        number_sets.append(number_set)

    return render_template('result.html', number_sets=number_sets)

if __name__ == '__main__':
    app.run(debug=True)
