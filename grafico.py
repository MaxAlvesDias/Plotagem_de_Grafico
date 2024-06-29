import yfinance as yf
import mplfinance as mpf

# Definição do ativo pretendido e o intervalo de tempo
ticker = "USDBRL=X"
start_date = "2024-06-01"
end_date = "2024-06-27" 

# Download dos dados escolhidos
data = yf.download(ticker, start=start_date, end=end_date, interval="5m")

# Verifica se os dados foram obtidos com sucesso
if data.empty:
    print("Nenhum dado encontrado para o intervalo especificado.")
else:
    # Calculo das médias móveis de 9 e 20 períodos
    data['SMA_9'] = data['Close'].rolling(window=9).mean()
    data['SMA_20'] = data['Close'].rolling(window=20).mean()

    # Plotagem do gráfico de velas com as médias móveis sem os dias não comerciais
    mpf.plot(data, type='candle', style='charles',
             title=f'Gráfico de Candlestick para USD/BRL em {start_date}',
             ylabel='Preço (BRL)',
             show_nontrading=False,
             mav=(9, 20),
             )
