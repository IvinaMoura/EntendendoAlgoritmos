modelo = Sequential()
modelo.add(LSTM(units=128, return_sequences=True, input_shape=(previsao.shape[1], 1), go_backwards=True))
modelo.add(Dropout(0.2))
modelo.add(LSTM(units=128, return_sequences=True,go_backwards=True))
modelo.add(Dropout(0.2))
modelo.add(LSTM(units=128))
modelo.add(Dropout(0.2))
modelo.add(Dense(units=1))

modelo.compile(optimizer='adam',
               loss='mean_squared_error',
               metrics=[MeanAbsoluteError(), RootMeanSquaredError()])


modelo.fit(X_treinamento, y_treinamento, batch_size=32, epochs=100, verbose=1)

keras.saving.save_model(modelo, 'LSTM_dengue.keras')