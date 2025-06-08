# Problem 5 - MNIST手写数字识别

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# 1. 数据加载与预处理
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 归一化像素值到[0,1]范围
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# 将标签转换为one-hot编码
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# 2. 模型构建
model = Sequential([
    Flatten(input_shape=(28, 28)),  # 将28x28图像展平
    Dense(128, activation='relu'),  # 隐藏层(128个神经元)
    Dense(64, activation='relu'),   # 第二个隐藏层(64个神经元)
    Dense(10, activation='softmax') # 输出层(10个类别)
])

# 3. 模型编译与训练
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 训练模型(10个epoch)
history = model.fit(x_train, y_train,
                    epochs=10,
                    batch_size=64,
                    validation_split=0.1,
                    verbose=1)

# 4. 性能评估
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"测试集准确率: {test_acc:.4f}")

# 5. 模型保存
model.save('mnist_model.h5')

assert test_acc >= 0.95, "模型未达到95%准确率要求"