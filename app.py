"""Bike Sharing Demand — Streamlit ARIMA 시계열 예측 웹앱."""
import pandas as pd
import streamlit as st
from statsmodels.tsa.arima.model import ARIMA

st.title("Bike Sharing 시계열 예측")
st.write("월별 자전거 대여량을 확인하고 미래 값을 예측합니다.")

uploaded_file = st.file_uploader("Bike_Sharing_Demand.csv 업로드", type=["csv"])

if uploaded_file is not None:
    bike = pd.read_csv(uploaded_file)
    st.subheader("원본 데이터")
    st.dataframe(bike)

    bike["datetime"] = pd.to_datetime(bike["datetime"])
    bike = bike.sort_values("datetime").reset_index(drop=True)

    bike["month"] = bike["datetime"].dt.to_period("M").dt.to_timestamp()
    monthly = bike.groupby("month", as_index=False)["count"].sum()
    monthly = monthly.set_index("month")

    st.subheader("월별 대여량")
    st.dataframe(monthly)
    st.line_chart(monthly["count"])

    forecast_period = st.selectbox("예측 기간(개월)", [1, 3, 6])

    model = ARIMA(monthly["count"], order=(2, 1, 1))
    model_fit = model.fit()
    forecast_values = model_fit.forecast(steps=forecast_period)

    last_month = monthly.index.max()
    future_index = pd.date_range(
        start=last_month + pd.offsets.MonthBegin(1),
        periods=forecast_period,
        freq="MS",
    )
    forecast_df = pd.DataFrame(
        {"predicted_count": forecast_values.values},
        index=future_index,
    )
    forecast_df.index.name = "month"

    st.subheader("미래 예측 결과")
    st.dataframe(forecast_df)

    combined = pd.concat(
        [
            monthly.rename(columns={"count": "value"}).assign(type="actual"),
            forecast_df.rename(columns={"predicted_count": "value"}).assign(type="forecast"),
        ]
    )
    chart_df = pd.DataFrame({
        "actual": monthly["count"],
        "forecast": forecast_df["predicted_count"],
    })
    st.subheader("실제값 + 미래 예측")
    st.line_chart(chart_df)
else:
    st.info("CSV 파일을 업로드하면 월별 집계와 ARIMA 예측을 확인할 수 있습니다.")
